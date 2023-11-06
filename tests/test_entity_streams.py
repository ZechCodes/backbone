from backbone.entity_streams import EntityStream
from unittest.mock import AsyncMock, Mock
import unittest.mock as mock
import pytest


@pytest.mark.asyncio
async def test_entity_push():
    mock_consumer, mock_entity = AsyncMock(), Mock()

    stream = EntityStream()
    stream.add_consumer(mock_consumer)
    await stream.push(mock_entity)

    assert mock_consumer.await_args == mock.call(mock_entity)
