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


class PaymentOptionDetailsPaymentCode(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            
            
            class channelCode(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'channelCode':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class agentCode(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'agentCode':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class agentChannelCode(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'agentChannelCode':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "channelCode": channelCode,
                "agentCode": agentCode,
                "agentChannelCode": agentChannelCode,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["channelCode"]) -> MetaOapg.properties.channelCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["agentCode"]) -> MetaOapg.properties.agentCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["agentChannelCode"]) -> MetaOapg.properties.agentChannelCode: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["channelCode", "agentCode", "agentChannelCode", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["channelCode"]) -> typing.Union[MetaOapg.properties.channelCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["agentCode"]) -> typing.Union[MetaOapg.properties.agentCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["agentChannelCode"]) -> typing.Union[MetaOapg.properties.agentChannelCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["channelCode", "agentCode", "agentChannelCode", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        channelCode: typing.Union[MetaOapg.properties.channelCode, None, str, schemas.Unset] = schemas.unset,
        agentCode: typing.Union[MetaOapg.properties.agentCode, None, str, schemas.Unset] = schemas.unset,
        agentChannelCode: typing.Union[MetaOapg.properties.agentChannelCode, None, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PaymentOptionDetailsPaymentCode':
        return super().__new__(
            cls,
            *args,
            channelCode=channelCode,
            agentCode=agentCode,
            agentChannelCode=agentChannelCode,
            _configuration=_configuration,
            **kwargs,
        )
