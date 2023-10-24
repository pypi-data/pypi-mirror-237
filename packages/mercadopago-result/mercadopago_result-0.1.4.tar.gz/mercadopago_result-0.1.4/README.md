MercadoPago Result
==================
A simple interface with MercadoPago RESTFUL API. This package use the packages
Result, Pydantic and HTTPX.

*Pydantic* makes sure to validate the data sent and received by the HTTP
requests.

*Result* is a package that implements an imitation of the programming language
Rust for returning results, also put a good use for the Python statement
"match"

*HTTPX* handles all requesitions send to the API.

## Table of Contents
- [Installation](#installation)
- [Summary](#summary)
  - [AccessToken](#accesstoken)
- [Requests](#requests)
  - [Checkout](#checkout)
    - [Create](#create)
    - [List](#list)
    - [Get](#get)
    - [Put](#put)
  - [Client](#client)
    - [Create](#create-1)
    - [List](#list-1)
    - [Get](#get-1)
    - [Put](#put-1)

Installation
============
Latest version
``` cmd
$ pip install mercadopago-result
```

Summary
=======
The idea for this library was to not depend on JSON / Dict objects to be sent and
received to and from the MercadoPago API. With Pydantic model validation, it is
possible to be sure that the data you sent or received is what you expected.
And the Result library is a nice way to handle the Package requests results.

To use this package it is necessary to get a MercadoPago API Token and create
an AccessToken object with it, then all API requests will require the token and
a object filter depending of what will be requested.

# AccessToken
Example creating the AccessToken:

``` python
from result import Ok, Err

from mercadopago_result.authentication import AccessToken
from mercadopago_result.authentication import AccessTokenError


access_token = None
match AccessToken.load_from_json_file("token_file.json"):
    case Ok(access_token):
        # The token's file had no problems and now the access_token is set
        pass
    case Err(AccessTokenError.LoadingFile.FileDoesNotExist(path)):
        # The error above set the 'path' with the file path that it could not
        # find
        print(f"File '{path}' does not exist")
    case Err(AccessTokenError.Parsing(message)):
        # If the message didn't matter, just put a underscore _ instead of
        # 'message'.
        print(f"Invalid Json: {message}")
# If everything was Ok in the match statement this should print the token model
print(access_token)

```

And this is an example to not deal with result library, in case it is not
desired to write an entire match statement:
``` python
from mercadopago_result.authentication import AccessToken
# This will raise an exception if the loading returned an Err instead of an Ok
access_token = AccessToken.load_from_json_file("token_file.json").unwrap()
print(access_token)
```

Requests
========

For now the package only have works with MercadoPago API Checkout and Client.

Here are some examples for Checkout requests.

# Checkout
## Create

Endpoint "https://api.mercadopago.com/checkout/preferences"

``` python
from pprint import pprint  # just for the example
from result import Ok, Err

from mercadopago_result.authorization import AccessToken
from mercadopago_result.api_requests.checkout import send_checkout_create_request
from mercadopago_result.api_requests.checkout import CheckoutCreateError
from mercadopago_result.checkout import Checkout
from mercadopago_result.checkout import ItemListField
from mercadopago_result.checkout import CheckoutRedirectURLS

access_token = AccessToken(
    public="YOUR_PUBLIC_API_TOKEN",
    private="YOUR_PRIVATE_API_TOKEN")
checkout_items: ItemListField = [
    Item(title="Something nice",
         quantity=420,
         currency_id=ValidCurrencies.BRL,
         unit_price=69.0),
    # ...
    # Item(...)
]
checkout_redirect_urls = CheckoutRedirectURLS(
    success="my.site.com/success",
    failure="my.site.com/failure",
    pending="my.site.com/pending")
checkout = Checkout(items=checkout_items,
                    back_urls=checkout_redirect_urls,
                    # same as "approved"
                    auto_return=CheckoutAutoReturnOptions.APPROVED,
                    notification_url="my.site.com/webhook")
pprint(checkout.model_dump(exclude_unset=True))
match send_checkout_create_request(checkout, access_token):
    case Ok(checkout_response_from_api):
        pprint(checkout_response_from_api.model_dump(exclude_unset=True))
    case Err(CheckoutCreateError.HttpRequest(code,
                                             api_error_type,
                                             api_error_message)):
        print(code, api_error_type, api_error_message)
    case Err(something_unexpected):
        print(something_unexpected)

# This also have the same result but avoid the match statement
checkout = send_checkout_create_request(checkout, access_token).unwrap()
pprint(checkout.model_dump(exclude_unset=True))
```

## List

Endpoint "https://api.mercadopago.com/checkout/preferences/search"

``` python
from pprint import pprint
from mercadopago_result.api_requests.checkout import send_checkout_get_list_request
from mercadopago_result.checkout import Checkout
from mercadopago_result.checkout import CheckoutShorten
from mercadopago_result.authentication import AccessToken

token = AccessToken(
    public="YOUR_PUBLIC_API_TOKEN",
    private="YOUR_PRIVATE_API_TOKEN")
# A checkout that will be used as filter
checkout_filter = Checkout()
checkout_list = send_checkout_get_list_request(checkout_filter, token).unwrap()
pprint([c.model_dump(exclude_unset=True) for c in checkout_list])
# the send_checkout_get_list_request returns a list of CheckoutShorten.
# For some reason the API responds with different type of checkout for this
# request, so it was necessary to create a second class to handle this. In
# future this package might be adjusted to return a Checkout instead

```

## Get

Endpoint "https://api.mercadopago.com/checkout/preferences/{id}"

``` python
from pprint import pprint
from mercadopago_result.api_requests.checkout import send_checkout_get_request
from mercadopago_result.checkout import Checkout
from mercadopago_result.authentication import AccessToken
token = AccessToken(
    public="YOUR_PUBLIC_API_TOKEN",
    private="YOUR_PRIVATE_API_TOKEN")
checkout_filter = Checkout(id="id")
checkout_response = send_checkout_get_request(checkout_filter, token).unwrap()
pprint(checkout_response.model_dump(exclude_unset=True))
```

## Put

Endpoint "https://api.mercadopago.com/checkout/preferences/{id}"

``` python
from pprint import pprint
from mercadopago_result.api_requests.checkout import send_checkout_put_request
from mercadopago_result.checkout import Checkout
from mercadopago_result.authentication import AccessToken
token = AccessToken(
    public="YOUR_PUBLIC_API_TOKEN",
    private="YOUR_PRIVATE_API_TOKEN")
checkout_filter = Checkout(id="id", )  # id and other values to be updated
checkout_response = send_checkout_put_request(checkout_filter, token).unwrap()
pprint(checkout_response.model_dump(exclude_unset=True))
```

# Client

## Create

Endpoint "https://api.mercadopago.com/v1/customers"

``` python
from pprint import pprint
from mercadopago_result.client import Client
from mercadopago_result.authentication import AccessToken
from mercadopago_result.api_requests.client import send_client_creation_request
token = AccessToken(
    public="YOUR_PUBLIC_API_TOKEN",
    private="YOUR_PRIVATE_API_TOKEN")
client_info = Client()  # fill the information
new_client = send_client_creation_request(client_info, token)
pprint(new_client.model_dump(exclude_unset=True))
```

## List

Endpoint "https://api.mercadopago.com/v1/customers/search"

``` python
from pprint import pprint
from mercadopago_result.client import Client
from mercadopago_result.authentication import AccessToken
from mercadopago_result.api_requests.client import send_client_get_list_request
token = AccessToken(
    public="YOUR_PUBLIC_API_TOKEN",
    private="YOUR_PRIVATE_API_TOKEN")
client_filter = Client()  # fill the information
client_list = send_client_get_list_request(client_filter, token)
pprint([c.model_dump(exclude_unset=True) for c in client_list])
```

## Get

Endpoint "https://api.mercadopago.com/v1/customers/search"

Obs.: The actual endpoint if "https://api.mercadopago.com/v1/customers/{id}"
this package is using the search endpoint because both return the same client
object with the same amount of information. This might change in future to use
the proper endpoint
``` python
from pprint import pprint
from mercadopago_result.client import Client
from mercadopago_result.authentication import AccessToken
from mercadopago_result.api_requests.client import send_client_get_request
token = AccessToken(
    public="YOUR_PUBLIC_API_TOKEN",
    private="YOUR_PRIVATE_API_TOKEN")
client_filter = Client()  # fill the information
client = send_client_get_request(client_filter, token)
pprint(client.model_dump(exclude_unset=True))
```

## Put

Endpoint "https://api.mercadopago.com/v1/customers/{id}"

``` python
from pprint import pprint
from mercadopago_result.client import Client
from mercadopago_result.authentication import AccessToken
from mercadopago_result.api_requests.client import send_client_put_request
token = AccessToken(
    public="YOUR_PUBLIC_API_TOKEN",
    private="YOUR_PRIVATE_API_TOKEN")
client_update_data = Client()  # fill the information
client = send_client_put_request(client_update_data, token)
pprint(client.model_dump(exclude_unset=True))
```
