import random

#화면에 음식 리스트를 출력하는 기능
def print_list(aa):
    for i, food in enumerate(aa):
        print(f"{i+1}. {food}")
#음식 리스트중에서 하나를 추천해주는 기능
def print_rand_list(bb):
    for i in range(5):
        food = random.choice(bb)
        print(f"{i+1}. {food}")