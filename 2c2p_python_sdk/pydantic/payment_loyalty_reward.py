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


class PaymentLoyaltyReward(BaseModel):
    sequence_no: typing.Optional[int] = Field(None, alias='sequenceNo')

    id: typing.Optional[typing.Optional[str]] = Field(None, alias='id')

    currency_code: typing.Optional[typing.Optional[str]] = Field(None, alias='currencyCode')

    total_points: typing.Optional[typing.Union[int, float]] = Field(None, alias='totalPoints')

    label: typing.Optional[typing.Optional[str]] = Field(None, alias='label')

    point: typing.Optional[typing.Union[int, float]] = Field(None, alias='point')

    force_to_select_reward: typing.Optional[bool] = Field(None, alias='forceToSelectReward')

    name: typing.Optional[typing.Optional[str]] = Field(None, alias='name')

    type: typing.Optional[typing.Optional[str]] = Field(None, alias='type')

    amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='amount')

    quantity: typing.Optional[typing.Union[int, float]] = Field(None, alias='quantity')

    price: typing.Optional[typing.Union[int, float]] = Field(None, alias='price')
    class Config:
        arbitrary_types_allowed = True
