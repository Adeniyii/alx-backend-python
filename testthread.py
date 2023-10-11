#!/usr/bin/env python3
"""wazzzzap"""
import requests
import time
import threading
import concurrent.futures


thread_local = threading.local()


def get_session():
    if hasattr(thread_local, "session"):
        return thread_local.session
    setattr(thread_local, "session", requests.Session())
    return thread_local.session


def download_sites(url: str):
    """download sites"""
    session = get_session()
    with session.get(url) as response:
        print("url: {}, res: {}\n".format(url, len(response.content)))


def make_reqs(sites):
    """make requests to sites"""
    with concurrent.futures.ThreadPoolExecutor(20) as executor:
        executor.map(download_sites, sites)


if __name__ == "__main__":
    sites = [
        "https://go.dev",
        "https://go.dev",
    ] * 50

    start_time = time.time()
    make_reqs(sites)
    duration = time.time() - start_time
    print("duration: {}".format(duration))
