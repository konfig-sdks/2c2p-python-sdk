<div align="center">

[![Visit 2c2p](./header.png)](https://2c2p.com&#x2F;)

# 2c2p<a id="2c2p"></a>

Rest API for PGW payment purpose - LATEST


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`twoctwop.apple_pay.validate_merchant`](#twoctwopapple_payvalidate_merchant)
  * [`twoctwop.cache.clean_cache`](#twoctwopcacheclean_cache)
  * [`twoctwop.cancel_transaction.post`](#twoctwopcancel_transactionpost)
  * [`twoctwop.card_installment_plan_info.create`](#twoctwopcard_installment_plan_infocreate)
  * [`twoctwop.card_token_info.get_card_token_info`](#twoctwopcard_token_infoget_card_token_info)
  * [`twoctwop.exchange_rate.apm_mcc`](#twoctwopexchange_rateapm_mcc)
  * [`twoctwop.exchange_rate.get_rate`](#twoctwopexchange_rateget_rate)
  * [`twoctwop.exchange_rate.request_endpoint`](#twoctwopexchange_raterequest_endpoint)
  * [`twoctwop.initialization.request_creation`](#twoctwopinitializationrequest_creation)
  * [`twoctwop.loyalty_point_info.post_loyalty_point_info`](#twoctwoployalty_point_infopost_loyalty_point_info)
  * [`twoctwop.payment.create_payment`](#twoctwoppaymentcreate_payment)
  * [`twoctwop.payment_inquiry.post_payment_details`](#twoctwoppayment_inquirypost_payment_details)
  * [`twoctwop.payment_instruction.submit_instruction`](#twoctwoppayment_instructionsubmit_instruction)
  * [`twoctwop.payment_notification.process_notification`](#twoctwoppayment_notificationprocess_notification)
  * [`twoctwop.payment_option.create_payment_option`](#twoctwoppayment_optioncreate_payment_option)
  * [`twoctwop.payment_option_details.post_option_details`](#twoctwoppayment_option_detailspost_option_details)
  * [`twoctwop.payment_simulate.execute_payment_simulation`](#twoctwoppayment_simulateexecute_payment_simulation)
  * [`twoctwop.payment_token.generate_token`](#twoctwoppayment_tokengenerate_token)
  * [`twoctwop.redirect_back_end.post_payment_redirect`](#twoctwopredirect_back_endpost_payment_redirect)
  * [`twoctwop.redirect_front_end.post_payment_redirect`](#twoctwopredirect_front_endpost_payment_redirect)
  * [`twoctwop.transaction_status.update_transaction_status`](#twoctwoptransaction_statusupdate_transaction_status)
  * [`twoctwop.user_preference.save_user_preference`](#twoctwopuser_preferencesave_user_preference)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=2C2P&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from 2c2p_python_sdk import TwoCTwoP, ApiException

twoctwop = TwoCTwoP(
)

try:
    validate_merchant_response = twoctwop.apple_pay.validate_merchant(
        payment_token="string_example",
        validation_url="string_example",
        locale="string_example",
        client_id="046b6c7f-0b8a-43b9-b35d-6489e6daee91",
        browser_details={
    },
    )
    print(validate_merchant_response)
except ApiException as e:
    print("Exception when calling ApplePayApi.validate_merchant: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python

import asyncio
from pprint import pprint
from 2c2p_python_sdk import TwoCTwoP, ApiException

twoctwop = TwoCTwoP(
)

async def main():
    try:
        validate_merchant_response = await twoctwop.apple_pay.avalidate_merchant(
            payment_token="string_example",
            validation_url="string_example",
            locale="string_example",
            client_id="046b6c7f-0b8a-43b9-b35d-6489e6daee91",
            browser_details={
    },
        )
        print(validate_merchant_response)
    except ApiException as e:
        print("Exception when calling ApplePayApi.validate_merchant: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)

asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from 2c2p_python_sdk import TwoCTwoP, ApiException

twoctwop = TwoCTwoP(
)

try:
    validate_merchant_response = twoctwop.apple_pay.raw.validate_merchant(
        payment_token="string_example",
        validation_url="string_example",
        locale="string_example",
        client_id="046b6c7f-0b8a-43b9-b35d-6489e6daee91",
        browser_details={
    },
    )
    pprint(validate_merchant_response.body)
    pprint(validate_merchant_response.body["epoch_timestamp"])
    pprint(validate_merchant_response.body["expires_at"])
    pprint(validate_merchant_response.body["merchant_session_identifier"])
    pprint(validate_merchant_response.body["nonce"])
    pprint(validate_merchant_response.body["merchant_identifier"])
    pprint(validate_merchant_response.body["domain_name"])
    pprint(validate_merchant_response.body["display_name"])
    pprint(validate_merchant_response.body["signature"])
    pprint(validate_merchant_response.body["operational_analytics_identifier"])
    pprint(validate_merchant_response.body["retries"])
    pprint(validate_merchant_response.body["psp_id"])
    pprint(validate_merchant_response.body["resp_code"])
    pprint(validate_merchant_response.body["resp_desc"])
    pprint(validate_merchant_response.headers)
    pprint(validate_merchant_response.status)
    pprint(validate_merchant_response.round_trip_time)
except ApiException as e:
    print("Exception when calling ApplePayApi.validate_merchant: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `twoctwop.apple_pay.validate_merchant`<a id="twoctwopapple_payvalidate_merchant"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
validate_merchant_response = twoctwop.apple_pay.validate_merchant(
    payment_token="string_example",
    validation_url="string_example",
    locale="string_example",
    client_id="046b6c7f-0b8a-43b9-b35d-6489e6daee91",
    browser_details={
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### payment_token: `str`<a id="payment_token-str"></a>

##### validation_url: `Optional[str]`<a id="validation_url-optionalstr"></a>

##### locale: `Optional[str]`<a id="locale-optionalstr"></a>

##### client_id: `str`<a id="client_id-str"></a>

##### browser_details: [`BrowserDetails`](./2c2p_python_sdk/type/browser_details.py)<a id="browser_details-browserdetails2c2p_python_sdktypebrowser_detailspy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MerchantValidationApplePay`](./2c2p_python_sdk/type/merchant_validation_apple_pay.py)
#### 🔄 Return<a id="🔄-return"></a>

[`MerchantValidationApplePayResponse`](./2c2p_python_sdk/pydantic/merchant_validation_apple_pay_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/payment/4.3/applepay/merchantvalidation` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `twoctwop.cache.clean_cache`<a id="twoctwopcacheclean_cache"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
twoctwop.cache.clean_cache()
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/payment/4.3/cache/cleancache` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `twoctwop.cancel_transaction.post`<a id="twoctwopcancel_transactionpost"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
post_response = twoctwop.cancel_transaction.post(
    payment_token="string_example",
    locale="string_example",
    client_id="046b6c7f-0b8a-43b9-b35d-6489e6daee91",
    browser_details={
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### payment_token: `str`<a id="payment_token-str"></a>

##### locale: `Optional[str]`<a id="locale-optionalstr"></a>

##### client_id: `str`<a id="client_id-str"></a>

##### browser_details: [`BrowserDetails`](./2c2p_python_sdk/type/browser_details.py)<a id="browser_details-browserdetails2c2p_python_sdktypebrowser_detailspy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PaymentBaseRequest`](./2c2p_python_sdk/type/payment_base_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PaymentNonRedirectResponse`](./2c2p_python_sdk/pydantic/payment_non_redirect_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/payment/4.3/canceltransaction` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `twoctwop.card_installment_plan_info.create`<a id="twoctwopcard_installment_plan_infocreate"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_response = twoctwop.card_installment_plan_info.create(
    payment_token="string_example",
    card_no="string_example",
    bank_code="string_example",
    locale="string_example",
    client_id="046b6c7f-0b8a-43b9-b35d-6489e6daee91",
    browser_details={
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### payment_token: `str`<a id="payment_token-str"></a>

##### card_no: `Optional[str]`<a id="card_no-optionalstr"></a>

##### bank_code: `Optional[str]`<a id="bank_code-optionalstr"></a>

##### locale: `Optional[str]`<a id="locale-optionalstr"></a>

##### client_id: `str`<a id="client_id-str"></a>

##### browser_details: [`BrowserDetails`](./2c2p_python_sdk/type/browser_details.py)<a id="browser_details-browserdetails2c2p_python_sdktypebrowser_detailspy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CardInstallmentPlanInfoRequest`](./2c2p_python_sdk/type/card_installment_plan_info_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PaymentOptionDetailsResponse`](./2c2p_python_sdk/pydantic/payment_option_details_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/payment/4.3/cardinstallmentplaninfo` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `twoctwop.card_token_info.get_card_token_info`<a id="twoctwopcard_token_infoget_card_token_info"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_card_token_info_response = twoctwop.card_token_info.get_card_token_info(
    payment_token="string_example",
    locale="string_example",
    client_id="046b6c7f-0b8a-43b9-b35d-6489e6daee91",
    browser_details={
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### payment_token: `str`<a id="payment_token-str"></a>

##### locale: `Optional[str]`<a id="locale-optionalstr"></a>

##### client_id: `str`<a id="client_id-str"></a>

##### browser_details: [`BrowserDetails`](./2c2p_python_sdk/type/browser_details.py)<a id="browser_details-browserdetails2c2p_python_sdktypebrowser_detailspy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PaymentBaseRequest`](./2c2p_python_sdk/type/payment_base_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PaymentCardTokenResponseV43`](./2c2p_python_sdk/pydantic/payment_card_token_response_v43.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/payment/4.3/cardtokeninfo` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `twoctwop.exchange_rate.apm_mcc`<a id="twoctwopexchange_rateapm_mcc"></a>

APM MCC Exchange Rate

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
apm_mcc_response = twoctwop.exchange_rate.apm_mcc(
    payment_token="string_example",
    locale="string_example",
    client_id="046b6c7f-0b8a-43b9-b35d-6489e6daee91",
    browser_details={
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### payment_token: `str`<a id="payment_token-str"></a>

##### locale: `Optional[str]`<a id="locale-optionalstr"></a>

##### client_id: `str`<a id="client_id-str"></a>

##### browser_details: [`BrowserDetails`](./2c2p_python_sdk/type/browser_details.py)<a id="browser_details-browserdetails2c2p_python_sdktypebrowser_detailspy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PaymentBaseRequest`](./2c2p_python_sdk/type/payment_base_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PaymentApmMccExchangeRateResponse`](./2c2p_python_sdk/pydantic/payment_apm_mcc_exchange_rate_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/payment/4.3/exchangerate/apmmccexchangerate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `twoctwop.exchange_rate.get_rate`<a id="twoctwopexchange_rateget_rate"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_rate_response = twoctwop.exchange_rate.get_rate(
    payment_token="string_example",
    bin="string_example",
    locale="string_example",
    client_id="046b6c7f-0b8a-43b9-b35d-6489e6daee91",
    browser_details={
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### payment_token: `str`<a id="payment_token-str"></a>

##### bin: `Optional[str]`<a id="bin-optionalstr"></a>

##### locale: `Optional[str]`<a id="locale-optionalstr"></a>

##### client_id: `str`<a id="client_id-str"></a>

##### browser_details: [`BrowserDetails`](./2c2p_python_sdk/type/browser_details.py)<a id="browser_details-browserdetails2c2p_python_sdktypebrowser_detailspy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PaymentExchangeRateConverterRequest`](./2c2p_python_sdk/type/payment_exchange_rate_converter_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PaymentExchangeRateConverterResponse`](./2c2p_python_sdk/pydantic/payment_exchange_rate_converter_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/payment/4.3/exchangerate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `twoctwop.exchange_rate.request_endpoint`<a id="twoctwopexchange_raterequest_endpoint"></a>

JWT Request Endpoint

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
request_endpoint_response = twoctwop.exchange_rate.request_endpoint(
    payload="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### payload: `Optional[str]`<a id="payload-optionalstr"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PayloadRequest`](./2c2p_python_sdk/type/payload_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PayloadRequest`](./2c2p_python_sdk/pydantic/payload_request.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/payment/4.3/exchangerate/secure` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `twoctwop.initialization.request_creation`<a id="twoctwopinitializationrequest_creation"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
request_creation_response = twoctwop.initialization.request_creation()
```

#### 🔄 Return<a id="🔄-return"></a>

[`PaymentInitializationResponse`](./2c2p_python_sdk/pydantic/payment_initialization_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/payment/4.3/initialization` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `twoctwop.loyalty_point_info.post_loyalty_point_info`<a id="twoctwoployalty_point_infopost_loyalty_point_info"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
post_loyalty_point_info_response = twoctwop.loyalty_point_info.post_loyalty_point_info(
    payment_token="string_example",
    provider_id="string_example",
    profile_id="string_example",
    reference_id="string_example",
    card_no="string_example",
    expiry_month="string_example",
    expiry_year="string_example",
    locale="string_example",
    client_id="046b6c7f-0b8a-43b9-b35d-6489e6daee91",
    browser_details={
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### payment_token: `str`<a id="payment_token-str"></a>

##### provider_id: `Optional[str]`<a id="provider_id-optionalstr"></a>

##### profile_id: `Optional[str]`<a id="profile_id-optionalstr"></a>

##### reference_id: `Optional[str]`<a id="reference_id-optionalstr"></a>

##### card_no: `Optional[str]`<a id="card_no-optionalstr"></a>

##### expiry_month: `Optional[str]`<a id="expiry_month-optionalstr"></a>

##### expiry_year: `Optional[str]`<a id="expiry_year-optionalstr"></a>

##### locale: `Optional[str]`<a id="locale-optionalstr"></a>

##### client_id: `str`<a id="client_id-str"></a>

##### browser_details: [`BrowserDetails`](./2c2p_python_sdk/type/browser_details.py)<a id="browser_details-browserdetails2c2p_python_sdktypebrowser_detailspy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PaymentLoyaltyPointInfoRequest`](./2c2p_python_sdk/type/payment_loyalty_point_info_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PaymentLoyaltyPointInfoResponse`](./2c2p_python_sdk/pydantic/payment_loyalty_point_info_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/payment/4.3/loyaltypointinfo` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `twoctwop.payment.create_payment`<a id="twoctwoppaymentcreate_payment"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_payment_response = twoctwop.payment.create_payment(
    payment_token="string_example",
    payment={
    },
    response_return_url="string_example",
    client_ip="string_example",
    locale="string_example",
    client_id="046b6c7f-0b8a-43b9-b35d-6489e6daee91",
    browser_details={
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### payment_token: `str`<a id="payment_token-str"></a>

##### payment: [`PaymentParamsRequestV43`](./2c2p_python_sdk/type/payment_params_request_v43.py)<a id="payment-paymentparamsrequestv432c2p_python_sdktypepayment_params_request_v43py"></a>


##### response_return_url: `Optional[str]`<a id="response_return_url-optionalstr"></a>

##### client_ip: `Optional[str]`<a id="client_ip-optionalstr"></a>

##### locale: `Optional[str]`<a id="locale-optionalstr"></a>

##### client_id: `str`<a id="client_id-str"></a>

##### browser_details: [`BrowserDetails`](./2c2p_python_sdk/type/browser_details.py)<a id="browser_details-browserdetails2c2p_python_sdktypebrowser_detailspy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PaymentRequestV43`](./2c2p_python_sdk/type/payment_request_v43.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PaymentResponse`](./2c2p_python_sdk/pydantic/payment_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/payment/4.3/payment` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `twoctwop.payment_inquiry.post_payment_details`<a id="twoctwoppayment_inquirypost_payment_details"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
post_payment_details_response = twoctwop.payment_inquiry.post_payment_details(
    payload="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### payload: `Optional[str]`<a id="payload-optionalstr"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PayloadRequest`](./2c2p_python_sdk/type/payload_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PayloadRequest`](./2c2p_python_sdk/pydantic/payload_request.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/payment/4.3/paymentinquiry` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `twoctwop.payment_instruction.submit_instruction`<a id="twoctwoppayment_instructionsubmit_instruction"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
submit_instruction_response = twoctwop.payment_instruction.submit_instruction(
    payload="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### payload: `Optional[str]`<a id="payload-optionalstr"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PayloadRequest`](./2c2p_python_sdk/type/payload_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PayloadRequest`](./2c2p_python_sdk/pydantic/payload_request.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/payment/4.3/paymentinstruction` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `twoctwop.payment_notification.process_notification`<a id="twoctwoppayment_notificationprocess_notification"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
process_notification_response = twoctwop.payment_notification.process_notification(
    payment_token="string_example",
    plateform="string_example",
    recipient_id="string_example",
    recipient_name="string_example",
    locale="string_example",
    client_id="046b6c7f-0b8a-43b9-b35d-6489e6daee91",
    browser_details={
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### payment_token: `str`<a id="payment_token-str"></a>

##### plateform: `Optional[str]`<a id="plateform-optionalstr"></a>

##### recipient_id: `Optional[str]`<a id="recipient_id-optionalstr"></a>

##### recipient_name: `Optional[str]`<a id="recipient_name-optionalstr"></a>

##### locale: `Optional[str]`<a id="locale-optionalstr"></a>

##### client_id: `str`<a id="client_id-str"></a>

##### browser_details: [`BrowserDetails`](./2c2p_python_sdk/type/browser_details.py)<a id="browser_details-browserdetails2c2p_python_sdktypebrowser_detailspy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PaymentNotificationRequest`](./2c2p_python_sdk/type/payment_notification_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PaymentResponseBase`](./2c2p_python_sdk/pydantic/payment_response_base.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/payment/4.3/paymentnotification` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `twoctwop.payment_option.create_payment_option`<a id="twoctwoppayment_optioncreate_payment_option"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_payment_option_response = twoctwop.payment_option.create_payment_option(
    payment_token="string_example",
    locale="string_example",
    client_id="046b6c7f-0b8a-43b9-b35d-6489e6daee91",
    browser_details={
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### payment_token: `str`<a id="payment_token-str"></a>

##### locale: `Optional[str]`<a id="locale-optionalstr"></a>

##### client_id: `str`<a id="client_id-str"></a>

##### browser_details: [`BrowserDetails`](./2c2p_python_sdk/type/browser_details.py)<a id="browser_details-browserdetails2c2p_python_sdktypebrowser_detailspy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PaymentBaseRequest`](./2c2p_python_sdk/type/payment_base_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PaymentOptionResponse`](./2c2p_python_sdk/pydantic/payment_option_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/payment/4.3/paymentoption` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `twoctwop.payment_option_details.post_option_details`<a id="twoctwoppayment_option_detailspost_option_details"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
post_option_details_response = twoctwop.payment_option_details.post_option_details(
    category_code="string_example",
    group_code="string_example",
    payment_token="string_example",
    locale="string_example",
    client_id="046b6c7f-0b8a-43b9-b35d-6489e6daee91",
    browser_details={
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### category_code: `str`<a id="category_code-str"></a>

##### group_code: `str`<a id="group_code-str"></a>

##### payment_token: `str`<a id="payment_token-str"></a>

##### locale: `Optional[str]`<a id="locale-optionalstr"></a>

##### client_id: `str`<a id="client_id-str"></a>

##### browser_details: [`BrowserDetails`](./2c2p_python_sdk/type/browser_details.py)<a id="browser_details-browserdetails2c2p_python_sdktypebrowser_detailspy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PaymentOptionDetailsRequest`](./2c2p_python_sdk/type/payment_option_details_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PaymentOptionDetailsResponse`](./2c2p_python_sdk/pydantic/payment_option_details_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/payment/4.3/paymentoptiondetails` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `twoctwop.payment_simulate.execute_payment_simulation`<a id="twoctwoppayment_simulateexecute_payment_simulation"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
execute_payment_simulation_response = twoctwop.payment_simulate.execute_payment_simulation(
    payload="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### payload: `Optional[str]`<a id="payload-optionalstr"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PayloadRequest`](./2c2p_python_sdk/type/payload_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PayloadRequest`](./2c2p_python_sdk/pydantic/payload_request.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/payment/4.3/paymentsimulate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `twoctwop.payment_token.generate_token`<a id="twoctwoppayment_tokengenerate_token"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
generate_token_response = twoctwop.payment_token.generate_token(
    payload="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### payload: `Optional[str]`<a id="payload-optionalstr"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PayloadRequest`](./2c2p_python_sdk/type/payload_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PayloadRequest`](./2c2p_python_sdk/pydantic/payload_request.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/payment/4.3/paymenttoken` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `twoctwop.redirect_back_end.post_payment_redirect`<a id="twoctwopredirect_back_endpost_payment_redirect"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
twoctwop.redirect_back_end.post_payment_redirect(
    payment_response="string_example",
    is_leave_app="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### payment_response: `str`<a id="payment_response-str"></a>

##### is_leave_app: `str`<a id="is_leave_app-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`RedirectBackEndPostPaymentRedirectRequest`](./2c2p_python_sdk/type/redirect_back_end_post_payment_redirect_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/payment/4.3/redirectbackend` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `twoctwop.redirect_front_end.post_payment_redirect`<a id="twoctwopredirect_front_endpost_payment_redirect"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
twoctwop.redirect_front_end.post_payment_redirect(
    pay_response="string_example",
    is_leave_app="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### pay_response: `str`<a id="pay_response-str"></a>

##### is_leave_app: `str`<a id="is_leave_app-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`RedirectFrontEndPostPaymentRedirectRequest`](./2c2p_python_sdk/type/redirect_front_end_post_payment_redirect_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/payment/4.3/redirectfrontend` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `twoctwop.transaction_status.update_transaction_status`<a id="twoctwoptransaction_statusupdate_transaction_status"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_transaction_status_response = twoctwop.transaction_status.update_transaction_status(
    payment_token="string_example",
    additional_info=True,
    locale="string_example",
    client_id="046b6c7f-0b8a-43b9-b35d-6489e6daee91",
    browser_details={
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### payment_token: `str`<a id="payment_token-str"></a>

##### additional_info: `bool`<a id="additional_info-bool"></a>

##### locale: `Optional[str]`<a id="locale-optionalstr"></a>

##### client_id: `str`<a id="client_id-str"></a>

##### browser_details: [`BrowserDetails`](./2c2p_python_sdk/type/browser_details.py)<a id="browser_details-browserdetails2c2p_python_sdktypebrowser_detailspy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TransactionStatusRequest`](./2c2p_python_sdk/type/transaction_status_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`TransactionStatusResponse`](./2c2p_python_sdk/pydantic/transaction_status_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/payment/4.3/transactionstatus` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `twoctwop.user_preference.save_user_preference`<a id="twoctwopuser_preferencesave_user_preference"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
save_user_preference_response = twoctwop.user_preference.save_user_preference(
    payment_token="string_example",
    locale="string_example",
    client_id="046b6c7f-0b8a-43b9-b35d-6489e6daee91",
    browser_details={
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### payment_token: `str`<a id="payment_token-str"></a>

##### locale: `Optional[str]`<a id="locale-optionalstr"></a>

##### client_id: `str`<a id="client_id-str"></a>

##### browser_details: [`BrowserDetails`](./2c2p_python_sdk/type/browser_details.py)<a id="browser_details-browserdetails2c2p_python_sdktypebrowser_detailspy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PaymentBaseRequest`](./2c2p_python_sdk/type/payment_base_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PaymentUserPreferenceResponse`](./2c2p_python_sdk/pydantic/payment_user_preference_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/payment/4.3/userpreference` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
