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


class MerchantValidationApplePay(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "paymentToken",
        }
        
        class properties:
            paymentToken = schemas.StrSchema
            
            
            class validationUrl(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'validationUrl':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class locale(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'locale':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            clientID = schemas.UUIDSchema
        
            @staticmethod
            def browserDetails() -> typing.Type['BrowserDetails']:
                return BrowserDetails
            __annotations__ = {
                "paymentToken": paymentToken,
                "validationUrl": validationUrl,
                "locale": locale,
                "clientID": clientID,
                "browserDetails": browserDetails,
            }
    
    paymentToken: MetaOapg.properties.paymentToken
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["paymentToken"]) -> MetaOapg.properties.paymentToken: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["validationUrl"]) -> MetaOapg.properties.validationUrl: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["locale"]) -> MetaOapg.properties.locale: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["clientID"]) -> MetaOapg.properties.clientID: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["browserDetails"]) -> 'BrowserDetails': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["paymentToken", "validationUrl", "locale", "clientID", "browserDetails", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["paymentToken"]) -> MetaOapg.properties.paymentToken: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["validationUrl"]) -> typing.Union[MetaOapg.properties.validationUrl, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["locale"]) -> typing.Union[MetaOapg.properties.locale, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["clientID"]) -> typing.Union[MetaOapg.properties.clientID, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["browserDetails"]) -> typing.Union['BrowserDetails', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["paymentToken", "validationUrl", "locale", "clientID", "browserDetails", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        paymentToken: typing.Union[MetaOapg.properties.paymentToken, str, ],
        validationUrl: typing.Union[MetaOapg.properties.validationUrl, None, str, schemas.Unset] = schemas.unset,
        locale: typing.Union[MetaOapg.properties.locale, None, str, schemas.Unset] = schemas.unset,
        clientID: typing.Union[MetaOapg.properties.clientID, str, uuid.UUID, schemas.Unset] = schemas.unset,
        browserDetails: typing.Union['BrowserDetails', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'MerchantValidationApplePay':
        return super().__new__(
            cls,
            *args,
            paymentToken=paymentToken,
            validationUrl=validationUrl,
            locale=locale,
            clientID=clientID,
            browserDetails=browserDetails,
            _configuration=_configuration,
            **kwargs,
        )

from 2c2p_python_sdk.model.browser_details import BrowserDetails
