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


class PaymentInitializationResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def initialization() -> typing.Type['PaymentInitialization']:
                return PaymentInitialization
            
            
            class respCode(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'respCode':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class respDesc(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'respDesc':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "initialization": initialization,
                "respCode": respCode,
                "respDesc": respDesc,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["initialization"]) -> 'PaymentInitialization': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["respCode"]) -> MetaOapg.properties.respCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["respDesc"]) -> MetaOapg.properties.respDesc: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["initialization", "respCode", "respDesc", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["initialization"]) -> typing.Union['PaymentInitialization', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["respCode"]) -> typing.Union[MetaOapg.properties.respCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["respDesc"]) -> typing.Union[MetaOapg.properties.respDesc, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["initialization", "respCode", "respDesc", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        initialization: typing.Union['PaymentInitialization', schemas.Unset] = schemas.unset,
        respCode: typing.Union[MetaOapg.properties.respCode, None, str, schemas.Unset] = schemas.unset,
        respDesc: typing.Union[MetaOapg.properties.respDesc, None, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PaymentInitializationResponse':
        return super().__new__(
            cls,
            *args,
            initialization=initialization,
            respCode=respCode,
            respDesc=respDesc,
            _configuration=_configuration,
            **kwargs,
        )

from 2c2p_python_sdk.model.payment_initialization import PaymentInitialization