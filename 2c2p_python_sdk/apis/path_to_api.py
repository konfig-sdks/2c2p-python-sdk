import typing_extensions

from 2c2p_python_sdk.paths import PathValues
from 2c2p_python_sdk.apis.paths.payment_4_3_applepay_merchantvalidation import Payment43ApplepayMerchantvalidation
from 2c2p_python_sdk.apis.paths.payment_4_3_cache_cleancache import Payment43CacheCleancache
from 2c2p_python_sdk.apis.paths.payment_4_3_canceltransaction import Payment43Canceltransaction
from 2c2p_python_sdk.apis.paths.payment_4_3_cardinstallmentplaninfo import Payment43Cardinstallmentplaninfo
from 2c2p_python_sdk.apis.paths.payment_4_3_cardtokeninfo import Payment43Cardtokeninfo
from 2c2p_python_sdk.apis.paths.payment_4_3_exchangerate import Payment43Exchangerate
from 2c2p_python_sdk.apis.paths.payment_4_3_exchangerate_secure import Payment43ExchangerateSecure
from 2c2p_python_sdk.apis.paths.payment_4_3_exchangerate_apmmccexchangerate import Payment43ExchangerateApmmccexchangerate
from 2c2p_python_sdk.apis.paths.payment_4_3_initialization import Payment43Initialization
from 2c2p_python_sdk.apis.paths.payment_4_3_loyaltypointinfo import Payment43Loyaltypointinfo
from 2c2p_python_sdk.apis.paths.payment_4_3_payment import Payment43Payment
from 2c2p_python_sdk.apis.paths.payment_4_3_paymentinquiry import Payment43Paymentinquiry
from 2c2p_python_sdk.apis.paths.payment_4_3_paymentinstruction import Payment43Paymentinstruction
from 2c2p_python_sdk.apis.paths.payment_4_3_paymentnotification import Payment43Paymentnotification
from 2c2p_python_sdk.apis.paths.payment_4_3_paymentoption import Payment43Paymentoption
from 2c2p_python_sdk.apis.paths.payment_4_3_paymentoptiondetails import Payment43Paymentoptiondetails
from 2c2p_python_sdk.apis.paths.payment_4_3_paymentsimulate import Payment43Paymentsimulate
from 2c2p_python_sdk.apis.paths.payment_4_3_paymenttoken import Payment43Paymenttoken
from 2c2p_python_sdk.apis.paths.payment_4_3_redirectbackend import Payment43Redirectbackend
from 2c2p_python_sdk.apis.paths.payment_4_3_redirectfrontend import Payment43Redirectfrontend
from 2c2p_python_sdk.apis.paths.payment_4_3_transactionstatus import Payment43Transactionstatus
from 2c2p_python_sdk.apis.paths.payment_4_3_userpreference import Payment43Userpreference

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.PAYMENT_4_3_APPLEPAY_MERCHANTVALIDATION: Payment43ApplepayMerchantvalidation,
        PathValues.PAYMENT_4_3_CACHE_CLEANCACHE: Payment43CacheCleancache,
        PathValues.PAYMENT_4_3_CANCELTRANSACTION: Payment43Canceltransaction,
        PathValues.PAYMENT_4_3_CARDINSTALLMENTPLANINFO: Payment43Cardinstallmentplaninfo,
        PathValues.PAYMENT_4_3_CARDTOKENINFO: Payment43Cardtokeninfo,
        PathValues.PAYMENT_4_3_EXCHANGERATE: Payment43Exchangerate,
        PathValues.PAYMENT_4_3_EXCHANGERATE_SECURE: Payment43ExchangerateSecure,
        PathValues.PAYMENT_4_3_EXCHANGERATE_APMMCCEXCHANGERATE: Payment43ExchangerateApmmccexchangerate,
        PathValues.PAYMENT_4_3_INITIALIZATION: Payment43Initialization,
        PathValues.PAYMENT_4_3_LOYALTYPOINTINFO: Payment43Loyaltypointinfo,
        PathValues.PAYMENT_4_3_PAYMENT: Payment43Payment,
        PathValues.PAYMENT_4_3_PAYMENTINQUIRY: Payment43Paymentinquiry,
        PathValues.PAYMENT_4_3_PAYMENTINSTRUCTION: Payment43Paymentinstruction,
        PathValues.PAYMENT_4_3_PAYMENTNOTIFICATION: Payment43Paymentnotification,
        PathValues.PAYMENT_4_3_PAYMENTOPTION: Payment43Paymentoption,
        PathValues.PAYMENT_4_3_PAYMENTOPTIONDETAILS: Payment43Paymentoptiondetails,
        PathValues.PAYMENT_4_3_PAYMENTSIMULATE: Payment43Paymentsimulate,
        PathValues.PAYMENT_4_3_PAYMENTTOKEN: Payment43Paymenttoken,
        PathValues.PAYMENT_4_3_REDIRECTBACKEND: Payment43Redirectbackend,
        PathValues.PAYMENT_4_3_REDIRECTFRONTEND: Payment43Redirectfrontend,
        PathValues.PAYMENT_4_3_TRANSACTIONSTATUS: Payment43Transactionstatus,
        PathValues.PAYMENT_4_3_USERPREFERENCE: Payment43Userpreference,
    }
)

