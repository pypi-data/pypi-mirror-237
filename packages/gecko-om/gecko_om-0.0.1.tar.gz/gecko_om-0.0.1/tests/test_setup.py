import pytest


pytestmark = pytest.mark.asyncio


class TestSetup:
    async def test_init(self):
        assert 1 == 1

    async def test_init_2(self):
        assert 1 != 2
