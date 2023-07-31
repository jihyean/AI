import sys
print(sys.version)
#python ... type int/float/string/bool
a = 1
print(type(a))#<class 'int'>
print(a)#1
a = 1.123
print(type(a))#<class 'float'>
print(a)#1.123
a = 'python'
print(type(a))#<class 'str'>
print(a)#python
a = 10>50
print(type(a))#<class 'bool'>
print(a)#False


a = 1 #대입 연산자 ... 초기화+객체의 인스턴스화...
b = 2
print (a+b)
print (a-b)
print (a*b)
print (a/b)
print (type(a+b))
print (type(a-b))
print (type(a*b))
print (type(a/b))

#python ... container list/tuple/dict
'''
list...[]...read/write/modify
       [start:end]...start, end +/-
tuple..()...read
dict...{key:value}...searching
'''
a = [1,2,3,4,5]
print(a)#[1, 2, 3, 4, 5]
print(type(a))#<class 'list'>

print(a[1:])#[2, 3, 4, 5]
print(a[:3])#[1, 2, 3]
print(a[:-1])#[1, 2, 3, 4]
print(a[:-2])#[1, 2, 3]
print(a[0])
print(a[4])
#print(a[5])#error....list index out of range

#dict
a = {'height':180}#dictionary ctor
print(a)#{'height': 180}
print(type(a))#<class 'dict'>
print(a['height'])#180

a['height'] = 185
print(a['height'])#185

a['weight'] = 80
print(a)

a = 10
b = 20
dictCalc = {'+':a+b,'-':a-b,'*':a*b,'/':a/b}
print(dictCalc)#{'+': 30, '-': -10, '*': 200, '/': 0.5}
print(dictCalc['+'])#30


#bool
hungry = True
sleepy = False
print(type(hungry))
print(not hungry)
#hungry = not hungry
print(hungry and sleepy)
print(hungry or sleepy)

#if
hungry = True
if hungry :
    print("I'm hungry")

hungry = False
if hungry :
    print("I'm hungry")
else :
    print("I'm not hungry")
    print("I'm sleepy")

#for
for x in range(1, 5+1, 1):
    print(x)
for x in [1,2,3,4,5]:
    print(x)
Xs = [1,2,3,4,5]
for x in Xs:
    print(x)

#function
def hello(count):
    for x in range(count):
        print("hello world!!")

hello(10)

def hello_animal(name):
    print("hello " + name + " my animal!!")

hello_animal("몰리~~~~")


#계산기...dict..출력
#구구단...가로..세로 출력




















