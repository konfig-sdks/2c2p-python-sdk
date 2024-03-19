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

from 2c2p_python_sdk.type.merchant_configuration import MerchantConfiguration
from 2c2p_python_sdk.type.payment_option_details_channel import PaymentOptionDetailsChannel
from 2c2p_python_sdk.type.payment_option_details_validation import PaymentOptionDetailsValidation

class RequiredPaymentOptionDetailsResponse(TypedDict):
    pass

class OptionalPaymentOptionDetailsResponse(TypedDict, total=False):
    totalChannel: int

    name: typing.Optional[str]

    categoryCode: typing.Optional[str]

    groupCode: typing.Optional[str]

    iconUrl: typing.Optional[str]

    channels: typing.Optional[typing.List[PaymentOptionDetailsChannel]]

    validation: PaymentOptionDetailsValidation

    configuration: MerchantConfiguration

    respCode: typing.Optional[str]

    respDesc: typing.Optional[str]

class PaymentOptionDetailsResponse(RequiredPaymentOptionDetailsResponse, OptionalPaymentOptionDetailsResponse):
    pass