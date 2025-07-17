import uuid
# uuid 모듈은 고유한 식별자를 생성하는 데 사용됩니다.
# UUID(Universally Unique Identifier)는 128비트 숫자로, 전 세계적으로 고유한 식별자를 생성하는 데 사용됩니다.
# 이 모듈은 주로 데이터베이스의 기본 키나 세션 식별자와 같은 고유한 식별자를 생성하는 데 사용됩니다.
# 웹애플리케이션에서 UUID는 사용자 세션, 파일 이름, 데이터베이스 레코드 등에서 고유성을 보장하기 위해 사용됩니다.
# uuid 모듈은 다양한 버전의 UUID를 생성할 수 있는 기능을 제공합니다.

class Product:
    # class의 모든 인스턴스에서 사용할수 있는 calories_to_kilojoules를 대문자로 변수 정의
    # 이 상수는 클래스의 모든 인스턴스에서 공유되며, 클래스의 속성으로 정의됩니다.
    # 대문자로 정의하는 것은 상수임을 나타내는 관례입니다.
    # 이 상수는 클래스의 모든 인스턴스에서 동일하게 사용됩니다.
    # 따라서, 이 상수는 클래스의 속성으로 정의하는 것이 좋습니다.
    CALORIES_TO_KILOJOULES = 4.184


    # class 는 객체의 blueprint 역할을 하는데 여기서 blueprint란 객체가 가져야 할 속성과 행동을 정의하는 것입니다.
    # 클래스는 객체를 생성하기 위한 틀을 제공하며, 객체는 클래스의 인스턴스(instance)입니다.
    # 클래스는 객체의 속성(attribute)과 메서드(method)를 정의합니다.
    # 속성은 객체가 가지고 있는 데이터이며, 메서드는 객체가 수행할 수 있는 행동을 정의합니다.
    # 클래스는 객체의 상태와 행동을 정의하는데, 상태는 객체의 속성(attribute)으로 표현되고, 행동은 메서드(method)로 표현됩니다
    # 생성자 메서드는 객체가 생성될 때 호출됩니다.
    # 생성자 메서드를 사용하는 이유는 객체의 초기 상태를 설정하기 위해서입니다.
    # 생성자 메서드는 __init__이라는 이름을 가지며, 첫 번째 매개변수로 self를 받습니다.
    # self는 생성된 객체 자신을 참조하는 역할을 합니다.
    # name과 price는 생성자 메서드의 매개변수로, 객체의 속성을 초기화하는 데 사용됩니다.
    def __init__(self, name, calories, price_per_kg):
        self.name = name
        self.calories = calories
        self.price_per_kg = price_per_kg
    
    # 객채의 price_per_kg 과 weight_kgs를 곱하여 가격을 계산하는 메서드
    def calculate_price(self, weight_kgs):
        return self.price_per_kg * weight_kgs

    # get_calories_kilojoules 메서드는 객체의 칼로리를 킬로줄로 변환하는 메서드입니다.
    # 이 메서드는 객체의 칼로리에 클래스 상수 CALORIES_TO_KILOJOULES를 곱하여 킬로줄로 변환합니다.
    def get_calories_kilojoules(self):
        return self.calories * self.CALORIES_TO_KILOJOULES
    
    # @staticmethod를 사용하여 generate_unique_id 메서드를 정의합니다.
    # 이 메서드는 클래스의 인스턴스와 관계없이 호출할 수 있는 정적 메서드입니다.
    # 이 메서드는 고유한 UUID를 생성하여 반환합니다.
    # uuid4()는 랜덤하게 UUID를 생성하고 hex는 16진수 문자열로 변환합니다
    # hex를 사용하고 안하고의 차이는 UUID의 표현 방식입니다.
    # hex를 사용하면 UUID를 32자리의 16진수 문자열로 표현합니다.
    # 16진수 문자열은 사람이 읽기 쉬운 형식으로, 예를 들어
    # 123e4567-e89b-12d3-a456-426614174000와 같은 형식입니다.
    # hex를 사용하지 않으면 UUID는 128비트 숫자로 표현됩니다. 128비트 숫자는 일반적으로 사람이 읽기 어려운 형식이며 01010101...와 같은 이진수 형태로 표현됩니다.
    @staticmethod
    def generate_unique_id():
        return f"Product-{uuid.uuid4().hex}"  



# banana 객체 생성
banana = Product(name="Banana", calories=89, price_per_kg=1.2)
# apple 객체 생성
apple = Product(name="Apple", calories=52, price_per_kg=2.5)
                
print(f"Product: {banana.name}, Calories: {banana.calories}, Price per kg: {banana.price_per_kg} USD")
print(f"Product: {apple.name}, Calories: {apple.calories}, Price per kg: {apple.price_per_kg} USD")
print()

# calculate_price 메서드를 사용하여 가격 계산
weight_kgs = 2  # 예시로 2kg의 가격을 계산
banana_price = banana.calculate_price(weight_kgs)
apple_price = apple.calculate_price(weight_kgs)
print(f"Price for {weight_kgs} kg of {banana.name}: {banana_price} USD")
print(f"Price for {weight_kgs} kg of {apple.name}: {apple_price} USD")



# get_calories_kilojoules 메서드를 사용하여 칼로리를 킬로줄로 변환
print()
banana_kilojoules = banana.get_calories_kilojoules()
apple_kilojoules = apple.get_calories_kilojoules()
print(f"Calories in {banana.name} (in kilojoules): {banana_kilojoules} kJ")
print(f"Calories in {apple.name} (in kilojoules): {apple_kilojoules} kJ")

# Product 클래스의 정적 메서드 generate_unique_id를 사용하여 고유한 ID 생성
# ID는 매번 호출할 때마다 새로운 UUID를 생성합니다.
print()
banana_id = Product.generate_unique_id()
apple_id = Product.generate_unique_id()
print(f"Unique ID for {banana.name}: {banana_id}")
print(f"Unique ID for {apple.name}: {apple_id}")
