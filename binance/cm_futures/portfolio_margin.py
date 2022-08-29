def pm_exchange_info(self, symbol: str = None):
    """
    |
    | **Portfolio Margin Exchange Information**
    | *Current Portfolio Margin exchange trading rules.*

    :API endpoint: ``GET /dapi/v1/pmExchangeInfo``
    :API doc: https://binance-docs.github.io/apidocs/delivery/en/#portfolio-margin-exchange-information

    :parameter symbol: string; the trading pair.
    |
    """

    params = {"symbol": symbol}
    return self.query("/dapi/v1/pmExchangeInfo", params)
