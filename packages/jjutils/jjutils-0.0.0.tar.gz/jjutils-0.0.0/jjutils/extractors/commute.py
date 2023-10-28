"""
This script calculates the miles and average commute times between two addresses
"""

import argparse
import json
import logging

import WazeRouteCalculator

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def validate_address(address):
    """
    Validates address
    """
    if not address:
        raise ValueError("Address cannot be empty or None")
    return True


def calc_route(to_address, from_address, region="US", real_time=False):
    """
    Calculates commute time between two locations
    """
    commutes = {}  # Initialize as an empty dictionary

    try:
        validate_address(to_address)
        validate_address(from_address)

        route = WazeRouteCalculator.WazeRouteCalculator(
            from_address, to_address, region
        )

        logger.info(
            "Calculating route from %s to %s in region %s using real_time=%s",
            from_address,
            to_address,
            region,
            real_time,
        )

        commutes["result"] = {
            "minutes": route.calc_route_info(real_time=real_time)[0],
            "km": route.calc_route_info(real_time=real_time)[1],
        }
    except ValueError as value_err:
        logger.error("Value error: %s", value_err)
        commutes["error"] = "Value error"
        commutes["distance"] = 0
        commutes["time"] = 0

    except ConnectionError:
        logger.error("Connection error occurred while trying to reach the API.")
        commutes["error"] = "Connection error"
        commutes["distance"] = 0
        commutes["time"] = 0

    except TimeoutError:
        logger.error("Timeout error occurred while trying to reach the API.")
        commutes["error"] = "Timeout error"
        commutes["distance"] = 0
        commutes["time"] = 0

    # Optionally, keep the general exception if you absolutely must
    except Exception as gen_except:
        logger.error("An unexpected error occurred: %s", gen_except)
        commutes["error"] = "An unexpected error occurred"
        commutes["distance"] = 0
        commutes["time"] = 0

    return json.dumps(commutes)


def main():
    """
    Main function for script execution
    """
    parser = argparse.ArgumentParser(
        description="Calculates the miles and average commute times between two addresses"
    )
    parser.add_argument("to_address", type=str, help="Destination address")
    parser.add_argument("from_address", type=str, help="Source address")
    parser.add_argument(
        "--region", type=str, default="US", help="Region (default is US)"
    )
    parser.add_argument(
        "--real_time", action="store_true", help="Whether to use real-time data"
    )

    args = parser.parse_args()

    commute = calc_route(
        to_address=args.to_address,
        from_address=args.from_address,
        region=args.region,
        real_time=args.real_time,
    )

    logger.info("Finished calculating route.")
    print(commute)


if __name__ == "__main__":
    main()
