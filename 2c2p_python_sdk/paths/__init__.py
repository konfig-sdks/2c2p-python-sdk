# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from 2c2p_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    PAYMENT_4_3_APPLEPAY_MERCHANTVALIDATION = "/payment/4.3/applepay/merchantvalidation"
    PAYMENT_4_3_CACHE_CLEANCACHE = "/payment/4.3/cache/cleancache"
    PAYMENT_4_3_CANCELTRANSACTION = "/payment/4.3/canceltransaction"
    PAYMENT_4_3_CARDINSTALLMENTPLANINFO = "/payment/4.3/cardinstallmentplaninfo"
    PAYMENT_4_3_CARDTOKENINFO = "/payment/4.3/cardtokeninfo"
    PAYMENT_4_3_EXCHANGERATE = "/payment/4.3/exchangerate"
    PAYMENT_4_3_EXCHANGERATE_SECURE = "/payment/4.3/exchangerate/secure"
    PAYMENT_4_3_EXCHANGERATE_APMMCCEXCHANGERATE = "/payment/4.3/exchangerate/apmmccexchangerate"
    PAYMENT_4_3_INITIALIZATION = "/payment/4.3/initialization"
    PAYMENT_4_3_LOYALTYPOINTINFO = "/payment/4.3/loyaltypointinfo"
    PAYMENT_4_3_PAYMENT = "/payment/4.3/payment"
    PAYMENT_4_3_PAYMENTINQUIRY = "/payment/4.3/paymentinquiry"
    PAYMENT_4_3_PAYMENTINSTRUCTION = "/payment/4.3/paymentinstruction"
    PAYMENT_4_3_PAYMENTNOTIFICATION = "/payment/4.3/paymentnotification"
    PAYMENT_4_3_PAYMENTOPTION = "/payment/4.3/paymentoption"
    PAYMENT_4_3_PAYMENTOPTIONDETAILS = "/payment/4.3/paymentoptiondetails"
    PAYMENT_4_3_PAYMENTSIMULATE = "/payment/4.3/paymentsimulate"
    PAYMENT_4_3_PAYMENTTOKEN = "/payment/4.3/paymenttoken"
    PAYMENT_4_3_REDIRECTBACKEND = "/payment/4.3/redirectbackend"
    PAYMENT_4_3_REDIRECTFRONTEND = "/payment/4.3/redirectfrontend"
    PAYMENT_4_3_TRANSACTIONSTATUS = "/payment/4.3/transactionstatus"
    PAYMENT_4_3_USERPREFERENCE = "/payment/4.3/userpreference"
