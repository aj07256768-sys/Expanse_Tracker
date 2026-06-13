import json
import os

class Data_base:
    def __init__(self, file_path):
        self.file_path = file_path
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
        if not os.path.exists(self.file_path):
            self.data_save([])

    def load_data(self):
        try:
            with open(self.file_path, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def data_save(self, data):
        with open(self.file_path, "w") as file:
            json.dump(data, file, indent=4)

    def data_append(self, new_item):
        current_data = self.load_data()
        current_data.append(new_item)
        self.data_save(current_data)

    def data_delete(self, index: int):
        current_data = self.load_data()
    
        if 0 <= index < len(current_data):
            removed_item = current_data.pop(index) 
            self.data_save(current_data)           
            return removed_item
        return None

    def data_update(self, index: int, updated_fields: dict):
        current_data = self.load_data()
        
        if 0 <= index < len(current_data):
            # Update only the fields that the user actually passed in
            for key, value in updated_fields.items():
                if value is not None:
                    current_data[index][key] = value
            
            self.data_save(current_data)
            return current_data[index]
        return None