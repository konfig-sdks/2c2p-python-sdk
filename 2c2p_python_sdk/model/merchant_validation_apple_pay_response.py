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


class MerchantValidationApplePayResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            epochTimestamp = schemas.Int64Schema
            expiresAt = schemas.Int64Schema
            
            
            class merchantSessionIdentifier(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'merchantSessionIdentifier':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class nonce(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'nonce':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class merchantIdentifier(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'merchantIdentifier':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class domainName(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'domainName':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class displayName(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'displayName':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class signature(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'signature':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class operationalAnalyticsIdentifier(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'operationalAnalyticsIdentifier':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            retries = schemas.Int32Schema
            
            
            class pspId(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'pspId':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
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
                "epochTimestamp": epochTimestamp,
                "expiresAt": expiresAt,
                "merchantSessionIdentifier": merchantSessionIdentifier,
                "nonce": nonce,
                "merchantIdentifier": merchantIdentifier,
                "domainName": domainName,
                "displayName": displayName,
                "signature": signature,
                "operationalAnalyticsIdentifier": operationalAnalyticsIdentifier,
                "retries": retries,
                "pspId": pspId,
                "respCode": respCode,
                "respDesc": respDesc,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["epochTimestamp"]) -> MetaOapg.properties.epochTimestamp: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expiresAt"]) -> MetaOapg.properties.expiresAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["merchantSessionIdentifier"]) -> MetaOapg.properties.merchantSessionIdentifier: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nonce"]) -> MetaOapg.properties.nonce: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["merchantIdentifier"]) -> MetaOapg.properties.merchantIdentifier: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["domainName"]) -> MetaOapg.properties.domainName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["displayName"]) -> MetaOapg.properties.displayName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["signature"]) -> MetaOapg.properties.signature: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["operationalAnalyticsIdentifier"]) -> MetaOapg.properties.operationalAnalyticsIdentifier: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["retries"]) -> MetaOapg.properties.retries: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pspId"]) -> MetaOapg.properties.pspId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["respCode"]) -> MetaOapg.properties.respCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["respDesc"]) -> MetaOapg.properties.respDesc: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["epochTimestamp", "expiresAt", "merchantSessionIdentifier", "nonce", "merchantIdentifier", "domainName", "displayName", "signature", "operationalAnalyticsIdentifier", "retries", "pspId", "respCode", "respDesc", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["epochTimestamp"]) -> typing.Union[MetaOapg.properties.epochTimestamp, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expiresAt"]) -> typing.Union[MetaOapg.properties.expiresAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["merchantSessionIdentifier"]) -> typing.Union[MetaOapg.properties.merchantSessionIdentifier, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nonce"]) -> typing.Union[MetaOapg.properties.nonce, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["merchantIdentifier"]) -> typing.Union[MetaOapg.properties.merchantIdentifier, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["domainName"]) -> typing.Union[MetaOapg.properties.domainName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["displayName"]) -> typing.Union[MetaOapg.properties.displayName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["signature"]) -> typing.Union[MetaOapg.properties.signature, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["operationalAnalyticsIdentifier"]) -> typing.Union[MetaOapg.properties.operationalAnalyticsIdentifier, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["retries"]) -> typing.Union[MetaOapg.properties.retries, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pspId"]) -> typing.Union[MetaOapg.properties.pspId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["respCode"]) -> typing.Union[MetaOapg.properties.respCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["respDesc"]) -> typing.Union[MetaOapg.properties.respDesc, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["epochTimestamp", "expiresAt", "merchantSessionIdentifier", "nonce", "merchantIdentifier", "domainName", "displayName", "signature", "operationalAnalyticsIdentifier", "retries", "pspId", "respCode", "respDesc", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        epochTimestamp: typing.Union[MetaOapg.properties.epochTimestamp, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        expiresAt: typing.Union[MetaOapg.properties.expiresAt, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        merchantSessionIdentifier: typing.Union[MetaOapg.properties.merchantSessionIdentifier, None, str, schemas.Unset] = schemas.unset,
        nonce: typing.Union[MetaOapg.properties.nonce, None, str, schemas.Unset] = schemas.unset,
        merchantIdentifier: typing.Union[MetaOapg.properties.merchantIdentifier, None, str, schemas.Unset] = schemas.unset,
        domainName: typing.Union[MetaOapg.properties.domainName, None, str, schemas.Unset] = schemas.unset,
        displayName: typing.Union[MetaOapg.properties.displayName, None, str, schemas.Unset] = schemas.unset,
        signature: typing.Union[MetaOapg.properties.signature, None, str, schemas.Unset] = schemas.unset,
        operationalAnalyticsIdentifier: typing.Union[MetaOapg.properties.operationalAnalyticsIdentifier, None, str, schemas.Unset] = schemas.unset,
        retries: typing.Union[MetaOapg.properties.retries, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        pspId: typing.Union[MetaOapg.properties.pspId, None, str, schemas.Unset] = schemas.unset,
        respCode: typing.Union[MetaOapg.properties.respCode, None, str, schemas.Unset] = schemas.unset,
        respDesc: typing.Union[MetaOapg.properties.respDesc, None, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'MerchantValidationApplePayResponse':
        return super().__new__(
            cls,
            *args,
            epochTimestamp=epochTimestamp,
            expiresAt=expiresAt,
            merchantSessionIdentifier=merchantSessionIdentifier,
            nonce=nonce,
            merchantIdentifier=merchantIdentifier,
            domainName=domainName,
            displayName=displayName,
            signature=signature,
            operationalAnalyticsIdentifier=operationalAnalyticsIdentifier,
            retries=retries,
            pspId=pspId,
            respCode=respCode,
            respDesc=respDesc,
            _configuration=_configuration,
            **kwargs,
        )
