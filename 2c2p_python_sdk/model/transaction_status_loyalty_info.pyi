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


class TransactionStatusLoyaltyInfo(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            
            
            class paymentScheme(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'paymentScheme':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            redeemAmount = schemas.Float64Schema
            
            
            class rewards(
                schemas.ListBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneTupleMixin
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['TransactionStatusRewards']:
                        return TransactionStatusRewards
            
            
                def __new__(
                    cls,
                    *args: typing.Union[list, tuple, None, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'rewards':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "paymentScheme": paymentScheme,
                "redeemAmount": redeemAmount,
                "rewards": rewards,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["paymentScheme"]) -> MetaOapg.properties.paymentScheme: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["redeemAmount"]) -> MetaOapg.properties.redeemAmount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rewards"]) -> MetaOapg.properties.rewards: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["paymentScheme", "redeemAmount", "rewards", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["paymentScheme"]) -> typing.Union[MetaOapg.properties.paymentScheme, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["redeemAmount"]) -> typing.Union[MetaOapg.properties.redeemAmount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rewards"]) -> typing.Union[MetaOapg.properties.rewards, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["paymentScheme", "redeemAmount", "rewards", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        paymentScheme: typing.Union[MetaOapg.properties.paymentScheme, None, str, schemas.Unset] = schemas.unset,
        redeemAmount: typing.Union[MetaOapg.properties.redeemAmount, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        rewards: typing.Union[MetaOapg.properties.rewards, list, tuple, None, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TransactionStatusLoyaltyInfo':
        return super().__new__(
            cls,
            *args,
            paymentScheme=paymentScheme,
            redeemAmount=redeemAmount,
            rewards=rewards,
            _configuration=_configuration,
            **kwargs,
        )

from 2c2p_python_sdk.model.transaction_status_rewards import TransactionStatusRewards
