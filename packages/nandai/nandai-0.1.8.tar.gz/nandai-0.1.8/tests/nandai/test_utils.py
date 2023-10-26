from __future__ import annotations
import asyncio
import pytest
from nandai.utils import batch_async
from nandai.utils import replace_with_correction


async def async_func(data):
    await asyncio.sleep(0.01)
    return f"{data}"


@pytest.mark.asyncio
async def test_batch_async():
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    batch_size = 3

    expected_results = [
        "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"
    ]

    results = await batch_async(data, async_func, batch_size)

    assert results == expected_results


def test_replace_with_correction():
    text = 'Kjelsberg was born in Oslo, he was a Norwegian politician.'
    corr = {"Kjelsberg was born in Oslo": "Kjelsberg was born in Svelvik, Vestfold"}
    assert replace_with_correction(text, {}) == text
    assert replace_with_correction(text, corr) == 'Kjelsberg was born in Svelvik, Vestfold, he was a Norwegian politician.'
    assert replace_with_correction(text, corr, lambda x, y: 'www') == 'www, he was a Norwegian politician.'
