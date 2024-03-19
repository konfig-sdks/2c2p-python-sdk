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


class PaymentResponse(BaseModel):
    channel_code: typing.Optional[typing.Optional[str]] = Field(None, alias='channelCode')

    resp_code: typing.Optional[typing.Optional[str]] = Field(None, alias='respCode')

    resp_desc: typing.Optional[typing.Optional[str]] = Field(None, alias='respDesc')
    class Config:
        arbitrary_types_allowed = True
