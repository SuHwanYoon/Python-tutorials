furuit_basket = ["apple", "banana", "orange"]
furuit = furuit_basket[0]

print(furuit)  # apple


if "apple" in furuit_basket:
    print("You have an apple in your basket.")
else:
    print("You don't have an apple in your basket.")    

furuit_basket.append("grape")
print(furuit_basket)  # ['apple', 'banana', 'orange', 'grape']
furuit_basket.remove("banana")
print(furuit_basket)  # ['apple', 'orange', 'grape']    
furuit_basket.insert(1, "kiwi")
print(furuit_basket)  # ['apple', 'kiwi', 'orange', 'grape']
furuit_basket.sort()
print(furuit_basket)  # ['apple', 'grape', 'kiwi', 'orange']
furuit_basket.reverse()
print(furuit_basket)  # ['orange', 'kiwi', 'grape', 'apple']
furuit_basket.clear()
print(furuit_basket)  # []  
furuit_basket = ["apple", "banana", "orange"]
print(len(furuit_basket))  # 3
print(furuit_basket[0])  # apple
print(furuit_basket[-1])  # orange
print(furuit_basket[1:3])  # ['banana', 'orange']
print(furuit_basket[:2])  # ['apple', 'banana']
print(furuit_basket[1:])  # ['banana', 'orange']
print(furuit_basket[-2:])  # ['banana', 'orange']
print(furuit_basket[::2])  # ['apple', 'orange']
print(furuit_basket[::-1])  # ['orange', 'banana', 'apple']
print(furuit_basket * 2)  # ['apple', 'banana', 'orange', 'apple', 'banana', 'orange']
print("apple" in furuit_basket)  # True
print("grape" in furuit_basket)  # False
print("banana" not in furuit_basket)  # False
print("grape" not in furuit_basket)  # True 
print(furuit_basket.index("banana"))  # 1
print(furuit_basket.count("apple"))  # 1
print(furuit_basket.count("grape"))  # 0

furuit_basket = ["apple", "banana", "orange"]
furuit_basket.pop()  # 마지막 요소 제거
print(furuit_basket)  # ['apple', 'banana']
furuit_basket.pop(0)  # 첫 번째 요소 제거
print(furuit_basket)  # ['banana']
furuit_basket.pop(1)  # 두 번째 요소 제거
print(furuit_basket)  # ['banana']
furuit_basket = ["apple", "banana", "orange"]
furuit_basket.remove("banana")  # "banana" 요소 제거
print(furuit_basket)  # ['apple', 'orange']
furuit_basket.remove("grape")  # "grape" 요소가 없으면
# ValueError 발생
# print(furuit_basket)  # ['apple', 'orange']
furuit_basket = ["apple", "banana", "orange"]
furuit_basket.clear()  # 모든 요소 제거
print(furuit_basket)  # []
furuit_basket = ["apple", "banana", "orange"]
furuit_basket.extend(["grape", "kiwi"])  # 리스트 확장
print(furuit_basket)  # ['apple', 'banana', 'orange', 'grape', 'kiwi']
furuit_basket.extend("melon")  # 문자열 확장
print(furuit_basket)  # ['apple', 'banana', 'orange', 'grape', 'kiwi', 'm', 'e', 'l', 'o', 'n']
furuit_basket = ["apple", "banana", "orange"]
furuit_basket.append(["grape", "kiwi"])  # 리스트 추가

my_list = [1, 2, 3]
sliced_list = my_list[1:3]  # [2, 3]
clone_list = my_list[:]  # [1, 2, 3]
print(clone_list)  # [1, 2, 3]
print(sliced_list)  # [2, 3]