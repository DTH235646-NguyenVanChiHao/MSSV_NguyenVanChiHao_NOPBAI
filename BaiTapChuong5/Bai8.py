
#Find more about regrex : https://docs.python.org/3/library/re.html
#find email , phone number , url in a text
#Find file name and file name without extension from a path 

def get_filename(path):
    # Tách theo dấu \ hoặc /
    return path.split("\\")[-1].split("/")[-1]

def get_filename_no_ext(path):
    filename = get_filename(path)
    # Tìm dấu chấm cuối cùng
    dot_index = filename.rfind(".")
    if dot_index != -1:
        return filename[:dot_index]
    return filename  # nếu không có đuôi file

# --- Chạy thử ---
path = "d:\\music\\muabui.mp3"
print("Đường dẫn:", path)
print("Tên file  :", get_filename(path))
print("Không đuôi:", get_filename_no_ext(path))
