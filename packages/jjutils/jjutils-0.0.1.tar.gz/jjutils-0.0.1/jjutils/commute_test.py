"""
Unit tests for the commute module.
"""

import json
from unittest import mock

import pytest
from commute import calc_route, validate_address


def test_valid_inputs():
    """
    Test calculation with valid input addresses.
    """
    with mock.patch(
        "WazeRouteCalculator.WazeRouteCalculator.calc_route_info"
    ) as mock_calc:
        mock_calc.return_value = (20, 10)
        result = calc_route("A", "B", "US", False)
        assert json.loads(result) == {"result": {"minutes": 20, "km": 10}}


def test_validate_address():
    """
    Test validation of addresses.
    """
    with pytest.raises(ValueError):
        validate_address(None)
    with pytest.raises(ValueError):
        validate_address("")
    assert validate_address("Valid Address") is True


def test_invalid_address():
    """
    Test calculation with invalid input addresses.
    """
    result = calc_route("", "", "US", False)
    assert json.loads(result) == {"error": "Value error", "distance": 0, "time": 0}


def test_real_time():
    """
    Test calculation with real-time data flag enabled.
    """
    with mock.patch(
        "WazeRouteCalculator.WazeRouteCalculator.calc_route_info"
    ) as mock_calc:
        mock_calc.return_value = (15, 10)
        result = calc_route("A", "B", "US", True)
        assert json.loads(result) == {"result": {"minutes": 15, "km": 10}}


def test_connection_error():
    """
    Test calculation when a ConnectionError occurs.
    """
    with mock.patch(
        "WazeRouteCalculator.WazeRouteCalculator.calc_route_info"
    ) as mock_calc:
        mock_calc.side_effect = ConnectionError
        result = calc_route("A", "B", "US", False)
        assert json.loads(result) == {
            "error": "Connection error",
            "distance": 0,
            "time": 0,
        }


def test_timeout_error():
    """
    Test calculation when a TimeoutError occurs.
    """
    with mock.patch(
        "WazeRouteCalculator.WazeRouteCalculator.calc_route_info"
    ) as mock_calc:
        mock_calc.side_effect = TimeoutError
        result = calc_route("A", "B", "US", False)
        assert json.loads(result) == {
            "error": "Timeout error",
            "distance": 0,
            "time": 0,
        }
