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

from 2c2p_python_sdk.type.payment_option_details_channel_currency_codes import PaymentOptionDetailsChannelCurrencyCodes
from 2c2p_python_sdk.type.payment_option_details_payment import PaymentOptionDetailsPayment

class RequiredPaymentOptionDetailsChannel(TypedDict):
    pass

class OptionalPaymentOptionDetailsChannel(TypedDict, total=False):
    sequenceNo: int

    name: typing.Optional[str]

    bankShortName: typing.Optional[str]

    currencyCodes: PaymentOptionDetailsChannelCurrencyCodes

    iconUrl: typing.Optional[str]

    logoUrl: typing.Optional[str]

    payment: PaymentOptionDetailsPayment

    isDown: bool

    checkEligibleOption: bool

    ippProviderCode: typing.Optional[str]

    registrationStatus: typing.Optional[str]

    partnerMerchantRefID: typing.Optional[str]

class PaymentOptionDetailsChannel(RequiredPaymentOptionDetailsChannel, OptionalPaymentOptionDetailsChannel):
    pass