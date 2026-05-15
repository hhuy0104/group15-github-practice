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
