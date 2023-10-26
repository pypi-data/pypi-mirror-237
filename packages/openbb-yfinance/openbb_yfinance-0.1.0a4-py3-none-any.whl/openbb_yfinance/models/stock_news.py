"""yfinance Stock News fetcher."""


import json
from datetime import datetime
from typing import Any, Dict, List, Optional

from openbb_provider.abstract.fetcher import Fetcher
from openbb_provider.standard_models.stock_news import (
    StockNewsData,
    StockNewsQueryParams,
)
from pydantic import Field, field_validator
from yfinance import Ticker


class YFinanceStockNewsQueryParams(StockNewsQueryParams):
    """YFinance Stock News Query.

    Source: https://finance.yahoo.com/news/
    """


class YFinanceStockNewsData(StockNewsData):
    """YFinance Stock News Data."""

    __alias_dict__ = {"date": "providerPublishTime", "url": "link"}

    uuid: str = Field(description="Unique identifier for the news article")
    publisher: str = Field(description="Publisher of the news article")
    type: str = Field(description="Type of the news article")
    thumbnail: Optional[List] = Field(
        default=None, description="Thumbnail related data to the ticker news article."
    )
    relatedTickers: str = Field(description="Tickers related to the news article.")

    @field_validator("providerPublishTime", mode="before", check_fields=False)
    def date_validate(cls, v):  # pylint: disable=E0213
        return datetime.fromtimestamp(v)

    @field_validator("relatedTickers", mode="before", check_fields=False)
    def related_tickers_string(cls, v):  # pylint: disable=E0213
        return ", ".join(v)

    @field_validator("thumbnail", mode="before", check_fields=False)
    def thumbnail_list(cls, v):  # pylint: disable=E0213
        return v["resolutions"]


class YFinanceStockNewsFetcher(
    Fetcher[
        YFinanceStockNewsQueryParams,
        List[YFinanceStockNewsData],
    ]
):
    @staticmethod
    def transform_query(params: Dict[str, Any]) -> YFinanceStockNewsQueryParams:
        return YFinanceStockNewsQueryParams(**params)

    @staticmethod
    def extract_data(
        query: YFinanceStockNewsQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[Dict]:
        data = Ticker(query.symbols).get_news()
        data = json.loads(json.dumps(data))

        return data

    @staticmethod
    def transform_data(
        query: YFinanceStockNewsQueryParams,
        data: List[Dict],
        **kwargs: Any,
    ) -> List[YFinanceStockNewsData]:
        return [YFinanceStockNewsData.model_validate(d) for d in data]
