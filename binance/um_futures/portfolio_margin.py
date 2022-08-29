def pm_exchange_info(self, symbol: str = None):
    """
    |
    | **Portfolio Margin Exchange Information**
    | *Current Portfolio Margin exchange trading rules.*

    :API endpoint: ``GET /fapi/v1/pmExchangeInfo``
    :API doc: https://binance-docs.github.io/apidocs/futures/en/#portfolio-margin-endpoints

    :parameter symbol: string; the trading pair.
    |
    """

    params = {"symbol": symbol}
    return self.query("/fapi/v1/pmExchangeInfo", params)
