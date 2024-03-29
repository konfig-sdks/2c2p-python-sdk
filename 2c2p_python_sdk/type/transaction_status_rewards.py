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


class RequiredTransactionStatusRewards(TypedDict):
    pass

class OptionalTransactionStatusRewards(TypedDict, total=False):
    totalPrice: typing.Union[int, float]

    totalAmount: typing.Union[int, float]

    name: typing.Optional[str]

    type: typing.Optional[str]

    amount: typing.Union[int, float]

    quantity: typing.Union[int, float]

    price: typing.Union[int, float]

class TransactionStatusRewards(RequiredTransactionStatusRewards, OptionalTransactionStatusRewards):
    pass
