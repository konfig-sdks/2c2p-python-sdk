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


class TransactionStatusPayment(BaseModel):
    description: typing.Optional[typing.Optional[str]] = Field(None, alias='description')

    code: typing.Optional[typing.Optional[str]] = Field(None, alias='code')

    auto_redirect: typing.Optional[bool] = Field(None, alias='autoRedirect')

    redirect_immediately: typing.Optional[bool] = Field(None, alias='redirectImmediately')

    auto_redirection_timer: typing.Optional[int] = Field(None, alias='autoRedirectionTimer')

    frontend_return_url: typing.Optional[typing.Optional[str]] = Field(None, alias='frontendReturnUrl')

    frontend_return_data: typing.Optional[typing.Optional[str]] = Field(None, alias='frontendReturnData')
    class Config:
        arbitrary_types_allowed = True
