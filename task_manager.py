import pymongo
from datetime import datetime, date
from bson import ObjectId

# MongoDB Connection
from db_config import get_mongo_client

# Base Task Class
class Task:
    def __init__(self, title, description, due_date):
        self._title = title
        self._description = description
        # Ensure due_date is a datetime object
        if isinstance(due_date, date) and not isinstance(due_date, datetime):
            self._due_date = datetime.combine(due_date, datetime.min.time())
        else:
            self._due_date = due_date

    def to_dict(self):
        return {
            "title": self._title,
            "description": self._description,
            "due_date": self._due_date
        }

# Personal Task (inherits from Task)
class PersonalTask(Task):
    def __init__(self, title, description, due_date):
        super().__init__(title, description, due_date)

# Work Task (inherits from Task)
class WorkTask(Task):
    def __init__(self, title, description, due_date):
        super().__init__(title, description, due_date)

# TaskManager to handle operations
class TaskManager:
    def __init__(self):
        self.client = get_mongo_client()
        self.db = self.client["task_db"]
        self.collection = self.db["tasks"]

    def add_task(self, task_type, title, description, due_date):
        if task_type == "personal":
            task = PersonalTask(title, description, due_date)
        else:
            task = WorkTask(title, description, due_date)
        
        task_dict = task.to_dict()
        task_dict["task_type"] = task_type
        self.collection.insert_one(task_dict)

    def get_all_tasks(self):
        return list(self.collection.find())

    def delete_task(self, task_id):
        self.collection.delete_one({"_id": ObjectId(task_id)})
