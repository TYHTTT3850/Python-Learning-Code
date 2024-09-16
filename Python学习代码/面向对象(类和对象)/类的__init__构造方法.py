#在设计类时使用__init__方法，可以实现在创建对象时直接传入属性的操作。
#__init__方法称为构造方法，在创建对象时会自动执行。
#构造方法也是成员方法，也需要self形参。
class Person:
    name = None
    age = None
    tel = None #其实可以省略定义成员变量的步骤，因为__init__方法会自动定义
    def __init__(self, name , age , tel):
        self.name = name
        self.age = age
        self.tel = tel
        print("创建对象成功")

# 创建对象时直接传入成员变量值：
person1 = Person("Mike",18,"1800000000")
print(person1.name,person1.age,person1.tel,sep=" ")
