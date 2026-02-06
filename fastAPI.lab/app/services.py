from .repositories import ITaskRepository
from .models import Task, TaskCreate
from typing import Optional, List
from fastapi import HTTPException # <--- ต้อง import ตัวนี้มาใช้สำหรับแจ้ง Error

class TaskService:
    def __init__(self, repo: ITaskRepository):
        self.repo = repo

    # Logic ส่วนที่ 1: ดึงข้อมูล
    def get_tasks(self) -> List[Task]:
        return self.repo.get_all()

    # Logic ส่วนที่ 2: สร้างงาน (ต้องมี Validation เช็คชื่อซ้ำ!)
    def create_task(self, task_in: TaskCreate) -> Task:
        # 1. เช็คก่อนว่าชื่อนี้มีใน DB ไหม
        existing_task = self.repo.get_by_title(task_in.title)
        
        # 2. ถ้ามีอยู่แล้ว ให้ Error ทันที (400 Bad Request)
        if existing_task:
            raise HTTPException(status_code=400, detail="Task with this title already exists")
        
        # 3. ถ้าไม่ซ้ำ ค่อยสร้าง
        return self.repo.create(task_in)

    # Logic ส่วนที่ 3: ทำเครื่องหมายว่าเสร็จ
    def mark_as_complete(self, task_id: int) -> Optional[Task]:
        # สั่ง Repository ให้อัปเดตสถานะเป็น True (ส่วนนี้คุณเขียนถูกแล้วครับ)
        return self.repo.update(task_id, True)