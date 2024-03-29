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

from 2c2p_python_sdk.type.merchant_details import MerchantDetails
from 2c2p_python_sdk.type.payment_channel_category import PaymentChannelCategory
from 2c2p_python_sdk.type.transaction_details import TransactionDetails
from 2c2p_python_sdk.type.user_details import UserDetails

class RequiredPaymentOptionResponse(TypedDict):
    pass

class OptionalPaymentOptionResponse(TypedDict, total=False):
    paymentToken: typing.Optional[str]

    merchantDetails: MerchantDetails

    transactionDetails: TransactionDetails

    channelCategories: typing.Optional[typing.List[PaymentChannelCategory]]

    userDetails: UserDetails

    respCode: typing.Optional[str]

    respDesc: typing.Optional[str]

class PaymentOptionResponse(RequiredPaymentOptionResponse, OptionalPaymentOptionResponse):
    pass
