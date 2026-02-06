from abc import ABC, abstractmethod
from typing import List, Optional
from .models import Task, TaskCreate

class ITaskRepository(ABC):
    def update(self, task_id: int, completed: bool) -> Optional[Task]:
        raise NotImplementedError

class InMemoryTaskRepository(ITaskRepository):
    # ... __init__, get_all, create เดิม ...

    # เพิ่ม function นี้ต่อท้ายสุด
    @abstractmethod
    def update_task_complete(self, task_id: int, completed: bool) -> Optional[Task]:
        pass
    
    @abstractmethod
    def get_all(self) -> List[Task]:
        pass

    @abstractmethod
    def create(self, task: TaskCreate) -> Task:
        pass
        
    @abstractmethod
    def get_by_id(self, task_id: int) -> Optional[Task]:
        pass

# ต้องชื่อเหมือนกันเป๊ะๆ
class InMemoryTaskRepository(ITaskRepository):  
    # code...
    def __init__(self):
            self.tasks = []
            self.current_id = 1

    def get_all(self) -> List[Task]:
        return self.tasks

    def create(self, task_in: TaskCreate) -> Task:
        task = Task(
            id=self.current_id,
            **task_in.dict()
        )
        self.tasks.append(task)
        self.current_id += 1
        return task
    
    def update_task_complete(self, task_id: int, completed: bool) -> Optional[Task]:
        db_task = self.get_by_id(task_id)
        if db_task:
            db_task.completed = completed
            return db_task
        return None

    def get_by_id(self, task_id: int) -> Optional[Task]:
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

# app/repositories.py (เพิ่มต่อท้าย)
from sqlalchemy.orm import Session
from . import models_orm # ต้องสร้าง SQLAlchemy Model แยก

class SqlTaskRepository(ITaskRepository):
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> List[Task]:
        return self.db.query(models_orm.Task).all()

    def create(self, task_in: TaskCreate) -> Task:
        db_task = models_orm.Task(**task_in.dict())
        self.db.add(db_task)
        self.db.commit()
        self.db.refresh(db_task)
        return db_task
    
    def get_by_id(self, id: int):
        # ... implementation ...
        pass
