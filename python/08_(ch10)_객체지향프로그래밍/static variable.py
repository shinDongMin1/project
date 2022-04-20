class MyClass:
    myVar = 1
    def __init__(self):
        print("Constructor")

    def __del__(self):
        print("Destructor")

    def HelloWorld(self):
        MyClass.myVar = 2   # 여기서 myVar 는 static 변수 입니다.
        self.myVar = 3      # 여기서 myVar 는 self (instance) 의 변수 입니다.


a = MyClass()
print("Static Value? : %d" % MyClass.myVar)
print("Instance Value of 'a'? : %d" % a.myVar)

a.HelloWorld()
print("################# HelloWord invoked")

print("Static Value? : %d" % MyClass.myVar)
print("Instance Value of 'a'? : %d" % a.myVar)

b = MyClass()
print("Instance Value of 'b'? : %d" % b.myVar)