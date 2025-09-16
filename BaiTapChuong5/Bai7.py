def ToiUuChuoiDanhTu(s):
    # Bước 1: bỏ khoảng trắng dư thừa, tách thành các từ
    words = s.strip().split()
    
    # Bước 2: viết thường toàn bộ rồi viết hoa chữ cái đầu
    words = [w.lower().capitalize() for w in words]
    
    # Bước 3: ghép lại thành chuỗi tối ưu
    return " ".join(words)


# --- Chạy thử ---
s = "    TRần    duY   ThANh   "
print("Input :", repr(s))
print("Output:", ToiUuChuoiDanhTu(s))
