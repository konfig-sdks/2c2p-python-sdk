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

from 2c2p_python_sdk.type.payment_loyalty_reward import PaymentLoyaltyReward

class RequiredPaymentLoyaltyPointInfoResponse(TypedDict):
    pass

class OptionalPaymentLoyaltyPointInfoResponse(TypedDict, total=False):
    paymentToken: typing.Optional[str]

    providerID: typing.Optional[str]

    providerName: typing.Optional[str]

    referenceID: typing.Optional[str]

    providerType: typing.Optional[str]

    terms: typing.Optional[str]

    rewards: typing.Optional[typing.List[PaymentLoyaltyReward]]

    respCode: typing.Optional[str]

    respDesc: typing.Optional[str]

class PaymentLoyaltyPointInfoResponse(RequiredPaymentLoyaltyPointInfoResponse, OptionalPaymentLoyaltyPointInfoResponse):
    pass
