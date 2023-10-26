"""FMP Stock News fetcher."""

from typing import Any, Dict, List, Optional, Union

from openbb_fmp.utils.helpers import get_data_many
from openbb_provider.abstract.fetcher import Fetcher
from openbb_provider.standard_models.stock_news import (
    StockNewsData,
    StockNewsQueryParams,
)
from pydantic import Field


class FMPStockNewsQueryParams(StockNewsQueryParams):
    """FMP Stock News query.

    Source: https://site.financialmodelingprep.com/developer/docs/stock-news-api/
    """

    __alias_dict__ = {"symbols": "tickers"}
    page: Optional[int] = Field(
        default=0,
        description="Page number of the results. Use in combination with limit.",
    )


class FMPStockNewsData(StockNewsData):
    """FMP Stock News data."""

    __alias_dict__ = {"date": "publishedDate"}

    symbol: str = Field(description="Ticker of the fetched news.")
    image: Optional[Union[List[str], str]] = Field(
        default=None, description="URL to the image of the news source."
    )
    site: str = Field(description="Name of the news source.")
    images: Optional[Union[List[str], str]] = Field(
        default=None, description="URL to the images of the news."
    )


class FMPStockNewsFetcher(
    Fetcher[
        FMPStockNewsQueryParams,
        List[FMPStockNewsData],
    ]
):
    """Transform the query, extract and transform the data from the FMP endpoints."""

    @staticmethod
    def transform_query(params: Dict[str, Any]) -> FMPStockNewsQueryParams:
        """Transform the query params."""
        return FMPStockNewsQueryParams(**params)

    @staticmethod
    def extract_data(
        query: FMPStockNewsQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[Dict]:
        """Return the raw data from the FMP endpoint."""
        api_key = credentials.get("fmp_api_key") if credentials else ""

        base_url = "https://financialmodelingprep.com/api/v3/stock_news"
        data = []
        url = f"{base_url}?page={query.page}&tickers={query.symbols}&limit={query.limit}&apikey={api_key}"
        response = get_data_many(url, **kwargs)

        if len(response) > 0:
            data = sorted(response, key=lambda x: x["publishedDate"], reverse=True)

        return data

    @staticmethod
    def transform_data(
        query: FMPStockNewsQueryParams, data: List[Dict], **kwargs: Any
    ) -> List[FMPStockNewsData]:
        """Return the transformed data."""
        return [FMPStockNewsData.model_validate(d) for d in data]
