"""
This module is a crud class for a json file.
"""


import json
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


class JSONFileCRUD:
    """A class to handle basic CRUD operations on a JSON file."""

    def __init__(self, file_name):
        self.file_name = file_name
        try:
            with open(self.file_name, "w", encoding="utf-8") as file:
                json.dump([], file)
            logger.info("Successfully initialized JSON file: %s", self.file_name)
        except IOError:
            logger.exception("Failed to initialize JSON file: %s", self.file_name)

    def create(self, data):
        """
        Create a new record in the JSON file."""
        try:
            with open(self.file_name, "x", encoding="utf-8") as file:
                pass
        except FileExistsError:
            pass

        try:
            with open(self.file_name, "r", encoding="utf-8") as file:
                data_list = json.load(file)
                data_list.append(data)
            with open(self.file_name, "w", encoding="utf-8") as file:
                json.dump(data_list, file)
            logger.info("Data added: %s", data)
        except (IOError, json.JSONDecodeError):
            logger.exception("Failed to add data: %s", data)

    def read(self):
        """Read all records from the JSON file."""
        try:
            with open(self.file_name, "r", encoding="utf-8") as file:
                data = json.load(file)
                logger.info("Data read: %s", data)
                return data
        except (IOError, json.JSONDecodeError):
            logger.exception("Failed to read data")
            return []

    def update(self, index, data):
        """Update a record in the JSON file."""
        try:
            data_list = self.read()
            data_list[index] = data
            with open(self.file_name, "w", encoding="utf-8") as file:
                json.dump(data_list, file)
            logger.info("Data updated at index %d: %s", index, data)
        except (IndexError, IOError, json.JSONDecodeError):
            logger.exception("Failed to update data at index %d", index)

    def delete(self, index):
        """Delete a record from the JSON file."""
        try:
            data_list = self.read()
            data_list.pop(index)
            with open(self.file_name, "w", encoding="utf-8") as file:
                json.dump(data_list, file)
            logger.info("Data deleted at index %d", index)
        except (IndexError, IOError, json.JSONDecodeError):
            logger.exception("Failed to delete data at index %d", index)
