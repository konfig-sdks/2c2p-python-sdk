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

from 2c2p_python_sdk.type.currency_apmmccfx_rate import CurrencyAPMMCCFxRate

class RequiredPaymentApmMccExchangeRateResponse(TypedDict):
    pass

class OptionalPaymentApmMccExchangeRateResponse(TypedDict, total=False):
    fxRates: typing.Optional[typing.List[CurrencyAPMMCCFxRate]]

    paymentToken: typing.Optional[str]

    respCode: typing.Optional[str]

    respDesc: typing.Optional[str]

class PaymentApmMccExchangeRateResponse(RequiredPaymentApmMccExchangeRateResponse, OptionalPaymentApmMccExchangeRateResponse):
    pass
