# Changelog

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
