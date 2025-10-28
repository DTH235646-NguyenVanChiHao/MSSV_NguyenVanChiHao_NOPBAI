n = 7


result = ""
for i in range(0, n ):
    if(i < n//2):
       result += " "*(n//2) + "*"*(i +1) +"\n"
    elif (i == n//2):
         result += "*"*n +"\n"
    else:
         result += "*"*(n - i)+"\n"

print(result   )