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

from 2c2p_python_sdk.type.loyalty_details import LoyaltyDetails

class RequiredPaymentParamsDataRequestV43(TypedDict):
    pass

class OptionalPaymentParamsDataRequestV43(TypedDict, total=False):
    accountTokenization: bool

    customerToken: typing.Optional[str]

    name: typing.Optional[str]

    email: typing.Optional[str]

    mobileNo: typing.Optional[str]

    accountNo: typing.Optional[str]

    securePayToken: typing.Optional[str]

    cardBank: typing.Optional[str]

    cardCountry: typing.Optional[str]

    installmentPeriod: int

    payLaterPeriod: typing.Optional[int]

    interestType: typing.Optional[str]

    securityCode: typing.Optional[str]

    qrType: typing.Optional[str]

    fxRateID: typing.Optional[str]

    billingAddress1: typing.Optional[str]

    billingAddress2: typing.Optional[str]

    billingAddress3: typing.Optional[str]

    billingCity: typing.Optional[str]

    billingState: typing.Optional[str]

    billingPostalCode: typing.Optional[str]

    billingCountryCode: typing.Optional[str]

    paymentExpiry: typing.Optional[str]

    cardNo: typing.Optional[str]

    expiryMonth: typing.Optional[str]

    expiryYear: typing.Optional[str]

    pin: typing.Optional[str]

    loyaltyPoints: typing.Optional[typing.List[LoyaltyDetails]]

    customerNote: typing.Optional[str]

    userAgent: typing.Optional[str]

class PaymentParamsDataRequestV43(RequiredPaymentParamsDataRequestV43, OptionalPaymentParamsDataRequestV43):
    pass
