#1

print("안녕하세요?")
s = input("이름이 어떻게 되시나요?")
print("만나서 반갑습니다 "+s+"씨")
print("이름의 길이는 다음과 같군요. "+str(len(s)))
y = int(input("나이가 어떻게 되나요? "))
print("내년이면 "+str(y+1)+"이 되시는군요.")


#2

a = input("기호를 입력하시오 : ")
b = input("중간에 삽입할 문자열을 입력하시오 : ")
print(a[0]+str(b)+a[1])


#3

import turtle

t=turtle

t.shape("turtle")

x1=int(input("x1을 입력하세요 : "))
y1=int(input("y1을 입력하세요 : "))
x2=int(input("x2을 입력하세요 : "))
y2=int(input("y2을 입력하세요 : "))
x3=int(input("x3을 입력하세요 : "))
y3=int(input("y3을 입력하세요 : "))

t.up()
t.goto(x1,y1)
t.down()
t.goto(x2,y2)
t.goto(x3,y3)

t.done()


#4

import turtle

t=turtle
t.shape("turtle")


a=str(input("yellow, red, blue, green중 첫 번째 색을 입력하세요."))
b=str(input("yellow, red, blue, green중 두 번째 색을 입력하세요."))
c=str(input("yellow, red, blue, green중 세 번째 색을 입력하세요."))
d=str(input("yellow, red, blue, green중 네 번째 색을 입력하세요."))
color=[a,b,c,d]
start = 0
for a in range(0,5,1) :
    start += 50
    t.fillcolor(color[a])
    t.begin_fill()
    t.circle(100)
    t.end_fill()
    t.goto(start,0)
t.done()


#5

a=int(input("현재 온도를 입력하시오 : "))

if a>=25 :
    print("반바지를 입으세요")
else :
    print("긴바지를 입으세요.")


#6

score = int(input("성적을 입력하시오 : "))

if score<0 or score>100 :
    print("잘못 입력하셨습니다.")
elif score>=90 :
    print("A학점 입니다.")
elif score>=80 :
    print("B학점 입니다.")
elif score>=70 :
    print("C학점 입니다.")
elif score>=60 :
    print("D학점 입니다.")
else :
    print("F학점 입니다.")


#7

import random
num1 = random.randint(1,100)
num2 = random.randint(1,100)

answer = int(input(str(num1)+"-"+str(num2)+"= "))
if answer == num1-num2 :
    print("맞았습니다.")
else :
    print("틀렸습니다.")


#8

want = int(input("원하는 단은 ? "))

for one_to in range(1,10,1) :
    print(str(want)+"*"+str(one_to)+"="+str(want*one_to))


#9 다시 해봐야 함.

#10

import random

num1 = int(random.randint(1,10))
num2 = int(random.randint(1,10))

answer = input(str(num1)+"*"+str(num2)+"는 ")

while answer != str(num1*num2) :

    num1 = int(random.randint(1,10))
    num2 = int(random.randint(1,10))

    answer = input(str(num1)+"*"+str(num2)+"는 ")

print("맞았습니다.")

#11


answer = int(input("정수를 입력하시오 : "))
total = answer 

while answer != 0 :
    answer = int(input("정수를 입력하시오 : "))
    total += answer
    
print("정수의 총 합은 ? ",str(total))


#12

import random
import turtle

turtle.shape("turtle")

for count in range(1,11,1) :


    x = int(random.randint(-200,200))
    y = int(random.randint(-200,200))
    r = int(random.randint(1,100))

    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    turtle.circle(r)

