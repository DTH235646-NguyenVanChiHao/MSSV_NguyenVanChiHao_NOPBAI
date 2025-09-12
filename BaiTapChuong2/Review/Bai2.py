#coi lai
#Hours - Minutes - Seconds
#Hour = 60 minutes  = 60*60 seconds
#
t=int(input("Nhập số giây:")) 

'''
the second is unknown => it can be larger than 24 hours
'''
hour=(t//3600)%24  
minute=(t%3600)//60 
second=(t%3600)%60 
print(hour,":",minute,":",second) 
# the hour can be larger 24

hour = (t  // 3600)  % 24
# the minute left
t %= 3600
minute = t // 60

# the second left
second = t % 60
print(hour,":",minute,":",second)   

'''
#Example:     
Input:  3661
Output: 1 : 1 : 1           
#Example:
Input:  86461
Output: 0 : 1 : 1
'''