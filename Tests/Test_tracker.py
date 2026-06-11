import os
import pytest
from storage import Data_base
from models import Expense, Income

# Define a temporary path for the test database to avoid overwriting your real data
TEST_DB_PATH = "Data/test_db.json"

@pytest.fixture(autouse=True)
def setup_and_teardown():
    """
    This runs before and after EVERY single test automatically.
    It ensures each test starts with a completely clean, empty JSON file.
    """
    # Clean up before test runs
    if os.path.exists(TEST_DB_PATH):
        os.remove(TEST_DB_PATH)
        
    yield  # This is where the actual test function executes
    
    # Clean up after test finishes
    if os.path.exists(TEST_DB_PATH):
        os.remove(TEST_DB_PATH)


# =====================================================================
# 1. TESTING MODELS.PY (OOP Structures)
# =====================================================================

def test_expense_class_serialization():
    # Rule 2: The 3A's
    # Arrange
    amt, cat, desc = 50.0, "Food", "Dinner"
    
    # Act
    exp_obj = Expense(amt, cat, desc)
    serialized_data = exp_obj.To_dic()
    
    # Assert
    assert serialized_data["Amount"] == 50.0
    assert serialized_data["category"] == "Food"
    assert serialized_data["Description"] == "Dinner"
    assert serialized_data["type"] == "Expense"
    assert "date" in serialized_data


def test_income_class_serialization():
    # Arrange & Act
    inc_obj = Income(2000.0, "Salary", "Monthly pay")
    serialized_data = inc_obj.To_dic()
    
    # Assert
    assert serialized_data["Amount"] == 2000.0
    assert serialized_data["type"] == "Income "  # Matching your model's trailing space string


# =====================================================================
# 2. TESTING STORAGE.PY (Database Management)
# =====================================================================

def test_database_initialization_creates_empty_list():
    # Arrange & Act
    db = Data_base(TEST_DB_PATH)
    
    # Assert
    assert os.path.exists(TEST_DB_PATH)
    assert db.load_data() == []


def test_data_append_saves_properly():
    # Arrange
    db = Data_base(TEST_DB_PATH)
    mock_expense = {
        "type": "Expense", 
        "Amount": 15.50, 
        "category": "Coffee", 
        "Description": "Latte", 
        "date": "2026-06-11 12:00:00"
    }
    
    # Act
    db.data_append(mock_expense)
    loaded_data = db.load_data()
    
    # Assert
    assert len(loaded_data) == 1
    assert loaded_data[0]["Amount"] == 15.50
    assert loaded_data[0]["category"] == "Coffee"


def test_data_delete_with_valid_index():
    # Arrange
    db = Data_base(TEST_DB_PATH)
    item_1 = {"type": "Income", "Amount": 100.0}
    item_2 = {"type": "Expense", "Amount": 20.0}
    db.data_append(item_1)
    db.data_append(item_2)
    
    # Act
    # Delete the first item (index 0)
    deleted_item = db.data_delete(0)
    remaining_data = db.load_data()
    
    # Assert
    assert deleted_item["Amount"] == 100.0  # Asserts it returned the popped item
    assert len(remaining_data) == 1        # Asserts only 1 item remains
    assert remaining_data[0]["Amount"] == 20.0  # Asserts index 1 shifted down to index 0


def test_data_delete_with_invalid_index_returns_none():
    # Arrange
    db = Data_base(TEST_DB_PATH)
    db.data_append({"type": "Expense", "Amount": 10.0})
    
    # Act
    deleted_item = db.data_delete(99)  # Non-existent index
    
    # Assert
    assert deleted_item is None