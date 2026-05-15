from datetime import datetime

class Task:
    def __init__(self, title, description=""):
        self.title       = title
        self.description = description
        self.status      = "pending"   # pending | done
        self.created_at  = datetime.now().strftime("%d/%m/%Y %H:%M")

    def mark_done(self):
        self.status = "done"

    def is_done(self):
        return self.status == "done"

    def __str__(self):
        icon = "✔" if self.is_done() else "○"
        return f"[{icon}] {self.title} ({self.status}) - {self.created_at}"


class TaskManager:
    def __init__(self):
        self._tasks = []

    # ── Thêm task ──────────────────────────────────────────────
    def add_task(self, title, description=""):
        task = Task(title, description)
        self._tasks.append(task)
        return task

    # ── Xóa task theo index ────────────────────────────────────
    def delete_task(self, index):
        if 0 <= index < len(self._tasks):
            return self._tasks.pop(index)
        raise IndexError("Index ngoài phạm vi danh sách.")

    # ── Đánh dấu hoàn thành ────────────────────────────────────
    def mark_done(self, index):
        if 0 <= index < len(self._tasks):
            self._tasks[index].mark_done()
        else:
            raise IndexError("Index ngoài phạm vi danh sách.")

    # ── Lấy toàn bộ task ───────────────────────────────────────
    def get_all_tasks(self):
        return list(self._tasks)

    # ── Tổng số task ───────────────────────────────────────────
    def count(self):
        return len(self._tasks)

        # ── Lấy task theo trạng thái ──────────────────────────────
    def get_tasks_by_status(self, status):
        return [task for task in self._tasks if task.status == status]

    # ── Lấy tất cả task đã hoàn thành ─────────────────────────
    def get_completed_tasks(self):
        return [task for task in self._tasks if task.is_done()]

    # ── Lấy tất cả task chưa hoàn thành ───────────────────────
    def get_pending_tasks(self):
        return [task for task in self._tasks if not task.is_done()]

    # ── Tìm task theo từ khóa ─────────────────────────────────
    def search_tasks(self, keyword):
        keyword = keyword.lower()
        return [
            task for task in self._tasks
            if keyword in task.title.lower()
            or keyword in task.description.lower()
        ]

    # ── Cập nhật title task ───────────────────────────────────
    def update_task_title(self, index, new_title):
        if 0 <= index < len(self._tasks):
            self._tasks[index].title = new_title
        else:
            raise IndexError("Index ngoài phạm vi danh sách.")

    # ── Cập nhật description task ─────────────────────────────
    def update_task_description(self, index, new_description):
        if 0 <= index < len(self._tasks):
            self._tasks[index].description = new_description
        else:
            raise IndexError("Index ngoài phạm vi danh sách.")

    # ── Xóa toàn bộ task ──────────────────────────────────────
    def clear_all_tasks(self):
        self._tasks.clear()

    # ── Kiểm tra danh sách rỗng ───────────────────────────────
    def is_empty(self):
        return len(self._tasks) == 0

    # ── Lấy task theo index ───────────────────────────────────
    def get_task(self, index):
        if 0 <= index < len(self._tasks):
            return self._tasks[index]
        raise IndexError("Index ngoài phạm vi danh sách.")

    # ── Thống kê task ─────────────────────────────────────────
    def statistics(self):
        done = len(self.get_completed_tasks())
        pending = len(self.get_pending_tasks())

        return {
            "total": self.count(),
            "done": done,
            "pending": pending
        }