fruit_list = ["apple", "banana", "cherry", "date"]
fruit_set = {"apple", "banana", "cherry", "date"}

fruit_list.append("elderberry")  # 리스트는 변경 가능
fruit_set.add("elderberry")  # 집합은 변경 가능
fruit_list.append("apple")  # 중복된 값은 추가됨
fruit_set.add("apple")  # 중복된 값은 추가되지 않음``
fruit_list.remove("banana")  # 리스트에서 값 제거
fruit_set.discard("banana")  # 집합에서 값 제거 (존재하지 않아도 에러 발생 안함)

print(f"Fruit List: {fruit_list}")
print(f"Fruit Set: {fruit_set}")

# set의 요소에 특정요소가 있는지 확인
print(f"Is 'apple' in fruit_set? {'apple' in fruit_set}")
print(f"Is 'banana' in fruit_set? {'banana' in fruit_set}")
print(f"Is 'cherry' in fruit_set? {'cherry' in fruit_set}")
# set의 교집합, 합집합, 차집합
another_set = {"cherry", "date", "fig"}
# set의 요소를 문자열로 변환하려면 join() 함수를 사용
print(f"Fruit Set as String: {', '.join(fruit_set)}")

# intersection, union, difference를 이용한 set 연산
print(f"Intersection with another_set: {fruit_set.intersection(another_set)}")
print(f"Union with another_set: {fruit_set.union(another_set)}")
# difference는 차집합을 구함
# difference의 순서는 fruit_set에서 another_set을 뺀 결과
print(f"Difference with another_set: {fruit_set.difference(another_set)}")

