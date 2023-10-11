#!/usr/bin/env python3
"""wazzzzap"""
import asyncio
import time
import aiohttp


async def get_req(session, url: str):
    """wazzapppp"""
    async with session.get(url) as response:
        print("url: {}, len: {}".format(url, response.content))
        return "url: {}".format(url)


async def setup_download(sites):
    """wazzzzzzzzzzzzzzzap"""
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in sites:
            task = asyncio.ensure_future(get_req(session, url))
            tasks.append(task)

        v = await asyncio.gather(*tasks, return_exceptions=True)
        return v


if __name__ == "__main__":
    sites = [
        "https://go.dev",
        "https://go.dev",
    ] * 50
    now = time.time()
    res = asyncio.run(setup_download(sites))
    duration = time.time() - now
    print("duration: {}\n".format(duration))
    print("values: {}".format(res))
