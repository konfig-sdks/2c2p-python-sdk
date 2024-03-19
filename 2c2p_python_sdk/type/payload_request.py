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


class RequiredPayloadRequest(TypedDict):
    pass

class OptionalPayloadRequest(TypedDict, total=False):
    payload: typing.Optional[str]

class PayloadRequest(RequiredPayloadRequest, OptionalPayloadRequest):
    pass
