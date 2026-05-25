# input: nhập số lượng phiếu và 4 dữ liệu của từng phiếu
# output: in phiếu hợp lệ, nếu ko, thông báo ra lỗi
# cách làm
# B1: Nhập số lượng phiếu n
# B2: Nếu n <= 0 -> báo lỗi và kết thúc
# B3: Lặp n lần:
#     Nhập chuỗi đăng ký
#     Tách chuỗi theo "|"
#     Nếu không đủ 4 phần -> báo lỗi, bỏ qua
#     Chuẩn hóa
#     Kiểm tra:
#         Nếu email không có "@": báo lỗi, bỏ qua
#         Nếu len(student_id) < 5: báo lỗi, bỏ qua
#     In thông tin chuẩn hóa
#     Tạo mã xác nhận

quantity_input = input("Enter the number of registration forms: ")

if not quantity_input.isdigit() or int(quantity_input) <= 0:
    print("Số lượng phiếu đăng ký không hợp lệ")
else:
    total_forms = int(quantity_input)

    for i in range(total_forms):
        raw_entry = input("Input (Họ tên học viên | Tên khóa học | Mã học viên | Email): ")
        
        if raw_entry.count('|') != 3:
            print("Dữ liệu đăng ký không hợp lệ. Bỏ qua phiếu này")
            continue

        name_raw, course_raw, id_raw, email_raw = raw_entry.split('|')

        student_id = id_raw.strip().upper()
        if len(student_id) < 5:
            print("Mã học viên không hợp lệ. Bỏ qua phiếu này")
            continue
        
        email_addr = email_raw.strip().lower()
        if '@' not in email_addr:
            print("Email không hợp lệ. Bỏ qua phiếu này")
            continue

        full_name = name_raw.strip().title()
        course_name = course_raw.strip().title()
        
        formatted_course = course_name.upper().replace(" ", "-")
        confirmation_code = f"{student_id}_{formatted_course}"

        print("\n===== PHIẾU ĐĂNG KÝ ĐÃ CHUẨN HÓA =====")
        print("Học viên:", full_name)
        print("Khóa học:", course_name)
        print("Mã học viên:", student_id)
        print("Email:", email_addr)
        print("Mã xác nhận:", confirmation_code)
