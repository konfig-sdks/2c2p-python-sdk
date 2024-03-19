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

from 2c2p_python_sdk.pydantic.merchant_configuration_payment_fx import MerchantConfigurationPaymentFx

class MerchantConfigurationPayment(BaseModel):
    tokenize: typing.Optional[bool] = Field(None, alias='tokenize')

    tokenize_only: typing.Optional[bool] = Field(None, alias='tokenizeOnly')

    card_token_only: typing.Optional[bool] = Field(None, alias='cardTokenOnly')

    immediate_payment: typing.Optional[bool] = Field(None, alias='immediatePayment')

    fx: typing.Optional[MerchantConfigurationPaymentFx] = Field(None, alias='fx')
    class Config:
        arbitrary_types_allowed = True