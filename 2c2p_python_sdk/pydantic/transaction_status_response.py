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

from 2c2p_python_sdk.pydantic.transaction_status_additional_info import TransactionStatusAdditionalInfo

class TransactionStatusResponse(BaseModel):
    locale: typing.Optional[typing.Optional[str]] = Field(None, alias='locale')

    additional_info: typing.Optional[TransactionStatusAdditionalInfo] = Field(None, alias='additionalInfo')

    invoice_no: typing.Optional[typing.Optional[str]] = Field(None, alias='invoiceNo')

    channel_code: typing.Optional[typing.Optional[str]] = Field(None, alias='channelCode')

    resp_code: typing.Optional[typing.Optional[str]] = Field(None, alias='respCode')

    resp_desc: typing.Optional[typing.Optional[str]] = Field(None, alias='respDesc')
    class Config:
        arbitrary_types_allowed = True
