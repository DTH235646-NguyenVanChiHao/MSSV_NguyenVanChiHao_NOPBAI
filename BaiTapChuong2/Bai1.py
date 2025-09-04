#perimeter
#area

import math

try: 
    r= float(input("Nhap ban kinh hinh tron: "))
    if r<0:
        print("Ban kinh khong hop le")                      
    else:
        P= 2*math.pi*r
        dt = math.pi*(r**2)
        print("Chu vi hinh tron la: ", round(P,3))   
        print("Dien tinh hinh tron la: ", dt)   
        print('Chu vi hinh tron la: {:.3f}'.format(P))  
        print(""+"Dien tinh hinh tron la: {:.3f}".format(dt))
except ValueError:
    print("Ban kinh khong hop le")
except:
    print("Co loi xay ra")

finally:
    print("Cam on ban da su dung chuong trinh")
# end


