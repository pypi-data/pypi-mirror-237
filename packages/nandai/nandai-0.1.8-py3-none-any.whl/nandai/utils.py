from __future__ import annotations

import asyncio
import re
from tqdm import tqdm
from typing import Callable
from typing import Any


async def batch_async(data: list[Any], async_func: Callable, batch_size: int):
    res = []
    with tqdm(total=len(data)) as pbar:
        for i in range(0, len(data), batch_size):
            batch = data[i:i+batch_size]
            tasks = [async_func(d) for d in batch]
            res += await asyncio.gather(*tasks)
            pbar.update(len(batch))

    return res


def replace_with_correction(
        text: str,
        correction: dict[str, str],
        replace_func: Callable[[str, str], str] = lambda _, y: y,
):
    match_regex = re.compile('(' + "|".join(re.escape(m) for m in correction) + ')')
    parts = re.split(match_regex, text)
    return ''.join([
        replace_func(p, correction[p])
        if p in correction else p for p in parts
    ])
