# coding: utf-8

"""
    PGW Payment API 4.3

    Rest API for PGW payment purpose - LATEST

    The version of the OpenAPI document: 4.3
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from 2c2p_python_sdk import schemas  # noqa: F401


class MerchantConfiguration(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def payment() -> typing.Type['MerchantConfigurationPayment']:
                return MerchantConfigurationPayment
        
            @staticmethod
            def notification() -> typing.Type['MerchantConfigurationNotification']:
                return MerchantConfigurationNotification
            __annotations__ = {
                "payment": payment,
                "notification": notification,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payment"]) -> 'MerchantConfigurationPayment': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["notification"]) -> 'MerchantConfigurationNotification': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["payment", "notification", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payment"]) -> typing.Union['MerchantConfigurationPayment', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["notification"]) -> typing.Union['MerchantConfigurationNotification', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["payment", "notification", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        payment: typing.Union['MerchantConfigurationPayment', schemas.Unset] = schemas.unset,
        notification: typing.Union['MerchantConfigurationNotification', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'MerchantConfiguration':
        return super().__new__(
            cls,
            *args,
            payment=payment,
            notification=notification,
            _configuration=_configuration,
            **kwargs,
        )

from 2c2p_python_sdk.model.merchant_configuration_notification import MerchantConfigurationNotification
from 2c2p_python_sdk.model.merchant_configuration_payment import MerchantConfigurationPayment
