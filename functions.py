# python functions 사용 예시
# 함수 정의

def add_numbers(a, b):
    """두 숫자를 더하는 함수"""
    return a + b

add_numbers(3, 5)  # 함수 호출

# python에서 함수의 parameter는 기본적으로 위치 인자입니다.
# 위치 인자: 함수 호출 시 인자의 순서가 중요합니다.
def greet(name1, name2):
    """두 이름을 받아 인사하는 함수"""
    return f"Hello, {name1} and {name2}!"

# 위치 인자 사용
print(greet("Alice", "Bob"))  # "Hello, Alice and Bob!"


# 만약 인자의 개수가 맞지 않으면 오류가 발생합니다.
# greet("Alice")  # TypeError: greet() missing 1 required positional argument: 'name2'
# greet()  # TypeError: greet() missing 2 required positional arguments
# 만약 인자의 개수는 맞지만 순서가 다르다면 오류가 발생합니다.
# greet("Bob", "Alice")  # TypeError: greet() takes 1 positional argument but 2 were given

# 일반적으로 파이썬에서 함수코드의 위치를 어디에 두는 것이 좋을까요?
# 함수는 일반적으로 모듈의 최상단에 정의하는 것이 좋습니다.
# 이는 가독성을 높이고, 모듈을 사용하는 다른 코드에서 함수가 쉽게 찾을 수 있도록 하기 위함입니다.
# 또한, 함수 정의는 모듈의 다른 코드보다 먼저 위치해야 합니다.
# 함수가 모듈의 다른 코드에서 호출되기 전에 정의되어 있어야 합니다.


# 키워드 인자 사용
def greet_with_keyword(name1, name2="Guest"):
    """두 이름을 받아 인사하는 함수, 두 번째 인자는 기본값이 있음"""
    return f"Hello, {name1} and {name2}!"

print(greet_with_keyword("Alice"))  # "Hello, Alice and Guest!"

# keyword arguments를 사용하는 예시
def greet_with_keywords(name1="Alice", name2="Bob"):
    """두 이름을 받아 인사하는 함수, 기본값이 있음"""
    return f"Hello, {name1} and {name2}!"

print(greet_with_keywords(name2="Charlie"))  # "Hello, Alice and Charlie!"
print(greet_with_keywords(name1="Dave", name2="Eve"))  # "Hello, Dave and Eve!"

# 키워드 인자를 사용하는경우 호출시에 순서가 중요하지 않습니다.
# 키워드의 이름만 맞다면 순서에 상관없이 인자를 전달할 수 있습니다.
print(greet_with_keywords(name2="Bob", name1="Alice"))  # "Hello, Alice and Bob!"

# optional arguments (선택적 인자)
# name2 = None인 경우, 인자를 전달하지 않아도 됩니다.
# 이 경우, 함수는 기본값을 사용합니다.
# 만약 인자를 기본값이 "" (빈 문자열)로 설정하면, 인자를 전달하지 않아도 됩니다.
# 이 경우, 함수는 빈 문자열을 사용합니다.
# 함수의 parameter가 기본값을 가지는 경우, 선택적 인자라고 합니다.
# 기본값을 None으로 설정하는 것과 빈 문자열("")로 설정하는 것은 상황에 따라 다릅니다.
# None은 인자가 전달되지 않았음을 명시적으로 나타내는 경우에 사용합니다
# 빈 문자열은 인자가 전달되었지만, 값이 없음을 나타내는 경우에 사용합니다.
# 일반적으로 None을 사용하는 것이 더 명확합니다.
def greet_with_optional(name1, name2=None):
    """두 이름을 받아 인사하는 함수, 두 번째 인자는 선택적"""
    if name2 is None:
        return f"Hello, {name1}!"
    return f"Hello, {name1} and {name2}!"
print(greet_with_optional("Alice"))  # "Hello, Alice!"


def say_hello(name="World"):
    """이름을 받아 인사하는 함수, 기본값은 'World'"""
    message =  f"Hello, {name}!"
    return message
print(say_hello())  # "Hello, World!"
print(say_hello("Alice"))  # "Hello, Alice!"

# python함수를 사용할때 하는 흔한 실수
def shout1(message):
    """문자열에 느낌표를 추가하는 함수"""
    message += '!'  # 문자열에 느낌표 추가
    # 수정된 문자열 반환을 안할경우
    # 원래 문자열이 변경되지 않음
