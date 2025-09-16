#Learn Random Module

from random import randrange 

continue_game=True
while continue_game: 
    somay=randrange(1,101) 
    solandoan=0 
    while solandoan<7: 
        solandoan+=1 
        songuoi=int(input("Máy đoán [1..100], mời bạn đoán:")) 
        print("Bạn đoán lần thứ ",solandoan) 
        if somay==songuoi: 
            print("Chúc mừng bạn đoán đúng, số máy là=",somay) 
            break 
        if somay > songuoi: 
            print("Bạn đoán sai, số máy > số bạn") 
        else:
            print("Bạn đoán sai, số máy < số bạn") 
    
    if solandoan==7: 
        print("Bạn đã thua, số máy là=",somay)

    continue_game=input("Tiếp không?") 
    if continue_game.lower()!="y": 
        continue_game=False
print("Cám ơn bạn đã chơi Game!") 