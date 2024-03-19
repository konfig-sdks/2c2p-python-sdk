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


class PodInfoProviderMerchantDetails(BaseModel):
    id: typing.Optional[typing.Optional[str]] = Field(None, alias='id')

    name: typing.Optional[typing.Optional[str]] = Field(None, alias='name')

    country_code: typing.Optional[typing.Optional[str]] = Field(None, alias='countryCode')
    class Config:
        arbitrary_types_allowed = True
