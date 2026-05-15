from task import TaskManager
from display import Display
from utils import search_tasks, filter_by_status

def main():
    manager = TaskManager()
    
    while True:
        print("\n========== TO-DO LIST ==========")
        print("1. Thêm task mới")
        print("2. Hiển thị tất cả task")
        print("3. Tìm kiếm task")
        print("4. Lọc task theo trạng thái")
        print("5. Đánh dấu hoàn thành")
        print("6. Xóa task")

        # Các thành viên dễ sửa cùng chỗ này -> dễ tạo merge conflict
        print("7. Thống kê task")
        print("8. Export task ra file")

        print("0. Thoát")
        print("================================")

        # TODO: thêm chức năng đồng bộ cloud trong tương lai
        
        choice = input("Chọn chức năng: ").strip()
        
        if choice == "1":
            title = input("Nhập tên task: ").strip()
            desc  = input("Nhập mô tả (Enter để bỏ qua): ").strip()
            if title:
                manager.add_task(title, desc)
                print("✔ Thêm task thành công!")
            else:
                print("✘ Tên task không được để trống.")

        elif choice == "2":
            Display.show_all(manager.get_all_tasks())

        elif choice == "3":
            keyword = input("Nhập từ khóa tìm kiếm: ").strip()
            results = search_tasks(manager.get_all_tasks(), keyword)
            Display.show_all(results, title=f'Kết quả tìm kiếm: "{keyword}"')

        elif choice == "4":
            print("Trạng thái: 1-Chưa xong  2-Hoàn thành")
            s = input("Chọn: ").strip()
            status = "done" if s == "2" else "pending"
            results = filter_by_status(manager.get_all_tasks(), status)
            Display.show_all(results, title=f"Lọc: {'Hoàn thành' if status == 'done' else 'Chưa xong'}")

        elif choice == "5":
            Display.show_all(manager.get_all_tasks())
            try:
                idx = int(input("Nhập số thứ tự task cần đánh dấu: ")) - 1
                manager.mark_done(idx)
                print("✔ Đã đánh dấu hoàn thành!")
            except (ValueError, IndexError):
                print("✘ Số thứ tự không hợp lệ.")

        elif choice == "6":
            Display.show_all(manager.get_all_tasks())
            try:
                idx = int(input("Nhập số thứ tự task cần xóa: ")) - 1
                manager.delete_task(idx)
                print("✔ Đã xóa task!")
            except (ValueError, IndexError):
                print("✘ Số thứ tự không hợp lệ.")

        elif choice == "7":
            print("Chức năng đang phát triển...")
        elif choice == "0":
            print("Tạm biệt!")
            break
        else:
            print("✘ Lựa chọn không hợp lệ, vui lòng thử lại.")

if __name__ == "__main__":
    main()
