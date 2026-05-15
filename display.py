from utils import get_summary

class Display:

    @staticmethod
    def show_all(tasks, title="Danh sách task"):
        """In toàn bộ danh sách task ra màn hình."""
        print(f"\n{'─'*40}")
        print(f"  {title}")
        print(f"{'─'*40}")

        if not tasks:
            print("  (Không có task nào)")
        else:
            for i, task in enumerate(tasks, start=1):
                icon   = "✔" if task.is_done() else "○"
                status = "Hoàn thành" if task.is_done() else "Chưa xong"
                print(f"  {i}. [{icon}] {task.title}")
                if task.description:
                    print(f"       Mô tả : {task.description}")
                print(f"       Trạng thái : {status}  |  Tạo lúc: {task.created_at}")

        Display.show_summary(tasks)
        print(f"{'─'*40}")

    @staticmethod
    def show_summary(tasks):
        """In dòng thống kê tổng hợp."""
        summary = get_summary(tasks)
        print(f"\n  Tổng: {summary['total']}  |  "
              f"Hoàn thành: {summary['done']}  |  "
              f"Chưa xong: {summary['pending']}")

    @staticmethod
    def show_task_detail(task, index):
        """In chi tiết 1 task."""
        print(f"\n{'─'*40}")
        print(f"  Chi tiết task #{index}")
        print(f"{'─'*40}")
        print(f"  Tên       : {task.title}")
        print(f"  Mô tả     : {task.description or '(Không có)'}")
        print(f"  Trạng thái: {'Hoàn thành ✔' if task.is_done() else 'Chưa xong ○'}")
        print(f"  Tạo lúc   : {task.created_at}")
        print(f"{'─'*40}")
