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

from 2c2p_python_sdk.pydantic.transaction_status_info import TransactionStatusInfo
from 2c2p_python_sdk.pydantic.transaction_status_merchant import TransactionStatusMerchant
from 2c2p_python_sdk.pydantic.transaction_status_payment import TransactionStatusPayment

class TransactionStatusAdditionalInfo(BaseModel):
    merchant_details: typing.Optional[TransactionStatusMerchant] = Field(None, alias='merchantDetails')

    transaction_details: typing.Optional[TransactionStatusInfo] = Field(None, alias='transactionDetails')

    payment_result_details: typing.Optional[TransactionStatusPayment] = Field(None, alias='paymentResultDetails')
    class Config:
        arbitrary_types_allowed = True
