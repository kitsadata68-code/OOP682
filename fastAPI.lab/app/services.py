# app/services.py

from .repositories import ITaskRepository
from .models import Task, TaskCreate
from typing import Optional, List

class TaskService:
    def __init__(self, repo: ITaskRepository):
        self.repo = repo

    # Logic ส่วนที่ 1: ดึงข้อมูล
    def get_tasks(self) -> List[Task]:
        return self.repo.get_all()

    # Logic ส่วนที่ 2: สร้างงาน
    def create_task(self, task_in: TaskCreate) -> Task:
        return self.repo.create(task_in)

    # Logic ส่วนที่ 3: ทำเครื่องหมายว่าเสร็จ (โจทย์ข้อนี้)
    def mark_as_complete(self, task_id: int) -> Optional[Task]:
        # สั่ง Repository ให้อัปเดตสถานะเป็น True
        return self.repo.update(task_id, True)