import myfood

foodlist = ["짜장면","짬뽕","탕수육","우동",]
for i in range(5):
    food = myfood.random.choice(foodlist)
    print(f"{i+1}. {food}")
#화면에 음식 리스트를 출력을하고
for i, food in enumerate(foodlist):
    print(f"{i+1}. {food}")

#위 리스트를 출력
myfood.print_list(foodlist)

#리스트 중에 먹고싶은 메뉴가 없으면
#사용자가 계속 입력을한다
#만약에 그만을 입력하면 입력이 끝나고 
#음식 리스트 출력하고 추천 메뉴가 출력
while True:
    addfood = input("추가 음식 입력 :")
    print(f"당신이 입력한 내용: {addfood}")
    #만약에 그만을 입력하면 
    if addfood == "그만":
        break
        #무한반복을 멈춤
    foodlist.append(addfood)
# 음식 리스트 출력
myfood.print_list(foodlist)
#우리가 추가해서 그중에서 추천했으면좋겠다...
myfood.print_rand_list(foodlist)
