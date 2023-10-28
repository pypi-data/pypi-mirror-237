""" Tests for the JSONFileCRUD class."""

import json
import os

import pytest
from crud_json import (
    JSONFileCRUD,
)  # Replace with the actual module name where JSONFileCRUD is defined


@pytest.fixture
def setup_json_file():
    """Setup and teardown for JSON file."""
    test_file_name = "test.json"
    yield test_file_name
    if os.path.exists(test_file_name):
        os.remove(test_file_name)


def test_json_file_init(setup_json_file):
    """Test the initialization of the JSON file."""
    crud_instance = JSONFileCRUD(setup_json_file)
    assert os.path.exists(setup_json_file)


def test_create(setup_json_file):
    """Test the creation of a record in the JSON file."""
    crud_instance = JSONFileCRUD(setup_json_file)
    test_data = {"key": "value"}
    crud_instance.create(test_data)

    with open(setup_json_file, "r", encoding="utf-8") as file:
        data = json.load(file)
    assert data == [test_data]


def test_read(setup_json_file):
    """Test the reading of all records from the JSON file."""
    crud_instance = JSONFileCRUD(setup_json_file)
    test_data = {"key": "value"}
    crud_instance.create(test_data)

    read_data = crud_instance.read()
    assert read_data == [test_data]


def test_update(setup_json_file):
    """Test the updating of a record in the JSON file."""
    crud_instance = JSONFileCRUD(setup_json_file)
    test_data = {"key": "value"}
    updated_data = {"key": "new_value"}

    crud_instance.create(test_data)
    crud_instance.update(0, updated_data)

    read_data = crud_instance.read()
    assert read_data == [updated_data]


def test_delete(setup_json_file):
    """Test the deletion of a record from the JSON file."""
    crud_instance = JSONFileCRUD(setup_json_file)
    test_data = {"key": "value"}

    crud_instance.create(test_data)
    crud_instance.delete(0)

    read_data = crud_instance.read()
    assert read_data == []
