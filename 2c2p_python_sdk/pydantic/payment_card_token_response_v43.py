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

from 2c2p_python_sdk.pydantic.credit_card_token_v43 import CreditCardTokenV43

class PaymentCardTokenResponseV43(BaseModel):
    payment_token: typing.Optional[typing.Optional[str]] = Field(None, alias='paymentToken')

    customer_token: typing.Optional[typing.Optional[typing.List[CreditCardTokenV43]]] = Field(None, alias='customerToken')

    resp_code: typing.Optional[typing.Optional[str]] = Field(None, alias='respCode')

    resp_desc: typing.Optional[typing.Optional[str]] = Field(None, alias='respDesc')
    class Config:
        arbitrary_types_allowed = True
