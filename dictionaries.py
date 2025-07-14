fruit_price = {
    "apple": 1.20,
    "banana": 0.50,
    "cherry": 2.00
}

fruit_price["orange"] = 0.80  # 새로운 과일 추가
fruit_price["banana"] = 0.60  # 가격 업데이트
fruit_price.update({"kiwi": 1.50})  # 여러 과일 추가

print(fruit_price)  # {'apple': 1.2, 'banana': 0.6, 'cherry': 2.0, 'orange': 0.8, 'kiwi': 1.5}

not_found_price = fruit_price.get("grape",0)  # 'grape'가 없으므로 기본값 0 반환
print(not_found_price)  # 0



if "apple" in fruit_price:
    print("Apple is available.")
else:
    print("Apple is not available.")


# comprehension을 사용하여 가격이 1.00 이상인 과일만 포함하는 딕셔너리 생성
# furuit: price 형태로 딕셔너리를 생성합니다.
# fruit_price.items()는 딕셔너리의 (키, 값) 쌍을 반환합니다.
# comprehension은 for 루프와 if 조건을 사용하여
# 조건에 맞는 항목만 포함하는 새로운 딕셔너리를 생성합니다.
# for fruit, price in fruit_price.items()는 각 과일과 가격을 순회합니다.
# 여기서는 가격이 1.00 이상인 과일만 포함합니다.
expensive_fruits = {fruit: price 
                    for fruit, price in fruit_price.items()
                     if price >= 1.00}
print(expensive_fruits)  # {'apple': 1.2, 'cherry': 2.0}    


# dictionary와 len을 사용하여 과일의 개수 출력
print(f"Number of fruits: {len(fruit_price)}")  # Number of fruits: 5
count = 0
for fruit in fruit_price:
    count += 1
print(f"Number of fruits using loop: {count}")  # Number of fruits using loop: 5
print(f"Number of fruits using len: {len(fruit_price)}")  # Number of fruits using len: 5
print(f"Number of fruits using for loop: {len([fruit for fruit in fruit_price])}")  # Number of fruits using for loop: 5
print(f"Number of fruits using comprehension: {len({fruit for fruit in fruit_price})}")  # Number of fruits using comprehension: 5
print(f"Number of fruits using comprehension with items: {len({fruit: price for fruit, price in fruit_price.items()})}")  # Number of fruits using comprehension with items: 5
print(f"Number of fruits using comprehension with items and condition: {len({fruit: price for fruit, price in fruit_price.items() if price >= 1.00})}")  # Number of fruits using comprehension with items and condition: 2


for key, value in fruit_price.items():
    print(f"{key}: ${value:.2f}")  # apple: $1.20, banana: $0.60, cherry: $2.00, orange: $0.80, kiwi: $1.50
    print(f"{key} costs ${value:.2f}")  # apple costs $1.20, banana costs $0.60, cherry costs $2.00, orange costs $0.80, kiwi costs $1.50
    print(f"The price of {key} is ${value:.2f}")  # The price of apple is $1.20, The price of banana is $0.60, 

# 새로운 shoe 딕셔너리 생성
shoe = {
    "brand": "Nike",
    "model": "Air Max",
    "size": 10,
    "color": ["Black", "White", "Red"],
    "price": 120.00
}
print(shoe)  # {'brand': 'Nike', 'model': 'Air Max', 'size': 10, 'color': 'Black'}
