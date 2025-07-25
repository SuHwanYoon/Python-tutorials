# python 에서 tuple이 List보다 유용한 경우는 어떤 경우일까?
# 튜플은 불변(immutable)한 자료형으로, 다음과 같은 경우에 유용합니다.
# 1. 데이터의 불변성 보장: 튜플은 생성 후 변경할 수 없으므로, 데이터가 변경되지 않도록 보장할 때 유용합니다.
# 2. 해시 가능성: 튜플은 해시 가능하므로, 딕셔너리의 키로 사용하거나 집합(set)의 원소로 사용할 수 있습니다.
# 3. 성능: 튜플은 리스트보다 메모리 사용이 적고, 생성 및 접근 속도가 빠릅니다.
# 4. 여러 값 반환: 함수에서 여러 값을 반환할 때 튜플을 사용하면 간편하게 여러 값을 묶어서 반환할 수 있습니다.
# 5. 데이터 구조: 튜플은 고정된 크기의 데이터 구조를 표현할 때 유용합니다.
# 6. 데이터의 의미: 튜플은 각 요소가 의미를 가지는 경우, 예를 들어 (x, y) 좌표와 같은 경우에 유용합니다.
# 7. 패킹과 언패킹: 튜플은 여러 값을 하나의 변수로 묶을 수 있어, 패킹과 언패킹이 용이합니다.
# 8. 함수 인자: 함수의 인자로 여러 값을 전달할 때 튜플을 사용하면 가독성이 좋아집니다.
# 9. 데이터베이스 레코드: 데이터베이스에서 레코드를 표현할 때 튜플을 사용하면 각 필드의 의미를 명확히 할 수 있습니다.
# 10. 불변 데이터 구조: 불변 데이터 구조를 필요로 하는 상황에서 튜플은 유용합니다.

fruits_tuple = ("apple", "banana", "cherry")

# 언패킹시에는 변수의 개수가 튜플의 요소 개수와 일치해야 합니다.
# 일치하지 않으면 ValueError가 발생합니다.
apple, banana, cherry = fruits_tuple  # 언패킹

# 튜플 요소에서 사용하지 않는 요소는 언패킹시 _로 처리할 수 있습니다.
# apple, _, cherry = fruits_tuple  # banana는 사용하지 않음


print(f"Apple: {apple}, Banana: {banana}, Cherry: {cherry}")

# tuple을 dictionary의 키로 사용
fruits_dict = {
    fruits_tuple: "Tropical Fruits"
}
print(f"Fruits Dictionary: {fruits_dict}")

 
