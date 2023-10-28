"""
This module tests the econ module.
"""
import datetime
from unittest import mock

import pandas as pd
import pytest
from econ import get_indicator


def mock_datareader_generic(*args, **kwargs):
    """
    Mock the pandas_datareader.data.DataReader function
    """
    series = args[0]
    dataframe = pd.DataFrame(
        {series: [1, 2, 3]}, index=[datetime.datetime(2020, 1, i) for i in range(1, 4)]
    )
    return dataframe


def mock_datareader_not_implemented(*args, **kwargs):
    """
    mock the pandas_datareader.data.DataReader function
    """
    raise NotImplementedError


def mock_datareader_general_error(*args, **kwargs):
    """mock the pandas_datareader.data.DataReader function"""
    raise Exception("An unexpected error")


# Test successful data retrieval for different indicators
@pytest.mark.parametrize(
    "indicator, start_year, end_year",
    [
        ("AWHMAN", 2020, 2021),
        ("IC4WSA", 2019, 2020),
        ("DGORDER", 2018, 2019),
        ("ANDENO", 2015, 2016),
        ("PERMIT", 2010, 2011),
        ("SP500", 2005, 2006),
        ("M2", 2000, 2001),
        ("UMCSENT", 1996, 1997),
    ],
)
@mock.patch("pandas_datareader.data.DataReader", side_effect=mock_datareader_generic)
def test_get_indicator_happy_path(mocked_datareader, indicator, start_year, end_year):
    """
    Test for successful data retrieval for different indicators"""
    result = get_indicator(indicator, start_year, end_year)
    assert result is not None
    assert indicator in result.columns
    assert len(result) == 3
    assert all(isinstance(val, (int, float)) for val in result[indicator].tolist())


# Test for return type None for invalid indicator
@mock.patch(
    "pandas_datareader.data.DataReader", side_effect=Exception("Unable to read URL")
)
def test_get_indicator_none_return(mocked_datareader):
    """Test for return type None for invalid indicator"""
    result = get_indicator("INVALID", 2020, 2021)
    assert result is None


# Test for NotImplementedError
@mock.patch(
    "pandas_datareader.data.DataReader", side_effect=mock_datareader_not_implemented
)
def test_get_indicator_not_implemented_error(mocked_datareader):
    """Test for NotImplementedError"""
    result = get_indicator("AWHMAN", 2020, 2021)
    assert result is None


# Test for general errors
@mock.patch(
    "pandas_datareader.data.DataReader", side_effect=mock_datareader_general_error
)
def test_get_indicator_general_error(mocked_datareader):
    """Test for general errors"""
    result = get_indicator("AWHMAN", 2020, 2021)
    assert result is None
