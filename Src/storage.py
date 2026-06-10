import json
import os


class Data_base:
    def __init__(self,file_path:str ="Data/db.json"):
        
        
        self.file_path = file_path
        self.Folder_maker()


    def Folder_maker(self):

        Directory = os.path.dirname(self.file_path)

        if Directory and not os.path.exists(Directory):
            os.makedirs(Directory)
    def data_save(self,data):
        self.Folder_maker()

        with open (self.file_path,"w") as file:
            json.dump(data,file, indent=3) 
    def load_data(self):
        if not os.path.exists(self.File_path):
            return []

        with open(self.File_path ,"r")as file : 
            return json.load (file)    

    def data_append(self, new_item):
    
        current_data = self.load_data()
        
    
        current_data.append(new_item)
        

        self.data_save(current_data)


























    