path_to_api = PathToApi(
    {
        PathValues.PAYMENT_4_3_APPLEPAY_MERCHANTVALIDATION: Payment43ApplepayMerchantvalidation,
        PathValues.PAYMENT_4_3_CACHE_CLEANCACHE: Payment43CacheCleancache,
        PathValues.PAYMENT_4_3_CANCELTRANSACTION: Payment43Canceltransaction,
        PathValues.PAYMENT_4_3_CARDINSTALLMENTPLANINFO: Payment43Cardinstallmentplaninfo,
        PathValues.PAYMENT_4_3_CARDTOKENINFO: Payment43Cardtokeninfo,
        PathValues.PAYMENT_4_3_EXCHANGERATE: Payment43Exchangerate,
        PathValues.PAYMENT_4_3_EXCHANGERATE_SECURE: Payment43ExchangerateSecure,
        PathValues.PAYMENT_4_3_EXCHANGERATE_APMMCCEXCHANGERATE: Payment43ExchangerateApmmccexchangerate,
        PathValues.PAYMENT_4_3_INITIALIZATION: Payment43Initialization,
        PathValues.PAYMENT_4_3_LOYALTYPOINTINFO: Payment43Loyaltypointinfo,
        PathValues.PAYMENT_4_3_PAYMENT: Payment43Payment,
        PathValues.PAYMENT_4_3_PAYMENTINQUIRY: Payment43Paymentinquiry,
        PathValues.PAYMENT_4_3_PAYMENTINSTRUCTION: Payment43Paymentinstruction,
        PathValues.PAYMENT_4_3_PAYMENTNOTIFICATION: Payment43Paymentnotification,
        PathValues.PAYMENT_4_3_PAYMENTOPTION: Payment43Paymentoption,
        PathValues.PAYMENT_4_3_PAYMENTOPTIONDETAILS: Payment43Paymentoptiondetails,
        PathValues.PAYMENT_4_3_PAYMENTSIMULATE: Payment43Paymentsimulate,
        PathValues.PAYMENT_4_3_PAYMENTTOKEN: Payment43Paymenttoken,
        PathValues.PAYMENT_4_3_REDIRECTBACKEND: Payment43Redirectbackend,
        PathValues.PAYMENT_4_3_REDIRECTFRONTEND: Payment43Redirectfrontend,
        PathValues.PAYMENT_4_3_TRANSACTIONSTATUS: Payment43Transactionstatus,
        PathValues.PAYMENT_4_3_USERPREFERENCE: Payment43Userpreference,
    }
)
