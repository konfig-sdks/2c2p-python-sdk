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


class PaymentParamsDataRequestV43(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            accountTokenization = schemas.BoolSchema
            
            
            class customerToken(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'customerToken':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class name(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'name':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class email(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'email':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class mobileNo(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'mobileNo':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class accountNo(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'accountNo':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class securePayToken(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'securePayToken':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class cardBank(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'cardBank':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class cardCountry(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'cardCountry':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            installmentPeriod = schemas.Int32Schema
            
            
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
            
            
            class securityCode(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'securityCode':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class qrType(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'qrType':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class fxRateID(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'fxRateID':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class billingAddress1(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'billingAddress1':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class billingAddress2(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'billingAddress2':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class billingAddress3(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'billingAddress3':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class billingCity(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'billingCity':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class billingState(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'billingState':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class billingPostalCode(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'billingPostalCode':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class billingCountryCode(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'billingCountryCode':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class paymentExpiry(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'paymentExpiry':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class cardNo(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'cardNo':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class expiryMonth(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'expiryMonth':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class expiryYear(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'expiryYear':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class pin(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'pin':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class loyaltyPoints(
                schemas.ListBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneTupleMixin
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['LoyaltyDetails']:
                        return LoyaltyDetails
            
            
                def __new__(
                    cls,
                    *args: typing.Union[list, tuple, None, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'loyaltyPoints':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class customerNote(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'customerNote':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class userAgent(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'userAgent':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "accountTokenization": accountTokenization,
                "customerToken": customerToken,
                "name": name,
                "email": email,
                "mobileNo": mobileNo,
                "accountNo": accountNo,
                "securePayToken": securePayToken,
                "cardBank": cardBank,
                "cardCountry": cardCountry,
                "installmentPeriod": installmentPeriod,
                "payLaterPeriod": payLaterPeriod,
                "interestType": interestType,
                "securityCode": securityCode,
                "qrType": qrType,
                "fxRateID": fxRateID,
                "billingAddress1": billingAddress1,
                "billingAddress2": billingAddress2,
                "billingAddress3": billingAddress3,
                "billingCity": billingCity,
                "billingState": billingState,
                "billingPostalCode": billingPostalCode,
                "billingCountryCode": billingCountryCode,
                "paymentExpiry": paymentExpiry,
                "cardNo": cardNo,
                "expiryMonth": expiryMonth,
                "expiryYear": expiryYear,
                "pin": pin,
                "loyaltyPoints": loyaltyPoints,
                "customerNote": customerNote,
                "userAgent": userAgent,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accountTokenization"]) -> MetaOapg.properties.accountTokenization: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customerToken"]) -> MetaOapg.properties.customerToken: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mobileNo"]) -> MetaOapg.properties.mobileNo: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accountNo"]) -> MetaOapg.properties.accountNo: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["securePayToken"]) -> MetaOapg.properties.securePayToken: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cardBank"]) -> MetaOapg.properties.cardBank: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cardCountry"]) -> MetaOapg.properties.cardCountry: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["installmentPeriod"]) -> MetaOapg.properties.installmentPeriod: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payLaterPeriod"]) -> MetaOapg.properties.payLaterPeriod: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["interestType"]) -> MetaOapg.properties.interestType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["securityCode"]) -> MetaOapg.properties.securityCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["qrType"]) -> MetaOapg.properties.qrType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fxRateID"]) -> MetaOapg.properties.fxRateID: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["billingAddress1"]) -> MetaOapg.properties.billingAddress1: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["billingAddress2"]) -> MetaOapg.properties.billingAddress2: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["billingAddress3"]) -> MetaOapg.properties.billingAddress3: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["billingCity"]) -> MetaOapg.properties.billingCity: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["billingState"]) -> MetaOapg.properties.billingState: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["billingPostalCode"]) -> MetaOapg.properties.billingPostalCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["billingCountryCode"]) -> MetaOapg.properties.billingCountryCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["paymentExpiry"]) -> MetaOapg.properties.paymentExpiry: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cardNo"]) -> MetaOapg.properties.cardNo: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expiryMonth"]) -> MetaOapg.properties.expiryMonth: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expiryYear"]) -> MetaOapg.properties.expiryYear: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pin"]) -> MetaOapg.properties.pin: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["loyaltyPoints"]) -> MetaOapg.properties.loyaltyPoints: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customerNote"]) -> MetaOapg.properties.customerNote: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["userAgent"]) -> MetaOapg.properties.userAgent: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["accountTokenization", "customerToken", "name", "email", "mobileNo", "accountNo", "securePayToken", "cardBank", "cardCountry", "installmentPeriod", "payLaterPeriod", "interestType", "securityCode", "qrType", "fxRateID", "billingAddress1", "billingAddress2", "billingAddress3", "billingCity", "billingState", "billingPostalCode", "billingCountryCode", "paymentExpiry", "cardNo", "expiryMonth", "expiryYear", "pin", "loyaltyPoints", "customerNote", "userAgent", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accountTokenization"]) -> typing.Union[MetaOapg.properties.accountTokenization, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customerToken"]) -> typing.Union[MetaOapg.properties.customerToken, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> typing.Union[MetaOapg.properties.email, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mobileNo"]) -> typing.Union[MetaOapg.properties.mobileNo, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accountNo"]) -> typing.Union[MetaOapg.properties.accountNo, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["securePayToken"]) -> typing.Union[MetaOapg.properties.securePayToken, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cardBank"]) -> typing.Union[MetaOapg.properties.cardBank, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cardCountry"]) -> typing.Union[MetaOapg.properties.cardCountry, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["installmentPeriod"]) -> typing.Union[MetaOapg.properties.installmentPeriod, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payLaterPeriod"]) -> typing.Union[MetaOapg.properties.payLaterPeriod, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["interestType"]) -> typing.Union[MetaOapg.properties.interestType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["securityCode"]) -> typing.Union[MetaOapg.properties.securityCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["qrType"]) -> typing.Union[MetaOapg.properties.qrType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fxRateID"]) -> typing.Union[MetaOapg.properties.fxRateID, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["billingAddress1"]) -> typing.Union[MetaOapg.properties.billingAddress1, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["billingAddress2"]) -> typing.Union[MetaOapg.properties.billingAddress2, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["billingAddress3"]) -> typing.Union[MetaOapg.properties.billingAddress3, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["billingCity"]) -> typing.Union[MetaOapg.properties.billingCity, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["billingState"]) -> typing.Union[MetaOapg.properties.billingState, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["billingPostalCode"]) -> typing.Union[MetaOapg.properties.billingPostalCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["billingCountryCode"]) -> typing.Union[MetaOapg.properties.billingCountryCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["paymentExpiry"]) -> typing.Union[MetaOapg.properties.paymentExpiry, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cardNo"]) -> typing.Union[MetaOapg.properties.cardNo, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expiryMonth"]) -> typing.Union[MetaOapg.properties.expiryMonth, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expiryYear"]) -> typing.Union[MetaOapg.properties.expiryYear, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pin"]) -> typing.Union[MetaOapg.properties.pin, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["loyaltyPoints"]) -> typing.Union[MetaOapg.properties.loyaltyPoints, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customerNote"]) -> typing.Union[MetaOapg.properties.customerNote, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["userAgent"]) -> typing.Union[MetaOapg.properties.userAgent, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["accountTokenization", "customerToken", "name", "email", "mobileNo", "accountNo", "securePayToken", "cardBank", "cardCountry", "installmentPeriod", "payLaterPeriod", "interestType", "securityCode", "qrType", "fxRateID", "billingAddress1", "billingAddress2", "billingAddress3", "billingCity", "billingState", "billingPostalCode", "billingCountryCode", "paymentExpiry", "cardNo", "expiryMonth", "expiryYear", "pin", "loyaltyPoints", "customerNote", "userAgent", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        accountTokenization: typing.Union[MetaOapg.properties.accountTokenization, bool, schemas.Unset] = schemas.unset,
        customerToken: typing.Union[MetaOapg.properties.customerToken, None, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, None, str, schemas.Unset] = schemas.unset,
        email: typing.Union[MetaOapg.properties.email, None, str, schemas.Unset] = schemas.unset,
        mobileNo: typing.Union[MetaOapg.properties.mobileNo, None, str, schemas.Unset] = schemas.unset,
        accountNo: typing.Union[MetaOapg.properties.accountNo, None, str, schemas.Unset] = schemas.unset,
        securePayToken: typing.Union[MetaOapg.properties.securePayToken, None, str, schemas.Unset] = schemas.unset,
        cardBank: typing.Union[MetaOapg.properties.cardBank, None, str, schemas.Unset] = schemas.unset,
        cardCountry: typing.Union[MetaOapg.properties.cardCountry, None, str, schemas.Unset] = schemas.unset,
        installmentPeriod: typing.Union[MetaOapg.properties.installmentPeriod, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        payLaterPeriod: typing.Union[MetaOapg.properties.payLaterPeriod, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        interestType: typing.Union[MetaOapg.properties.interestType, None, str, schemas.Unset] = schemas.unset,
        securityCode: typing.Union[MetaOapg.properties.securityCode, None, str, schemas.Unset] = schemas.unset,
        qrType: typing.Union[MetaOapg.properties.qrType, None, str, schemas.Unset] = schemas.unset,
        fxRateID: typing.Union[MetaOapg.properties.fxRateID, None, str, schemas.Unset] = schemas.unset,
        billingAddress1: typing.Union[MetaOapg.properties.billingAddress1, None, str, schemas.Unset] = schemas.unset,
        billingAddress2: typing.Union[MetaOapg.properties.billingAddress2, None, str, schemas.Unset] = schemas.unset,
        billingAddress3: typing.Union[MetaOapg.properties.billingAddress3, None, str, schemas.Unset] = schemas.unset,
        billingCity: typing.Union[MetaOapg.properties.billingCity, None, str, schemas.Unset] = schemas.unset,
        billingState: typing.Union[MetaOapg.properties.billingState, None, str, schemas.Unset] = schemas.unset,
        billingPostalCode: typing.Union[MetaOapg.properties.billingPostalCode, None, str, schemas.Unset] = schemas.unset,
        billingCountryCode: typing.Union[MetaOapg.properties.billingCountryCode, None, str, schemas.Unset] = schemas.unset,
        paymentExpiry: typing.Union[MetaOapg.properties.paymentExpiry, None, str, schemas.Unset] = schemas.unset,
        cardNo: typing.Union[MetaOapg.properties.cardNo, None, str, schemas.Unset] = schemas.unset,
        expiryMonth: typing.Union[MetaOapg.properties.expiryMonth, None, str, schemas.Unset] = schemas.unset,
        expiryYear: typing.Union[MetaOapg.properties.expiryYear, None, str, schemas.Unset] = schemas.unset,
        pin: typing.Union[MetaOapg.properties.pin, None, str, schemas.Unset] = schemas.unset,
        loyaltyPoints: typing.Union[MetaOapg.properties.loyaltyPoints, list, tuple, None, schemas.Unset] = schemas.unset,
        customerNote: typing.Union[MetaOapg.properties.customerNote, None, str, schemas.Unset] = schemas.unset,
        userAgent: typing.Union[MetaOapg.properties.userAgent, None, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PaymentParamsDataRequestV43':
        return super().__new__(
            cls,
            *args,
            accountTokenization=accountTokenization,
            customerToken=customerToken,
            name=name,
            email=email,
            mobileNo=mobileNo,
            accountNo=accountNo,
            securePayToken=securePayToken,
            cardBank=cardBank,
            cardCountry=cardCountry,
            installmentPeriod=installmentPeriod,
            payLaterPeriod=payLaterPeriod,
            interestType=interestType,
            securityCode=securityCode,
            qrType=qrType,
            fxRateID=fxRateID,
            billingAddress1=billingAddress1,
            billingAddress2=billingAddress2,
            billingAddress3=billingAddress3,
            billingCity=billingCity,
            billingState=billingState,
            billingPostalCode=billingPostalCode,
            billingCountryCode=billingCountryCode,
            paymentExpiry=paymentExpiry,
            cardNo=cardNo,
            expiryMonth=expiryMonth,
            expiryYear=expiryYear,
            pin=pin,
            loyaltyPoints=loyaltyPoints,
            customerNote=customerNote,
            userAgent=userAgent,
            _configuration=_configuration,
            **kwargs,
        )

from 2c2p_python_sdk.model.loyalty_details import LoyaltyDetails