hello1 = "Hello"
message1 = shout1(hello1)  # hello1은 변경되지 않음
print(message1)  # None, 반환값이 없으므로 None 출력



def shout2(message):
    message += '!!!!!!' # 문자열에 느낌표 추가
    return message # 수정된 문자열 반환

hello2 = "Hello"

print(shout2(hello2))  # "Hello!!!!!!"


# python에서 primitive type인 문자열을 함수에서 수정하려면,
# 문자열을 수정한 후, 수정된 문자열을 반환해야 합니다.
# primitive type에는 문자열, 정수, 부동소수점 숫자, 불리언 등이 있습니다.
# 이러한 primitive type은 불변(immutable)하므로, 함수 내에서 수정해도
# 원래 변수는 변경되지 않습니다.

# 반대로 list, dict, set, tuple 등은 mutable type으로,
# 함수 내에서 수정하면 원래 변수도 변경됩니다.

# 함수에서 list를 수정하는 예시
def modify_list(my_list):
    """리스트에 요소를 추가하는 함수"""
    return my_list.append("new item")  # 리스트에 새 항목 추가

my_list = ["item1", "item2"]
modify_list(my_list)  # my_list가 변경됨
print(my_list)  # ["item1", "item2", "new item"]

# mutable type인 list는 함수 내에서 수정하면 원래 변수도 변경되는데
# 이는 함수가 원래 리스트를 참조하기 때문입니다.
# 그렇다면 함수에서 return을 사용하지 않고도
# 원래 리스트를 수정할 수 있습니다.
# 그러면 함수가 return을 사용하는것과 사용하지않는것의 차이는 무엇일까요?
# return을 사용하지 않는 경우, 함수는 원래 리스트를 직접 수정합니다.
# return을 사용하는 경우, 함수는 수정된 리스트를 새로 반환합니다.
# return을 사용하지 않는 경우, 함수는 원래 리스트를 직접 수정하므로,
# 원래 리스트가 변경됩니다.
# return을 사용하는 경우, 함수는 수정된 리스트를 새로 반환하므로,
# 원래 리스트는 변경되지 않습니다.

# 어떤 경우에 return을 사용하는 것이 좋고 어떤 경우에 사용하지 않는 것이 좋을까요?
# return을 사용하는 것이 좋습니다.
# return을 사용하면 함수가 명시적으로 값을 반환하므로, 함수의 동작이 명확해집니다.
# 또한, 함수가 반환하는 값을 다른 변수에 저장할 수 있으므로,
# 함수의 결과를 재사용할 수 있습니다.
# 함수에서 return을 사용하지 않는 경우, 함수가 원래 리스트를 직접 수정하므로,
# 함수의 동작이 명확하지 않을 수 있습니다.
# 또한, 함수의 결과를 재사용할 수 없으므로, 함수의 결과를 다른 변수에 저장할 수 없습니다.

# 함수에서 return을 사용하는 케이스
def add_to_list(my_list, item):
    """리스트에 새 항목을 추가하고 수정된 리스트를 반환하는 함수"""
    my_list.append(item)  # 리스트에 새 항목 추가
    # 반환하는 요소의 변수명은 my_list은 add_to_list 함수의 매개변수 이름과 동일합니다.
    # 함수가 반환하는 요소의 변수명이 함수의 매개변수 이름과 동일한 이유는 무엇일까요?
    # 이는 함수가 매개변수로 전달된 리스트를 수정하고, 수정된 리스트를 반환하기 때문입니다.
    # 함수가 매개변수로 전달된 리스트를 수정하지 않고, 새 리스트를 생성하여 반환하는 경우,
    # 함수의 매개변수 이름과 반환하는 요소의 변수명이 동일할 필요는 없습니다.
    # 그러나 함수가 매개변수로 전달된 리스트를 수정하고, 수정된 리스트를 반환하는 경우,
    # 함수의 매개변수 이름과 반환하는 요소의 변수명이 동일한 것이
    # 가독성을 높이고, 함수의 동작을 명확하게 합니다.
    return my_list  
my_list = ["item1", "item2"]
new_list = add_to_list(my_list, "item3")  # my_list가 변경됨
print(new_list)  # ["item1", "item2", "item3"]