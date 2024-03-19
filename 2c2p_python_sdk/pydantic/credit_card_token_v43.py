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


class CreditCardTokenV43(BaseModel):
    token: typing.Optional[typing.Optional[str]] = Field(None, alias='token')

    account_no: typing.Optional[typing.Optional[str]] = Field(None, alias='accountNo')

    name: typing.Optional[typing.Optional[str]] = Field(None, alias='name')

    email: typing.Optional[typing.Optional[str]] = Field(None, alias='email')

    expiry: typing.Optional[typing.Optional[str]] = Field(None, alias='expiry')

    channel_code: typing.Optional[typing.Optional[str]] = Field(None, alias='channelCode')

    sub_channel_code: typing.Optional[typing.Optional[str]] = Field(None, alias='subChannelCode')

    card_brand: typing.Optional[typing.Optional[str]] = Field(None, alias='cardBrand')

    status: typing.Optional[typing.Optional[str]] = Field(None, alias='status')

    icon_url: typing.Optional[typing.Optional[str]] = Field(None, alias='iconUrl')

    logo_url: typing.Optional[typing.Optional[str]] = Field(None, alias='logoUrl')
    class Config:
        arbitrary_types_allowed = True