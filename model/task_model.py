import os
import sys
import base64
import datetime
import config.mongo_connection as con
from pymongo.collection import Collection

class Task(Collection):
    def __init__(self, db):
        super().__init__(db, "task")

    def create_task(self, title: str, description: str, creat_date: datetime, end_date: datetime, author: str):
        creat_date = datetime.datetime.now()
        end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d %H:%M:%S')
    
        task = {
                    "title": title,
                    "description": description,
                    "creat_date": creat_date,
                    "end_date": end_date,
                    "author": author
                }
        
        self.insert_one(task)