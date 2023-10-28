import pytest

from faststream.rabbit import TestRabbitBroker
from faststream.annotations import ContextRepo
from unittest.mock import AsyncMock, MagicMock

from .actor import cache

from .broker import broker, inbox_queue, exch


@pytest.fixture
async def test_broker():
    async with TestRabbitBroker(broker) as br:
        context = ContextRepo()
        context.set_global("session", AsyncMock())
        context.set_global("logger", AsyncMock())

        actor = AsyncMock()
        actor.actor_id = "http://local/actor"
        cache["bovine_name"] = actor
        actor.actor_object.build = MagicMock(
            return_value={"endpoints": {"eventSource": "xxxx"}}
        )

        yield br


async def test_inbox_handler(test_broker):
    remote_actor = "https://remote.example/actor"

    await test_broker.publish(
        {
            "bovine_name": "bovine_name",
            "submitter": remote_actor,
            "data": {
                "@context": "about:bovine",
                "actor": remote_actor,
                "type": "Like",
            },
        },
        exchange=exch,
        queue=inbox_queue,
    )
