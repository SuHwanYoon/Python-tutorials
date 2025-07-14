# comprehention은 list, set, dict를 생성하는 간결한 방법입니다.
# 예를 들어, 0부터 9까지의 제곱수를 포함하는 리스트
squares = [x**2 for x in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 조건을 추가하여 짝수 제곱수만 포함하는 리스트
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)  # [0, 4, 16, 36, 64]

# comprehension은 어떤 경우에 유용한가요?
# 예를 들어, 리스트의 각 요소에 2를 곱하는 경우
doubled = [x * 2 for x in range(10)]
print(doubled)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]   

# comprehension은 set과 딕셔너리에도 사용할 수 있습니다.
# 예를 들어, 0부터 9까지의 제곱수를 포함하는 set
squares_set = {x**2 for x in range(10)}
print(squares_set)  # {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}

