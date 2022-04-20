class Product(object):
    pass

class Inventory(object):
    def __init__(self):
        self.__items = []   # __items = private 변수
    def add_new_item(self, product):
        #print(type(product))    # <class '__main__.Product'>
        if type(product) == Product:
            self.__items.append(product)
            print("new item added")
        else:
            raise ValueError("Invalid Item")
    def get_number_of_items(self):
        return len(self.__items)

my_inventory = Inventory()      # 객체 생성
my_inventory.add_new_item(Product())
my_inventory.add_new_item(Product())

my_inventory.__items    # 객체내의 private 변수 액세스 불가능.
