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

from 2c2p_python_sdk.type.payment_item import PaymentItem
from 2c2p_python_sdk.type.recurring import Recurring

class RequiredTransactionDetails(TypedDict):
    pass

class OptionalTransactionDetails(TypedDict, total=False):
    description: typing.Optional[str]

    amount: typing.Optional[str]

    currencyCode: typing.Optional[str]

    invoiceNo: typing.Optional[str]

    recurring: Recurring

    dateTime: typing.Optional[str]

    paymentItems: typing.Optional[typing.List[PaymentItem]]

    showFxRate: bool

class TransactionDetails(RequiredTransactionDetails, OptionalTransactionDetails):
    pass
