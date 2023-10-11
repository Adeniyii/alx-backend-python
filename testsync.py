#!/usr/bin/env python3
"""wazzzzap"""
import requests
import time


def download_sites(session: requests.Session, url):
    """download sites"""
    with session.get(url) as response:
        print("url: {}, res: {}\n".format(url, len(response.content)))


def make_reqs(sites):
    """make requests to sites"""
    with requests.Session() as sesh:
        for site in sites:
            download_sites(sesh, site)


if __name__ == "__main__":
    sites = [
        "https://go.dev"
    ] * 20

    start_time = time.time()
    make_reqs(sites)
    duration = time.time() - start_time
    print("duration: {}".format(duration))
