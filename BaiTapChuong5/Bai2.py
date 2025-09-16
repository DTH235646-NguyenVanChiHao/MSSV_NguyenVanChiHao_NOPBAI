def ToiUuChuoi(s): 
    s2 = s 
    s2 = s2.strip()              # bỏ khoảng trắng đầu và cuối
    arr = s2.split(' ')          # tách theo khoảng trắng
    s2 = "" 
    for x in arr: 
        word = x 
        if len(word.strip()) != 0:   # bỏ từ rỗng
            s2 = s2 + word + " "     # nối lại, thêm 1 khoảng trắng
    return s2.strip()                # bỏ khoảng trắng cuối cùng
 
s = "    Trần     Duy     Thanh   "
print(s, "=>", len(s))
s = ToiUuChuoi(s)
print(s, "=>", len(s))
