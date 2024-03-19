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

from 2c2p_python_sdk.pydantic.browser_details import BrowserDetails
from 2c2p_python_sdk.pydantic.payment_params_request_v43 import PaymentParamsRequestV43

class PaymentRequestV43(BaseModel):
    payment_token: str = Field(alias='paymentToken')

    payment: typing.Optional[PaymentParamsRequestV43] = Field(None, alias='payment')

    response_return_url: typing.Optional[typing.Optional[str]] = Field(None, alias='responseReturnUrl')

    client_i_p: typing.Optional[typing.Optional[str]] = Field(None, alias='clientIP')

    locale: typing.Optional[typing.Optional[str]] = Field(None, alias='locale')

    client_i_d: typing.Optional[str] = Field(None, alias='clientID')

    browser_details: typing.Optional[BrowserDetails] = Field(None, alias='browserDetails')
    class Config:
        arbitrary_types_allowed = True
