"""Getting data from USATT website."""
from __future__ import annotations

import logging

import pandas as pd
import requests
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)


def get_ratings(usattid: int | str) -> dict:
    """
    Get ratings for a specific USATT#.
    :param usattid: USATT#
    :return: {
        "USATT#": usattid,
        "Name": " ".join(name),
        "Tournament Rating": vals[0],
        "Highest Tournament Rating": vals[1],
        "Tournaments Played": vals[2],
        "League Rating": vals[3],
        "Highest League Rating": vals[4],
        "Leagues Played": vals[5]
    }.
    """
    r = requests.get(f"https://usatt.simplycompete.com/userAccount/s2?q={usattid}")

    if r.status_code != 200:
        raise RuntimeError("No connection to USATT.")

    soup = BeautifulSoup(r.content)

    name = []

    for link in soup.find_all("a"):
        url = link.get("href")
        if "userAccount/up" in url:
            accountid = url.split("/")[-1]
            name.append(link.text)

    r = requests.get(f"http://usatt.simplycompete.com/userAccount/up/{accountid}")
    soup = BeautifulSoup(r.content)
    vals = [int(d.text) for d in soup.find_all("span", class_="details-text")]
    return {
        "USATT#": usattid,
        "Name": " ".join(name),
        "Tournament Rating": vals[0],
        "Highest Tournament Rating": vals[1],
        "Tournaments Played": vals[2],
        "League Rating": vals[3],
        "Highest League Rating": vals[4],
        "Leagues Played": vals[5],
    }


def get_usatt_summary() -> pd.DataFrame:
    """
    Get a pandas DataFrame of a summary of all USATT ratings.

    :return:
    """
    offset = 0

    dfs = []
    while True:
        url = f"https://usatt.simplycompete.com/userAccount/s2?displayColumns=First+Name&displayColumns=Last+Name&displayColumns=USATT%23&displayColumns=Location&displayColumns=Home+Club&displayColumns=Tournament+Rating&displayColumns=Last+Played+Tournament&displayColumns=League+Rating&displayColumns=Last+Played+League&displayColumns=Membership+Expiration&pageSize=1000&format=&offset={offset}&max=1000"

        r = requests.get(url)

        if r.status_code != 200:
            raise RuntimeError("No connection to USATT.")

        df = pd.read_html(r.content)[0]

        if len(df) == 0:
            break

        logger.info(f"Entries {offset+1}-{offset+len(df)}")

        dfs.append(df)
        offset += 1000
        if offset > 30000:
            # In case there is a problem, we will break. There shouldn't be more than 30000 USATT players.
            print("Infinite loop?")
            break

    all_data = pd.concat(dfs)
    all_data = all_data[all_data.columns[2:]]
    return all_data.set_index("USATT#")
