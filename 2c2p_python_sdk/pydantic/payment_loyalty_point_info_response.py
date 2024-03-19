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

from 2c2p_python_sdk.pydantic.payment_loyalty_reward import PaymentLoyaltyReward

class PaymentLoyaltyPointInfoResponse(BaseModel):
    payment_token: typing.Optional[typing.Optional[str]] = Field(None, alias='paymentToken')

    provider_i_d: typing.Optional[typing.Optional[str]] = Field(None, alias='providerID')

    provider_name: typing.Optional[typing.Optional[str]] = Field(None, alias='providerName')

    reference_i_d: typing.Optional[typing.Optional[str]] = Field(None, alias='referenceID')

    provider_type: typing.Optional[typing.Optional[str]] = Field(None, alias='providerType')

    terms: typing.Optional[typing.Optional[str]] = Field(None, alias='terms')

    rewards: typing.Optional[typing.Optional[typing.List[PaymentLoyaltyReward]]] = Field(None, alias='rewards')

    resp_code: typing.Optional[typing.Optional[str]] = Field(None, alias='respCode')

    resp_desc: typing.Optional[typing.Optional[str]] = Field(None, alias='respDesc')
    class Config:
        arbitrary_types_allowed = True