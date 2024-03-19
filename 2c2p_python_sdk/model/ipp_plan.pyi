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


class IppPlan(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            sequenceNo = schemas.Int32Schema
            period = schemas.Int32Schema
            
            
            class interestType(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'interestType':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            interestRate = schemas.Float64Schema
            monthlyAmount = schemas.Float64Schema
            monthlyInterest = schemas.Float64Schema
            
            
            class currencyCode(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'currencyCode':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class label(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'label':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class terms(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'terms':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class payLaterPeriod(
                schemas.Int32Base,
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                class MetaOapg:
                    format = 'int32'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'payLaterPeriod':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "sequenceNo": sequenceNo,
                "period": period,
                "interestType": interestType,
                "interestRate": interestRate,
                "monthlyAmount": monthlyAmount,
                "monthlyInterest": monthlyInterest,
                "currencyCode": currencyCode,
                "label": label,
                "terms": terms,
                "payLaterPeriod": payLaterPeriod,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sequenceNo"]) -> MetaOapg.properties.sequenceNo: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["period"]) -> MetaOapg.properties.period: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["interestType"]) -> MetaOapg.properties.interestType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["interestRate"]) -> MetaOapg.properties.interestRate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["monthlyAmount"]) -> MetaOapg.properties.monthlyAmount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["monthlyInterest"]) -> MetaOapg.properties.monthlyInterest: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currencyCode"]) -> MetaOapg.properties.currencyCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["label"]) -> MetaOapg.properties.label: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["terms"]) -> MetaOapg.properties.terms: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payLaterPeriod"]) -> MetaOapg.properties.payLaterPeriod: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["sequenceNo", "period", "interestType", "interestRate", "monthlyAmount", "monthlyInterest", "currencyCode", "label", "terms", "payLaterPeriod", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sequenceNo"]) -> typing.Union[MetaOapg.properties.sequenceNo, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["period"]) -> typing.Union[MetaOapg.properties.period, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["interestType"]) -> typing.Union[MetaOapg.properties.interestType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["interestRate"]) -> typing.Union[MetaOapg.properties.interestRate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["monthlyAmount"]) -> typing.Union[MetaOapg.properties.monthlyAmount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["monthlyInterest"]) -> typing.Union[MetaOapg.properties.monthlyInterest, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currencyCode"]) -> typing.Union[MetaOapg.properties.currencyCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["label"]) -> typing.Union[MetaOapg.properties.label, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["terms"]) -> typing.Union[MetaOapg.properties.terms, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payLaterPeriod"]) -> typing.Union[MetaOapg.properties.payLaterPeriod, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["sequenceNo", "period", "interestType", "interestRate", "monthlyAmount", "monthlyInterest", "currencyCode", "label", "terms", "payLaterPeriod", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        sequenceNo: typing.Union[MetaOapg.properties.sequenceNo, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        period: typing.Union[MetaOapg.properties.period, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        interestType: typing.Union[MetaOapg.properties.interestType, None, str, schemas.Unset] = schemas.unset,
        interestRate: typing.Union[MetaOapg.properties.interestRate, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        monthlyAmount: typing.Union[MetaOapg.properties.monthlyAmount, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        monthlyInterest: typing.Union[MetaOapg.properties.monthlyInterest, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        currencyCode: typing.Union[MetaOapg.properties.currencyCode, None, str, schemas.Unset] = schemas.unset,
        label: typing.Union[MetaOapg.properties.label, None, str, schemas.Unset] = schemas.unset,
        terms: typing.Union[MetaOapg.properties.terms, None, str, schemas.Unset] = schemas.unset,
        payLaterPeriod: typing.Union[MetaOapg.properties.payLaterPeriod, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'IppPlan':
        return super().__new__(
            cls,
            *args,
            sequenceNo=sequenceNo,
            period=period,
            interestType=interestType,
            interestRate=interestRate,
            monthlyAmount=monthlyAmount,
            monthlyInterest=monthlyInterest,
            currencyCode=currencyCode,
            label=label,
            terms=terms,
            payLaterPeriod=payLaterPeriod,
            _configuration=_configuration,
            **kwargs,
        )
