# Chương trình máy tính đơn giản
# Dành cho học sinh cấp 3 (lớp 9-12)

def hien_thi_menu():
    """Hiển thị menu các phép tính cho người dùng."""
    print("\n=== CHƯƠNG TRÌNH MÁY TÍNH ĐƠN GIẢN ===")
    print("1. Phép cộng (+)")
    print("2. Phép trừ (-)")
    print("3. Phép nhân (×)")
    print("4. Phép chia (÷)")
    print("5. Thoát chương trình")

def nhap_so(thu_tu):
    """Hàm nhập và kiểm tra số hợp lệ.
    
    Args:
        thu_tu: Thứ tự của số cần nhập ("thứ nhất" hoặc "thứ hai")
    
    Returns:
        float: Số đã nhập nếu hợp lệ
    """
    while True:
        try:
            so = float(input(f"\nNhập số {thu_tu}: "))
            return so
        except ValueError:
            print("Lỗi: Vui lòng nhập một số hợp lệ!")

def thuc_hien_phep_tinh(so1, so2, lua_chon):
    """Thực hiện phép tính dựa trên lựa chọn của người dùng.
    
    Args:
        so1: Số thứ nhất
        so2: Số thứ hai
        lua_chon: Lựa chọn phép tính (1-4)
    
    Returns:
        tuple: (Kết quả phép tính, Ký hiệu phép tính)
    """
    if lua_chon == 1:
        return (so1 + so2, "+")
    elif lua_chon == 2:
        return (so1 - so2, "-")
    elif lua_chon == 3:
        return (so1 * so2, "×")
    elif lua_chon == 4:
        if so2 == 0:
            raise ZeroDivisionError("Không thể chia cho số 0!")
        return (so1 / so2, "÷")

def main():
    """Hàm chính của chương trình."""
    while True:
        # Hiển thị menu
        hien_thi_menu()
        
        # Nhập lựa chọn từ người dùng
        try:
            lua_chon = int(input("\nNhập lựa chọn của bạn (1-5): "))
            
            # Kiểm tra thoát chương trình
            if lua_chon == 5:
                print("\nCảm ơn bạn đã sử dụng chương trình!")
                break
            
            # Kiểm tra lựa chọn hợp lệ
            if lua_chon not in [1, 2, 3, 4]:
                print("Lỗi: Vui lòng chọn số từ 1 đến 5!")
                continue
            
            # Nhập hai số
            so1 = nhap_so("thứ nhất")
            so2 = nhap_so("thứ hai")
            
            # Thực hiện phép tính
            ket_qua, ky_hieu = thuc_hien_phep_tinh(so1, so2, lua_chon)
            
            # Hiển thị kết quả
            print(f"\nKết quả: {so1} {ky_hieu} {so2} = {ket_qua}")
            
        except ValueError:
            print("Lỗi: Vui lòng nhập một số nguyên từ 1 đến 5!")
        except ZeroDivisionError as e:
            print(f"Lỗi: {e}")

# Chạy chương trình
if __name__ == "__main__":
    main()