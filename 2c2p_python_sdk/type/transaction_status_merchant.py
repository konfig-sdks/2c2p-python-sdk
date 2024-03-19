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


class RequiredTransactionStatusMerchant(TypedDict):
    pass

class OptionalTransactionStatusMerchant(TypedDict, total=False):
    name: typing.Optional[str]

    address: typing.Optional[str]

    email: typing.Optional[str]

    logoUrl: typing.Optional[str]

class TransactionStatusMerchant(RequiredTransactionStatusMerchant, OptionalTransactionStatusMerchant):
    pass