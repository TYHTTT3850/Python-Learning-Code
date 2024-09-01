# 多返回值函数
def multiple_returns():
    return 1,"hello",True # 可以任意多
x,y,z = multiple_returns() #位置对应
print(x,y,z,sep=",")
print()

# 位置参数和关键字参数
def user_info1(name,age,gender):
    print(f"Hello {name},you are {age},you are {gender}")
user_info1("John",23,"Male") #位置参数
user_info1(name="Marry",age=23,gender="Female") #关键字参数
user_info1(age=23,gender="Female",name="Marry") #关键字参数可换顺序
user_info1("Jack",age=23,gender="Male") #位置参数和关键字参数，位置参数必须在关键字参数前
print()

# 缺省参数(默认值)
def user_info2(name,age,gender="Male"): # 设置默认值的参数需统一放在无默认值参数的后面
    print(f"Hello {name},you are {age},you are {gender}")
user_info2("Jack",age=23)
user_info2("Marry",gender="Female",age=23)
print()

# 不定长参数(可变参数)，不确定调用时传递几个参数(不传参也可以)
def test_args(*args): # 位置不定长，*args可以改成其他名字
    print(f"args类型为：{type(args)},内容是：{args}")
test_args("Jack","Marry","Jhon",11,22,33)
def test_kwargs(**kwargs): # 关键字不定长，**kwargs可以改成其他名字
    print(f"kwargs类型为：{type(kwargs)},内容是：{kwargs}")
test_kwargs(name="Marry",age=23,gender="Female")