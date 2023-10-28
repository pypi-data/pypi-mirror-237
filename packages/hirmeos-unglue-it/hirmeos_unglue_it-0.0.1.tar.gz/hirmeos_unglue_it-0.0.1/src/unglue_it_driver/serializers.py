from typing import List

from pydantic import BaseModel, Field


class UnglueIdentifier(BaseModel):
    edition: str
    id: int
    type: str
    value: str
    work: str

class UnglueReportItem(BaseModel):
    downloads: int = Field(alias="download_count")
    isbn: UnglueIdentifier
