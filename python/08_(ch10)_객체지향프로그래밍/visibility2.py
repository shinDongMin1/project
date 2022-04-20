
class Product(object):
    pass

class Inventory(object):            # private 변수로 선언(타인이 접근 못 함)
    def __init__(self):
        self.__items = [1, 2]       # 편의상 기존 재고가 있는 것으로 가정한다.

    def add_new_item(self, product):
        if type(product) == Product:
            self.__items.append(product)
            print("new item added")
        else:
            raise ValueError("Invalid Item")

    def get_number_of_items(self):
        return len(self.__items)

    def get_items(self):            # private 변수, list를 반환
        return self.__items         # 주의!! 반환받는 변수는 자료를 공유한다.

    @property                       # property 데코레이터(숨겨진 변수 반환)
    def items(self):                # 함수를 변수로 바꾸어준다.
        return self.__items         # 숨겨진 변수와 함수의 이름이 같아야 한다.
                                    # 주의!! 반환받는 변수는 자료를 공유한다.


my_inventory = Inventory()
print(my_inventory.get_items())     # [1, 2]. 함수를 호출하여 items를 반환받음
print(my_inventory.items)           # [1, 2]. 함수였는데 변수가 되었음.

my_inventory.add_new_item(Product())        # new item added
print(my_inventory.get_number_of_items())   # 3

my_items = my_inventory.items
if my_items is my_inventory.items:
    print('They share data.')       # 데이터를 공유한다.

print(len(my_items))                # 3
my_items.append(Product())          # 4개로 늘어남.
my_items.append('100')              # 5개로 늘어남.
my_inventory.add_new_item(Product())    # 6개로 늘어남.
print(len(my_items))                        # 6
print(my_inventory.get_number_of_items())   # 6

another = my_inventory.get_items()
another.append('200')
print(my_inventory.get_number_of_items())   # 7

if another is my_inventory.items:
    print('They share data.')

another.pop()           # 객체의 private 변수로 지운다.
my_items.pop()
print(len(another))                         # 5
print(len(my_items))                        # 5
print(len(my_inventory.items))              # 5
print(my_inventory.get_number_of_items())   # 5

