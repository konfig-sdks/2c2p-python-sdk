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

from 2c2p_python_sdk.type.ipp_plan import IppPlan
from 2c2p_python_sdk.type.payment_option_details_custom_data import PaymentOptionDetailsCustomData
from 2c2p_python_sdk.type.payment_option_details_info_provider import PaymentOptionDetailsInfoProvider

class RequiredPaymentOptionDetailsInfo(TypedDict):
    pass

class OptionalPaymentOptionDetailsInfo(TypedDict, total=False):
    terms: typing.Optional[str]

    promoUrl: typing.Optional[str]

    plans: typing.Optional[typing.List[IppPlan]]

    customData: typing.Optional[typing.List[PaymentOptionDetailsCustomData]]

    provider: PaymentOptionDetailsInfoProvider

    learnMoreUrl: typing.Optional[str]

    termsConsent: bool

class PaymentOptionDetailsInfo(RequiredPaymentOptionDetailsInfo, OptionalPaymentOptionDetailsInfo):
    pass
