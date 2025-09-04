# toan=float(input("Nhập điểm Toán:")) 
# ly=float(input("Nhập điểm lý:")) 
# hoa=float(input("Nhập điểm hóa:")) 
# dtb=(toan+ly+hoa)/3 
# print("Điểm trung bình=",dtb) 
# print("Điểm trung bình=",round(dtb,2)) 

print("Chương trình tính điểm trung bình") 

#What is eval?
# eval() function evaluates the specified expression, if the expression is a legal Python statement, it will be executed.
# If the expression is a legal Python expression, it will be evaluated and the result will be returned. 
toan,ly,hoa=eval(input("Nhập điểm toán,lý,hóa:")) 
print("Điểm toán=",toan) 
print("Điểm lý=",ly) 
print("Điểm hóa=",hoa) 
dtb=(toan+ly+hoa)/3 
print("Điểm trung bình=",dtb) 
print("Điểm làm tròn=",round(dtb,2)) 