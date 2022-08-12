#음식 리스트 중에서
#그중 하나를 추천
import random
foodlist = ["짜장면","짬뽕","탕수육","우동",]


food = random.choice(foodlist)
#자동으로 입력되게 냅둬야 오히려 오류가 줄어든다..오타방지
print(food)

# 5번을 연속으로 추천해보자
for i in range(5):
    # print(i+1) ctrl / 누르면 주석으로 바꾼다
    food = random.choice(foodlist)
#자동으로 입력되게 냅둬야 오히려 오류가 줄어든다..오타방지
    print(f"{i+1}. {food}")

  

print("종료")
lotto = list(range(1,46))

my = random.sample(lotto, 6)

