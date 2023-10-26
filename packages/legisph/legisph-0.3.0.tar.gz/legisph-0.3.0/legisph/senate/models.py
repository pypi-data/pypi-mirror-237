import datetime
from typing import Optional, List

from pydantic import BaseModel

from ..core.models import (
    Bill,
    Legislator,
    LegislativeCommittee,
    LegislativeSubject,
    LegislativeVote,
)
from ..core.website import Link


class Senator(Legislator):
    """A member of the Senate"""

    name: str


class SenateCommittee(LegislativeCommittee):
    """A committee in the Senate"""

    name: str


class SenateBill(Bill):
    """
    Senate Bill

    A bill is prefixed with S., followed by a number assigned the measure based
    on the order in which it is introduced. The vast majority of legislative
    proposals recommendations dealing with the economy, increasing penalties
    for certain crimes, regulation on commerce and trade, etc., are drafted in
    the form of bills. They also include budgetary appropriation of the
    government and many others. When passed by both chambers in identical
    form and signed by the President or repassed by Congress over a presidential
    veto, they become laws.

    [Definition Source](http://legacy.senate.gov.ph/about/legpro.asp)
    """

    class SenateBillStatus(BaseModel):
        date: datetime.date
        item: str

    class SenateFloorActivity(BaseModel):
        date: datetime.date
        parliamentary_status: str
        senators: Optional[List[Senator]]

    url: str
    congress: int
    bill_num: str
    congress_text: str
    bill_num_text: str
    title: str
    long_title: str
    filing_date: datetime.date
    filers: Optional[List[Senator]] = None
    links: Optional[List[Link]] = None
    scope: str
    legislative_status: SenateBillStatus
    subjects: Optional[List[LegislativeSubject]] = None
    primary_committee: Optional[List[SenateCommittee]] = None
    secondary_committee: Optional[List[SenateCommittee]] = None
    committee_reports: Optional[List[Link]] = None
    sponsors: Optional[List[Senator]] = None
    cosponsors: Optional[List[Senator]] = None
    document_certification: Optional[str] = None
    floor_activity: Optional[List[SenateFloorActivity]]
    votes: Optional[List[LegislativeVote]]
    legislative_history: List[SenateBillStatus]

    def __str__(self):
        return f"[{self.billno}] {self.title}"
