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


class PaymentOptionDetailsInfo(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            
            
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
            
            
            class promoUrl(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'promoUrl':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class plans(
                schemas.ListBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneTupleMixin
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['IppPlan']:
                        return IppPlan
            
            
                def __new__(
                    cls,
                    *args: typing.Union[list, tuple, None, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'plans':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class customData(
                schemas.ListBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneTupleMixin
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['PaymentOptionDetailsCustomData']:
                        return PaymentOptionDetailsCustomData
            
            
                def __new__(
                    cls,
                    *args: typing.Union[list, tuple, None, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'customData':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def provider() -> typing.Type['PaymentOptionDetailsInfoProvider']:
                return PaymentOptionDetailsInfoProvider
            
            
            class learnMoreUrl(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'learnMoreUrl':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            termsConsent = schemas.BoolSchema
            __annotations__ = {
                "terms": terms,
                "promoUrl": promoUrl,
                "plans": plans,
                "customData": customData,
                "provider": provider,
                "learnMoreUrl": learnMoreUrl,
                "termsConsent": termsConsent,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["terms"]) -> MetaOapg.properties.terms: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["promoUrl"]) -> MetaOapg.properties.promoUrl: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["plans"]) -> MetaOapg.properties.plans: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customData"]) -> MetaOapg.properties.customData: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["provider"]) -> 'PaymentOptionDetailsInfoProvider': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["learnMoreUrl"]) -> MetaOapg.properties.learnMoreUrl: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["termsConsent"]) -> MetaOapg.properties.termsConsent: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["terms", "promoUrl", "plans", "customData", "provider", "learnMoreUrl", "termsConsent", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["terms"]) -> typing.Union[MetaOapg.properties.terms, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["promoUrl"]) -> typing.Union[MetaOapg.properties.promoUrl, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["plans"]) -> typing.Union[MetaOapg.properties.plans, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customData"]) -> typing.Union[MetaOapg.properties.customData, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["provider"]) -> typing.Union['PaymentOptionDetailsInfoProvider', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["learnMoreUrl"]) -> typing.Union[MetaOapg.properties.learnMoreUrl, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["termsConsent"]) -> typing.Union[MetaOapg.properties.termsConsent, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["terms", "promoUrl", "plans", "customData", "provider", "learnMoreUrl", "termsConsent", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        terms: typing.Union[MetaOapg.properties.terms, None, str, schemas.Unset] = schemas.unset,
        promoUrl: typing.Union[MetaOapg.properties.promoUrl, None, str, schemas.Unset] = schemas.unset,
        plans: typing.Union[MetaOapg.properties.plans, list, tuple, None, schemas.Unset] = schemas.unset,
        customData: typing.Union[MetaOapg.properties.customData, list, tuple, None, schemas.Unset] = schemas.unset,
        provider: typing.Union['PaymentOptionDetailsInfoProvider', schemas.Unset] = schemas.unset,
        learnMoreUrl: typing.Union[MetaOapg.properties.learnMoreUrl, None, str, schemas.Unset] = schemas.unset,
        termsConsent: typing.Union[MetaOapg.properties.termsConsent, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PaymentOptionDetailsInfo':
        return super().__new__(
            cls,
            *args,
            terms=terms,
            promoUrl=promoUrl,
            plans=plans,
            customData=customData,
            provider=provider,
            learnMoreUrl=learnMoreUrl,
            termsConsent=termsConsent,
            _configuration=_configuration,
            **kwargs,
        )

from 2c2p_python_sdk.model.ipp_plan import IppPlan
from 2c2p_python_sdk.model.payment_option_details_custom_data import PaymentOptionDetailsCustomData
from 2c2p_python_sdk.model.payment_option_details_info_provider import PaymentOptionDetailsInfoProvider
