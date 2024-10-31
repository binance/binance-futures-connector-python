# Changelog

## 4.1.0 - 2024-10-31

### Added
- UM_Futures:
  - `GET /fapi/v1/fundingInfo`
  - `GET /futures/data/delivery-price`
  - `GET /fapi/v1/constituents`
  - `GET /fapi/v1/accountConfig`
  - `GET /fapi/v1/symbolConfig`
  - `GET /fapi/v1/rateLimit/order`
  - `GET /fapi/v1/order/asyn`
  - `GET /fapi/v1/order/asyn/id`
  - `GET /fapi/v1/trade/asyn`
  - `GET /fapi/v1/trade/asyn/id`
  - `POST /fapi/v1/feeBurn`
  - `GET /fapi/v1/feeBurn`
  - `GET /fapi/v1/convert/exchangeInfo`
  - `POST /fapi/v1/convert/getQuote`
  - `POST /fapi/v1/convert/acceptQuote`
  - `GET /fapi/v1/convert/orderStatus`
  - Websocket Stream `mark_price_all_market`

- CM_Futures:
  - `GET /dapi/v1/income/asyn`
  - `GET /dapi/v1/constituents`

### Changed
- UM_Futures:
  - `GET /fapi/v1/income`: Add parameter `page` for pagination
  - `POST /fapi/v1/order`: Add parameters `selfTradePreventionMode`, `priceMatch` and `goodTillDate`
  - `POST /fapi/v1/batchOrders`: Add parameters `priceMatch`, `selfTradePreventionMode` and `goodTillDate`
  - `GET /fapi/v1/ticker/price`: deprecated, replaced by `GET /fapi/v2/ticker/price`
  - `GET /fapi/v2/balance`: deprecated, replaced by `GET /fapi/v3/balance`
  - `GET /fapi/v2/account`: deprecated, replaced by `GET /fapi/v3/account`
  - `GET /fapi/v2/positionRisk`: deprecated, replaced by `GET /fapi/v3/positionRisk`

- CM_Futures:
  - `GET /dapi/v1/income`: Add parameter `page` for pagination
  - `POST /dapi/v1/order`: Add parameters `priceMatch` and `selfTradePreventionMode`

- Update Websocket connection exceptions: Add `_handle_exception` method to handle exceptions

### Removed
- CM_Futures:
  - `/dapi/v1/pmExchangeInfo`

## 4.0.1 - 2024-10-03

### Removed
- UM_Futures:
  - `GET /v1/pmExchangeInfo`

## 4.0.0 - 2023-08-08

### Changed
- Add proxy support for websockets
- Remove support for Python 3.7

## 4.0.0rc3 - 2023-07-03

### Changed
- Change `User-Agent`

### Updated 
- Fixed `modify_order` (`PUT /fapi/v1/order`) Endpoint by correctly adding the `price` parameter 

## 4.0.0rc2 - 2023-05-25

### Added
- Implemented Modify Order (`PUT /fapi/v1/order`) - `modify_order` for UM Futures.

## 4.0.0rc1 - 2023-05-18

### Changed
- Redesign of Websocket part. Please consult `README.md` for details on its new usage.

## 3.3.1 - 2023-03-21

### Updated
- Merge #68

## 3.3.0 - 2023-01-11

### Add
- RSA Key support

### Remove
- Python 3.6 Support Deprecated

## 3.2.0 - 2022-08-29

### Add
#### UM Futures
 - New endpoint `GET /fapi/v1/pmExchangeInfo` to get current Portfolio Margin exchange trading rules.
#### CM Futures
 - New endpoint `GET /dapi/v1/pmExchangeInfo` to get current Portfolio Margin exchange trading rules.

### Update
#### UM Futures
 - `symbol` is no longer a required parameter in `GET /fapi/v1/premiumIndex`

## 3.1.2 - 2022-08-23

### Update
- Fix encoding issue of parameters in `DELETE /fapi/v1/batchOrders`

## 3.1.1 - 2022-06-02

### Update
- Fix import path error in example files

## 3.1.0 - 2022-06-02

### Add

- New endpoint `GET /fapi/v1/income/asyn` to get Download Id For Futures Transaction History
- New endpoint `GET /fapi/v1/income/asyn/id` to get Futures Transaction History Download Link by Id


## 3.0.0 - 2022-05-26

- Refactor the connector
