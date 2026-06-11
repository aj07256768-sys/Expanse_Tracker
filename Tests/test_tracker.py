import os
import pytest
from Src.storage import Data_base
from Src.models import Expense, Income

TEST_DB_PATH = "Data/test_db.json"

@pytest.fixture(autouse=True)
def setup_and_teardown():
    if os.path.exists(TEST_DB_PATH):
        os.remove(TEST_DB_PATH)
        
    yield
    
    if os.path.exists(TEST_DB_PATH):
        os.remove(TEST_DB_PATH)


def test_expense_class_serialization():
    amt, cat, desc = 50.0, "Food", "Dinner"
    
    exp_obj = Expense(amt, cat, desc)
    serialized_data = exp_obj.To_dic()
    
    assert serialized_data["Amount"] == 50.0
    assert serialized_data["category"] == "Food"
    assert serialized_data["Description"] == "Dinner"
    assert serialized_data["type"] == "Expense"
    assert "date" in serialized_data


def test_income_class_serialization():
    inc_obj = Income(2000.0, "Salary", "Monthly pay")
    serialized_data = inc_obj.To_dic()
    
    assert serialized_data["Amount"] == 2000.0
    assert serialized_data["type"] == "Income "


def test_database_initialization_creates_empty_list():
    db = Data_base(TEST_DB_PATH)
    
    assert os.path.exists(TEST_DB_PATH)
    assert db.load_data() == []


def test_data_append_saves_properly():
    db = Data_base(TEST_DB_PATH)
    mock_expense = {
        "type": "Expense", 
        "Amount": 15.50, 
        "category": "Coffee", 
        "Description": "Latte", 
        "date": "2026-06-11 12:00:00"
    }
    
    db.data_append(mock_expense)
    loaded_data = db.load_data()
    
    assert len(loaded_data) == 1
    assert loaded_data[0]["Amount"] == 15.50
    assert loaded_data[0]["category"] == "Coffee"


def test_data_delete_with_valid_index():
    db = Data_base(TEST_DB_PATH)
    item_1 = {"type": "Income", "Amount": 100.0}
    item_2 = {"type": "Expense", "Amount": 20.0}
    db.data_append(item_1)
    db.data_append(item_2)
    
    deleted_item = db.data_delete(0)
    remaining_data = db.load_data()
    
    assert deleted_item["Amount"] == 100.0
    assert len(remaining_data) == 1
    assert remaining_data[0]["Amount"] == 20.0


def test_data_delete_with_invalid_index_returns_none():
    db = Data_base(TEST_DB_PATH)
    db.data_append({"type": "Expense", "Amount": 10.0})
    
    deleted_item = db.data_delete(99)
    
    assert deleted_item is None