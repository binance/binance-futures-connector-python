def pm_exchange_info(self, symbol: str = None):
    """
    |
    | **Portfolio Margin Exchange Information**
    | *Current Portfolio Margin exchange trading rules.*

    :API endpoint: ``GET /dapi/v1/pmExchangeInfo``
    :API doc: https://developers.binance.com/docs/derivatives/coin-margined-futures/portfolio-margin-endpoints/Query-Classic-Portfolio-Margin-Notional-Limit

    :parameter symbol: string; the trading pair.
    |
    """

    params = {"symbol": symbol}
    return self.query("/dapi/v1/pmExchangeInfo", params)
