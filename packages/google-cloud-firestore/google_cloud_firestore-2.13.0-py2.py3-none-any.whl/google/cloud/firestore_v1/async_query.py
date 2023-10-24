# Copyright 2020 Google LLC All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Classes for representing queries for the Google Cloud Firestore API.

A :class:`~google.cloud.firestore_v1.query.Query` can be created directly from
a :class:`~google.cloud.firestore_v1.collection.Collection` and that can be
a more common way to create a query than direct usage of the constructor.
"""
from __future__ import annotations

from google.api_core import gapic_v1
from google.api_core import retry as retries

from google.cloud import firestore_v1
from google.cloud.firestore_v1.base_query import (
    BaseCollectionGroup,
    BaseQuery,
    QueryPartition,
    _query_response_to_snapshot,
    _collection_group_query_response_to_snapshot,
    _enum_from_direction,
)

from google.cloud.firestore_v1 import async_document
from google.cloud.firestore_v1.async_aggregation import AsyncAggregationQuery
from google.cloud.firestore_v1.base_document import DocumentSnapshot
from typing import AsyncGenerator, List, Optional, Type, TYPE_CHECKING

if TYPE_CHECKING:  # pragma: NO COVER
    # Types needed only for Type Hints
    from google.cloud.firestore_v1.transaction import Transaction
    from google.cloud.firestore_v1.field_path import FieldPath


class AsyncQuery(BaseQuery):
    """Represents a query to the Firestore API.

    Instances of this class are considered immutable: all methods that
    would modify an instance instead return a new instance.

    Args:
        parent (:class:`~google.cloud.firestore_v1.collection.CollectionReference`):
            The collection that this query applies to.
        projection (Optional[:class:`google.cloud.proto.firestore.v1.\
            query.StructuredQuery.Projection`]):
            A projection of document fields to limit the query results to.
        field_filters (Optional[Tuple[:class:`google.cloud.proto.firestore.v1.\
            query.StructuredQuery.FieldFilter`, ...]]):
            The filters to be applied in the query.
        orders (Optional[Tuple[:class:`google.cloud.proto.firestore.v1.\
            query.StructuredQuery.Order`, ...]]):
            The "order by" entries to use in the query.
        limit (Optional[int]):
            The maximum number of documents the query is allowed to return.
        offset (Optional[int]):
            The number of results to skip.
        start_at (Optional[Tuple[dict, bool]]):
            Two-tuple of :

            * a mapping of fields. Any field that is present in this mapping
              must also be present in ``orders``
            * an ``after`` flag

            The fields and the flag combine to form a cursor used as
            a starting point in a query result set. If the ``after``
            flag is :data:`True`, the results will start just after any
            documents which have fields matching the cursor, otherwise
            any matching documents will be included in the result set.
            When the query is formed, the document values
            will be used in the order given by ``orders``.
        end_at (Optional[Tuple[dict, bool]]):
            Two-tuple of:

            * a mapping of fields. Any field that is present in this mapping
              must also be present in ``orders``
            * a ``before`` flag

            The fields and the flag combine to form a cursor used as
            an ending point in a query result set. If the ``before``
            flag is :data:`True`, the results will end just before any
            documents which have fields matching the cursor, otherwise
            any matching documents will be included in the result set.
            When the query is formed, the document values
            will be used in the order given by ``orders``.
        all_descendants (Optional[bool]):
            When false, selects only collections that are immediate children
            of the `parent` specified in the containing `RunQueryRequest`.
            When true, selects all descendant collections.
        recursive (Optional[bool]):
            When true, returns all documents and all documents in any subcollections
            below them. Defaults to false.
    """

    def __init__(
        self,
        parent,
        projection=None,
        field_filters=(),
        orders=(),
        limit=None,
        limit_to_last=False,
        offset=None,
        start_at=None,
        end_at=None,
        all_descendants=False,
        recursive=False,
    ) -> None:
        super(AsyncQuery, self).__init__(
            parent=parent,
            projection=projection,
            field_filters=field_filters,
            orders=orders,
            limit=limit,
            limit_to_last=limit_to_last,
            offset=offset,
            start_at=start_at,
            end_at=end_at,
            all_descendants=all_descendants,
            recursive=recursive,
        )

    async def _chunkify(
        self, chunk_size: int
    ) -> AsyncGenerator[List[DocumentSnapshot], None]:
        max_to_return: Optional[int] = self._limit
        num_returned: int = 0
        original: AsyncQuery = self._copy()
        last_document: Optional[DocumentSnapshot] = None

        while True:
            # Optionally trim the `chunk_size` down to honor a previously
            # applied limit as set by `self.limit()`
            _chunk_size: int = original._resolve_chunk_size(num_returned, chunk_size)

            # Apply the optionally pruned limit and the cursor, if we are past
            # the first page.
            _q = original.limit(_chunk_size)

            if last_document:
                _q = _q.start_after(last_document)

            snapshots = await _q.get()

            if snapshots:
                last_document = snapshots[-1]

            num_returned += len(snapshots)

            yield snapshots

            # Terminate the iterator if we have reached either of two end
            # conditions:
            #   1. There are no more documents, or
            #   2. We have reached the desired overall limit
            if len(snapshots) < _chunk_size or (
                max_to_return and num_returned >= max_to_return
            ):
                return

    async def get(
        self,
        transaction: Transaction = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
    ) -> list:
        """Read the documents in the collection that match this query.

        This sends a ``RunQuery`` RPC and returns a list of documents
        returned in the stream of ``RunQueryResponse`` messages.

        Args:
            transaction
                (Optional[:class:`~google.cloud.firestore_v1.transaction.Transaction`]):
                An existing transaction that this query will run in.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.  Defaults to a system-specified policy.
            timeout (float): The timeout for this request.  Defaults to a
                system-specified value.

        If a ``transaction`` is used and it already has write operations
        added, this method cannot be used (i.e. read-after-write is not
        allowed).

        Returns:
            list: The documents in the collection that match this query.
        """
        is_limited_to_last = self._limit_to_last

        if self._limit_to_last:
            # In order to fetch up to `self._limit` results from the end of the
            # query flip the defined ordering on the query to start from the
            # end, retrieving up to `self._limit` results from the backend.
            for order in self._orders:
                order.direction = _enum_from_direction(
                    self.DESCENDING
                    if order.direction == self.ASCENDING
                    else self.ASCENDING
                )
            self._limit_to_last = False

        result = self.stream(transaction=transaction, retry=retry, timeout=timeout)
        result = [d async for d in result]
        if is_limited_to_last:
            result = list(reversed(result))

        return result

    def count(
        self, alias: str | None = None
    ) -> Type["firestore_v1.async_aggregation.AsyncAggregationQuery"]:
        """Adds a count over the nested query.

        Args:
            alias(Optional[str]): Optional name of the field to store the result of the aggregation into.
                If not provided, Firestore will pick a default name following the format field_<incremental_id++>.

        Returns:
            :class:`~google.cloud.firestore_v1.async_aggregation.AsyncAggregationQuery`:
            An instance of an AsyncAggregationQuery object
        """
        return AsyncAggregationQuery(self).count(alias=alias)

    def sum(
        self, field_ref: str | FieldPath, alias: str | None = None
    ) -> Type["firestore_v1.async_aggregation.AsyncAggregationQuery"]:
        """Adds a sum over the nested query.

        Args:
            field_ref(Union[str, google.cloud.firestore_v1.field_path.FieldPath]): The field to aggregate across.
            alias(Optional[str]): Optional name of the field to store the result of the aggregation into.
                If not provided, Firestore will pick a default name following the format field_<incremental_id++>.

        Returns:
            :class:`~google.cloud.firestore_v1.async_aggregation.AsyncAggregationQuery`:
            An instance of an AsyncAggregationQuery object
        """
        return AsyncAggregationQuery(self).sum(field_ref, alias=alias)

    def avg(
        self, field_ref: str | FieldPath, alias: str | None = None
    ) -> Type["firestore_v1.async_aggregation.AsyncAggregationQuery"]:
        """Adds an avg over the nested query.

        Args:
            field_ref(Union[str, google.cloud.firestore_v1.field_path.FieldPath]): The field to aggregate across.
            alias(Optional[str]): Optional name of the field to store the result of the aggregation into.
                If not provided, Firestore will pick a default name following the format field_<incremental_id++>.

        Returns:
            :class:`~google.cloud.firestore_v1.async_aggregation.AsyncAggregationQuery`:
            An instance of an AsyncAggregationQuery object
        """
        return AsyncAggregationQuery(self).avg(field_ref, alias=alias)

    async def stream(
        self,
        transaction=None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
    ) -> AsyncGenerator[async_document.DocumentSnapshot, None]:
        """Read the documents in the collection that match this query.

        This sends a ``RunQuery`` RPC and then returns an iterator which
        consumes each document returned in the stream of ``RunQueryResponse``
        messages.

        .. note::

           The underlying stream of responses will time out after
           the ``max_rpc_timeout_millis`` value set in the GAPIC
           client configuration for the ``RunQuery`` API.  Snapshots
           not consumed from the iterator before that point will be lost.

        If a ``transaction`` is used and it already has write operations
        added, this method cannot be used (i.e. read-after-write is not
        allowed).

        Args:
            transaction
                (Optional[:class:`~google.cloud.firestore_v1.transaction.Transaction`]):
                An existing transaction that this query will run in.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.  Defaults to a system-specified policy.
            timeout (float): The timeout for this request.  Defaults to a
                system-specified value.

        Yields:
            :class:`~google.cloud.firestore_v1.async_document.DocumentSnapshot`:
            The next document that fulfills the query.
        """
        request, expected_prefix, kwargs = self._prep_stream(
            transaction,
            retry,
            timeout,
        )

        response_iterator = await self._client._firestore_api.run_query(
            request=request,
            metadata=self._client._rpc_metadata,
            **kwargs,
        )

        async for response in response_iterator:
            if self._all_descendants:
                snapshot = _collection_group_query_response_to_snapshot(
                    response, self._parent
                )
            else:
                snapshot = _query_response_to_snapshot(
                    response, self._parent, expected_prefix
                )
            if snapshot is not None:
                yield snapshot

    @staticmethod
    def _get_collection_reference_class() -> (
        Type["firestore_v1.async_collection.AsyncCollectionReference"]
    ):
        from google.cloud.firestore_v1.async_collection import AsyncCollectionReference

        return AsyncCollectionReference


class AsyncCollectionGroup(AsyncQuery, BaseCollectionGroup):
    """Represents a Collection Group in the Firestore API.

    This is a specialization of :class:`.AsyncQuery` that includes all documents in the
    database that are contained in a collection or subcollection of the given
    parent.

    Args:
        parent (:class:`~google.cloud.firestore_v1.collection.CollectionReference`):
            The collection that this query applies to.
    """

    def __init__(
        self,
        parent,
        projection=None,
        field_filters=(),
        orders=(),
        limit=None,
        limit_to_last=False,
        offset=None,
        start_at=None,
        end_at=None,
        all_descendants=True,
        recursive=False,
    ) -> None:
        super(AsyncCollectionGroup, self).__init__(
            parent=parent,
            projection=projection,
            field_filters=field_filters,
            orders=orders,
            limit=limit,
            limit_to_last=limit_to_last,
            offset=offset,
            start_at=start_at,
            end_at=end_at,
            all_descendants=all_descendants,
            recursive=recursive,
        )

    @staticmethod
    def _get_query_class():
        return AsyncQuery

    async def get_partitions(
        self,
        partition_count,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
    ) -> AsyncGenerator[QueryPartition, None]:
        """Partition a query for parallelization.

        Partitions a query by returning partition cursors that can be used to run the
        query in parallel. The returned partition cursors are split points that can be
        used as starting/end points for the query results.

        Args:
            partition_count (int): The desired maximum number of partition points. The
                number must be strictly positive. The actual number of partitions
                returned may be fewer.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.  Defaults to a system-specified policy.
            timeout (float): The timeout for this request.  Defaults to a
                system-specified value.
        """
        request, kwargs = self._prep_get_partitions(partition_count, retry, timeout)
        pager = await self._client._firestore_api.partition_query(
            request=request,
            metadata=self._client._rpc_metadata,
            **kwargs,
        )

        start_at = None
        async for cursor_pb in pager:
            cursor = self._client.document(cursor_pb.values[0].reference_value)
            yield QueryPartition(self, start_at, cursor)
            start_at = cursor

        yield QueryPartition(self, start_at, None)
