# pylint: disable=too-few-public-methods

from __future__ import annotations

from sqlalchemy.orm import Mapped, mapped_column

from sqlalchemy import Integer, String


from multi_processing.models.base import BaseModel


class Data(BaseModel):
    __tablename__ = "data"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    content: Mapped[str] = mapped_column(String(1024), nullable=True)
