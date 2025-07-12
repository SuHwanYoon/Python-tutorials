furuit_basket = ['apple', 'banana', 'cherry']
furuit_basket2 = ['orange', 'grape', 'kiwi']
for fruit in furuit_basket:
    print(f"The furuit is {fruit}")
    print(f"It's a delicious!")

print()

# enumerate는 리스트의 인덱스와 값을 함께 가져올 때 유용합니다.
for i, fruit in enumerate(furuit_basket2):
    print(f"Index {i}: The furuit is {fruit}")
    print(f"It's a tasty fruit!")    


print()


# range는 숫자 범위를 생성할 때 사용합니다.
# 예를 들어, 0부터 4까지의 숫자를 생성하려면 다음과 같이 합니다.
for i in range(5):
    print(f"Number: {i}")

 
print()

# range를 사용하여 짝수 숫자만 출력할 수도 있습니다.
for i in range(0, 10, 2):
    print(f"Even Number: {i}")

# range를 사용하여 역순으로 숫자를 출력할 수도 있습니다.
for i in range(10, 0, -1):
    print(f"Reverse Number: {i}")



# range를 사용하여 음수를 출력할 수도 있습니다.
for i in range(0, -10, -2):
    print(f"Negative Even Number: {i}")

print()


# while 과 break
# while 루프는 조건이 참인 동안 계속 실행됩니다.
# break 문을 사용하면 루프를 즉시 종료할 수 있습니다.
count = 0
while count < 5:
    print(f"Count is {count}")
    count += 1
    if count == 3:
        print("Breaking the loop at count 3")
        break       


print()

# while, brak, continue
# continue 문을 사용하면 현재 반복을 건너뛰고 다음 반복으로 넘어갑니다.
count = 0
while count < 5:
    count += 1
    if count == 3:
        print("Skipping count 3")
        continue
    print(f"Count is {count}")  
