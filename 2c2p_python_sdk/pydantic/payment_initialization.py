# coding: utf-8

"""
    PGW Payment API 4.3

    Rest API for PGW payment purpose - LATEST

    The version of the OpenAPI document: 4.3
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel

from 2c2p_python_sdk.pydantic.locale import Locale

class PaymentInitialization(BaseModel):
    locale: typing.Optional[typing.Optional[typing.List[Locale]]] = Field(None, alias='locale')
    class Config:
        arbitrary_types_allowed = True