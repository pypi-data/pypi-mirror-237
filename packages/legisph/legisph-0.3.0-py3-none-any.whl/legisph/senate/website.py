import re
from datetime import timedelta, datetime
from itertools import islice
from pathlib import Path
from typing import Union, Dict
from urllib.parse import urlencode, urljoin

from bs4 import BeautifulSoup, NavigableString
from more_itertools import grouper, split_when
from requests import Response

from .models import SenateBill, Senator, SenateCommittee
from ..core.models import LegislativeVote, LegislativeSubject
from ..core.website import Website, NotFoundError, ServerError, Link


class SenateWebsite(Website):
    """
    The Senate Website, accessible at https://legacy.senate.gov.ph/.
    """

    base_url = "https://legacy.senate.gov.ph"

    def __init__(self, cache_dir=Path(".cache/senate"), **kwargs):
        super().__init__(
            cache_name="senate_requests", cache_dir=cache_dir.absolute(), **kwargs
        )

    def fetch_bill_info(
        self, url: str, params: Dict[str, str], expire_after: Union[timedelta, int] = -1
    ) -> Response:
        # Make an initial GET request to access the form parameters
        resp = self.session.get(url=url, params=params, expire_after=expire_after)
        html = BeautifulSoup(resp.text, features="html5lib")

        # Handle error cases
        content_str = html.find("td", {"id": "content"}).text.strip()
        match content_str:
            case "Not found.":
                raise NotFoundError(f"{url} not found", url)
            case "An error has occurred. Exception has been logged.":
                raise ServerError(f"Internal Error for {url}", url)

        # Access the form parameters and update to fetch all information
        form = html.find(name="form", attrs={"name": "form1"})
        inputs = form.find_all(name="input")
        data = {i["id"]: i.attrs.get("value", "") for i in inputs}
        data.update({"__EVENTTARGET": "lbAll", "__EVENTARGUMENT": ""})

        # Fetch bill information
        return self.session.post(url, params=params, data=data)

    def fetch_bill(
        self,
        congress: int,
        bill_num: str,
        expire_after: Union[timedelta, int] = -1,
    ) -> SenateBill:
        """
        Fetch and parse a bill from the Senate Website and return a `SenateBill` object.

        Args:
           congress (int): Order of Congress (e.g., 18th congress is 18)
           bill_num (str): Senate bill number in the format SBN-XXXX
           expire_after (Union[timedelta, int]): Time Delta or integer days.
        """

        # Initial parameters
        url = f"{self.base_url}/lis/bill_res.aspx"
        params = {"q": bill_num, "congress": congress}

        # Fetch bill information
        resp = self.fetch_bill_info(url, params, expire_after)

        # Break the data into parts
        html = BeautifulSoup(resp.text, features="html5lib")
        content = html.find("td", attrs={"id": "content"})
        title = list(islice(content.children, 5))
        data = {
            item.find_previous().text.strip(): item
            for item in content.find_all("blockquote", recursive=False)
        }

        # Parse through complex votes table
        if votes := data.get("Vote(s)"):

            def parse_votes(votes_list):
                tally = {}
                for vote in votes_list:
                    tds = vote.find_all("td")
                    tally = tally | {
                        vote.text.strip(): (
                            [
                                Senator(name=voter.text.strip())
                                for voter in voters.find("blockquote").children
                                if voter.text.strip() != ""
                            ]
                            if vote.text.strip() != "Abstained"
                            else [
                                Senator(name=f"{senator[0]}, {senator[1]}")
                                for senator in grouper(
                                    voters.text.strip().split(", "), 2
                                )
                            ]
                        )
                        for vote, voters in zip(
                            tds[0 : (len(tds) // 2)],
                            tds[len(tds) // 2 : len(tds) + 1],
                        )
                    }
                return tally

            elems = (e for e in votes.children if not isinstance(e, NavigableString))
            votes = list(split_when(elems, lambda _, y: y.name == "blockquote"))
            votes = [
                LegislativeVote(
                    type=vote[0].text.split("(")[0].strip(),
                    date=datetime.strptime(
                        vote[0].text.split("(")[1].replace(")", ""), "%m/%d/%Y"
                    ),
                    tally=parse_votes(vote[1:]),
                )
                for vote in votes
            ]

        # Parse subtitle
        subtitle = title[4].text.strip()
        subtitle = subtitle.split("Filed on ")[1].split(" by")

        # Construct Senate Bill
        bill = SenateBill(
            url=url + "?" + urlencode(params),
            congress=congress,
            bill_num=bill_num,
            congress_text=title[0].text.strip(),
            bill_num_text=title[2].text.strip(),
            title=content.find("div", class_="lis_doctitle").text.strip(),
            long_title=data["Long title"].text.strip(),
            filing_date=datetime.strptime(subtitle[0], "%B %d, %Y"),
            filers=(
                [
                    Senator(name=f"{s[0]}, {s[1]}".strip())
                    for s in grouper(subtitle[1].split(", "), 2)
                ]
                if subtitle[1] != ""
                else None
            ),
            links=(
                [
                    Link(url=urljoin(url, t["href"]), name=t.text.strip())
                    for t in links.find_all("a")
                ]
                if (links := content.find("div", id="lis_download"))
                else None
            ),
            scope=data["Scope"].text.strip(),
            legislative_status=SenateBill.SenateBillStatus(
                date=datetime.strptime(
                    re.findall(
                        r"\((.+)\)", (s := data["Legislative status"].text.strip())
                    )[0],
                    "%m/%d/%Y",
                ),
                item=re.findall(r"(.+) \(", s)[0],
            ),
            subjects=(
                [
                    LegislativeSubject(name=subject.text)
                    for subject in subjects
                    if subject.text != ""
                ]
                if (subjects := data.get("Subject(s)"))
                else None
            ),
            primary_committee=(
                [
                    SenateCommittee(name=committee.text)
                    for committee in committees.children
                    if committee.text != ""
                ]
                if (committees := data.get("Primary committee"))
                else None
            ),
            secondary_committee=(
                [
                    SenateCommittee(name=committee.text)
                    for committee in committees.children
                    if committee.text != ""
                ]
                if (committees := data.get("Secondary committee"))
                else None
            ),
            committee_reports=(
                [
                    Link(url=urljoin(url, report["href"]), name=report.text)
                    for report in reports.find_all("a")
                ]
                if (reports := data.get("Committee report"))
                else None
            ),
            sponsors=(
                [
                    Senator(name=f"{senator[0]}, {senator[1]}")
                    for senator in grouper(sponsors.text.split(", "), 2)
                ]
                if (sponsors := data.get("Sponsor(s)"))
                else None
            ),
            cosponsors=(
                [
                    Senator(name=f"{senator[0]}, {senator[1]}")
                    for senator in grouper(cosponsors.text.split(", "), 2)
                ]
                if (cosponsors := data.get("Co-sponsor(s)"))
                else None
            ),
            document_certification=(
                certification.text
                if (certification := data.get("Document certification"))
                else None
            ),
            floor_activity=(
                [
                    SenateBill.SenateFloorActivity(
                        date=datetime.strptime(cols[0].text.strip(), "%m/%d/%Y"),
                        parliamentary_status=cols[1].text.strip(),
                        senators=(
                            [
                                Senator(name=senator.text.strip())
                                for senator in cols[2].children
                                if senator.text.strip() != ""
                            ]
                            if len(list(cols[2].children)) > 0
                            else None
                        ),
                    )
                    for cols in [
                        row.find_all("td") for row in floor_activity.find_all("tr")
                    ][1:]
                ]
                if (floor_activity := data.get("Floor activity"))
                else None
            ),
            votes=votes,
            legislative_history=[
                SenateBill.SenateBillStatus(
                    date=datetime.strptime(row[0].text.strip(), "%m/%d/%Y"),
                    item=row[1].text.strip(),
                )
                for row in (
                    row.find_all("td")
                    for row in data["Legislative History"].find_all("tr")
                )
                if len(row) == 2
            ],
        )

        return bill
