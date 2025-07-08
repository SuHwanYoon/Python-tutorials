print(5 // 3)  # 정수 나눗셈, 결과는 1
print(5 % 3)   # 나머지, 결과는 2
print(5 ** 3)  # 거듭제곱, 결과는 125

x = 10
x += 5  # x = x + 5
print(x)  # 결과는 15

x *= 2  # x = x * 2
print(x)  # 결과는 30

# python Evaluation 
result = 10 + 5 * 2 - 3 / 1
print(result)  # 결과는 17.0

#  Should I make a coffee right now?
is_cup_empty = False
is_daytime = True
should_make_coffee = is_cup_empty and is_daytime
print('Should I make coffee?' ,should_make_coffee)  # 결과는 False


# Should I walk or dive to my office?
is_raining = False
is_tired = True
should_walk = not is_raining and not is_tired
should_drive = is_raining or is_tired
print('Should I walk to my office?', should_walk)  # 결과는 False
print('Should I drive to my office?', should_drive)  # 결과는 True



