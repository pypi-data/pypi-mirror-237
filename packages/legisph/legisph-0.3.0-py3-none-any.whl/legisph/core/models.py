import datetime
from typing import List, Dict

from pydantic import BaseModel


class LegislativeDocument(BaseModel):
    "Documents produced as artifacts of the legislative process."
    pass


class Bill(LegislativeDocument):
    "General measures, which if passed upon, may become laws."
    pass


class Legislator(BaseModel):
    "An elected representative of the legislative who participats in the process."
    pass


class LegislativeCommittee(BaseModel):
    """
    A smaller grouping of the legislative body who first deliberates o legislative
    actions before it is delivered to the full body
    """

    pass


class LegislativeSubject(BaseModel):
    "A subject of legislative relevance"
    name: str


class LegislativeVote(BaseModel):
    """
    A vote in a legislative body
    """

    type: str
    date: datetime.date
    tally: Dict[str, List[Legislator]]
