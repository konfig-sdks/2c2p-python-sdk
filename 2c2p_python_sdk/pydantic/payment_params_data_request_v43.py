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

from 2c2p_python_sdk.pydantic.loyalty_details import LoyaltyDetails

class PaymentParamsDataRequestV43(BaseModel):
    account_tokenization: typing.Optional[bool] = Field(None, alias='accountTokenization')

    customer_token: typing.Optional[typing.Optional[str]] = Field(None, alias='customerToken')

    name: typing.Optional[typing.Optional[str]] = Field(None, alias='name')

    email: typing.Optional[typing.Optional[str]] = Field(None, alias='email')

    mobile_no: typing.Optional[typing.Optional[str]] = Field(None, alias='mobileNo')

    account_no: typing.Optional[typing.Optional[str]] = Field(None, alias='accountNo')

    secure_pay_token: typing.Optional[typing.Optional[str]] = Field(None, alias='securePayToken')

    card_bank: typing.Optional[typing.Optional[str]] = Field(None, alias='cardBank')

    card_country: typing.Optional[typing.Optional[str]] = Field(None, alias='cardCountry')

    installment_period: typing.Optional[int] = Field(None, alias='installmentPeriod')

    pay_later_period: typing.Optional[typing.Optional[int]] = Field(None, alias='payLaterPeriod')

    interest_type: typing.Optional[typing.Optional[str]] = Field(None, alias='interestType')

    security_code: typing.Optional[typing.Optional[str]] = Field(None, alias='securityCode')

    qr_type: typing.Optional[typing.Optional[str]] = Field(None, alias='qrType')

    fx_rate_i_d: typing.Optional[typing.Optional[str]] = Field(None, alias='fxRateID')

    billing_address1: typing.Optional[typing.Optional[str]] = Field(None, alias='billingAddress1')

    billing_address2: typing.Optional[typing.Optional[str]] = Field(None, alias='billingAddress2')

    billing_address3: typing.Optional[typing.Optional[str]] = Field(None, alias='billingAddress3')

    billing_city: typing.Optional[typing.Optional[str]] = Field(None, alias='billingCity')

    billing_state: typing.Optional[typing.Optional[str]] = Field(None, alias='billingState')

    billing_postal_code: typing.Optional[typing.Optional[str]] = Field(None, alias='billingPostalCode')

    billing_country_code: typing.Optional[typing.Optional[str]] = Field(None, alias='billingCountryCode')

    payment_expiry: typing.Optional[typing.Optional[str]] = Field(None, alias='paymentExpiry')

    card_no: typing.Optional[typing.Optional[str]] = Field(None, alias='cardNo')

    expiry_month: typing.Optional[typing.Optional[str]] = Field(None, alias='expiryMonth')

    expiry_year: typing.Optional[typing.Optional[str]] = Field(None, alias='expiryYear')

    pin: typing.Optional[typing.Optional[str]] = Field(None, alias='pin')

    loyalty_points: typing.Optional[typing.Optional[typing.List[LoyaltyDetails]]] = Field(None, alias='loyaltyPoints')

    customer_note: typing.Optional[typing.Optional[str]] = Field(None, alias='customerNote')

    user_agent: typing.Optional[typing.Optional[str]] = Field(None, alias='userAgent')
    class Config:
        arbitrary_types_allowed = True
