"""
Get economic indicator from FRED
"""

import argparse
import datetime
import json
import logging

import pandas_datareader.data as web

# Initialize logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def get_indicator(series, start_year, end_year):
    """
    Get economic indicator from FRED
    """
    try:
        start = datetime.datetime(start_year, 1, 1)
        end = datetime.datetime(end_year, 12, 31)
        indicator = web.DataReader(series, "fred", start, end)
        return indicator
    except NotImplementedError as error:
        logger.error(
            "The method is not implemented for series %s. NotImplementedError: %s",
            series,
            error,
        )
    except Exception as error:  # General catch-all, but consider limiting this
        if "Unable to read URL" in str(error):
            logger.error(
                "The URL could not be read for series %s. Error: %s", series, error
            )
        else:
            logger.error("Failed to get data for series %s. Error: %s", series, error)
    return None


def main(indicator, start_year, end_year):
    """Main function"""
    # Initialize an empty dictionary to store the JSON structure
    data_json = {}

    mydata = get_indicator(indicator, start_year, end_year)

    if mydata is not None:
        # Convert DataFrame values to list and add to dictionary
        data_json[indicator] = mydata[indicator].tolist()

    # Convert the entire dictionary to a JSON string for return
    data_json_str = json.dumps(data_json, indent=4)

    return data_json_str


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Collects a specified economic indicator."
    )
    parser.add_argument(
        "--indicator",
        type=str,
        required=True,
        help="Economic indicator to fetch (e.g., AWHMAN, IC4WSA, etc.)",
    )
    parser.add_argument(
        "--start-year", type=int, default=1996, help="Start year for data collection"
    )
    parser.add_argument(
        "--end-year", type=int, default=2018, help="End year for data collection"
    )

    args = parser.parse_args()

    data = main(args.indicator, args.start_year, args.end_year)
    logger.info("Fetched data: %s", data)
