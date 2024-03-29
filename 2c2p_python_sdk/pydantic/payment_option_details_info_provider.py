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

from 2c2p_python_sdk.pydantic.payment_option_details_info_provider_channels import PaymentOptionDetailsInfoProviderChannels
from 2c2p_python_sdk.pydantic.pod_info_provider_merchant_details import PodInfoProviderMerchantDetails
from 2c2p_python_sdk.pydantic.pod_info_provider_transaction_details import PodInfoProviderTransactionDetails

class PaymentOptionDetailsInfoProvider(BaseModel):
    id: typing.Optional[typing.Optional[str]] = Field(None, alias='id')

    channels: typing.Optional[PaymentOptionDetailsInfoProviderChannels] = Field(None, alias='channels')

    merchant_details: typing.Optional[PodInfoProviderMerchantDetails] = Field(None, alias='merchantDetails')

    transaction_details: typing.Optional[PodInfoProviderTransactionDetails] = Field(None, alias='transactionDetails')

    terms: typing.Optional[typing.Optional[str]] = Field(None, alias='terms')

    terms_consent: typing.Optional[bool] = Field(None, alias='termsConsent')
    class Config:
        arbitrary_types_allowed = True
