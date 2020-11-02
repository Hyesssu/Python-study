#1
'''
import turtle
turtle.shape("turtle")

def square() :
    for _ in range (4) :
        turtle.forward(50)
        turtle.left(90)

for i in range(3) :
    turtle.up()
    turtle.goto(100*i,0)
    turtle.down()
    square()

turtle.done()
'''

#2
'''
def sum_ (first, second) : 
    print("정수",str(first)+"+"+str(second),"의 합은 ? ")

first = int(input("첫 번째 정수 : "))
second = int(input("두 번째 정수 : "))

sum_(first,second)
'''

#3
'''
def sum_ (radius) :
    return radius**2*3.1415926

def length (radius) :
    return radius*2*3.1415926

radius = int(input("반지름의 값을 입력하세요 : "))
print("반지름이",str(radius)+"인 원의 면적 : ",sum_(radius))
print("반지름이",str(radius)+"인 원의 둘레 : ",length(radius))
'''

#4 
'''
def function (x) :
    return (x**2+1)*0.01

import turtle
turtle.shape("turtle")
turtle.forward(100)
turtle.home()
turtle.left(90)
turtle.forward(100)
turtle.home()

for x in range (100) :
    turtle.goto(x,function(x))

turtle.done()
'''

#5 
'''
import turtle
slist =[]
def number () :
    for _ in range (7) :
        num = int(input("자료를 입력하세요 : "))
        slist.append(num)

number()

turtle.shape("arrow")
turtle.color("blue","red")

def turtle_play () :
    turtle.left(90)
    turtle.forward(slist[i])
    turtle.left(90)

for i in range (7) :
    turtle.goto(50*i,0)
    turtle.forward(50)
    turtle_play()
    turtle.forward(50)
    turtle.write(slist[i])
    turtle_play()
    turtle.goto(50*i,0)

turtle.forward(50)
turtle.done()
'''

#6-1
'''
i = int(input("정수를 입력하시오 >> "))

for star in range (i+1) :
    print("*"*star+" "*(i-star))
'''

#6-2
'''
i = int(input("정수를 입력하시오 >> "))

for star in range (i+1) :
    print("*"*(i-star)+" "*star)
'''

#6-3
'''
i = int(input("정수를 입력하시오 >> "))

for star in range (i+1) :
    print(" "*(i-star)+"*"*star)
'''

#6-4
'''
i = int(input("정수를 입력하시오 >> "))

for star in range (i+1) :
    print(" "*star+"*"*(i-star))
'''
