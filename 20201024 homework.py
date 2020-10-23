
#1 초콜렛을 자르는 방법의 수
'''
a = int(input("가로 길이를 입력하세요 : "))
b = int(input("세로 길이를 입력하세요 : "))

print("자르는 방법은 총 " , a*b-1)
'''

#2 

import turtle as t #as t라고 작성하면 앞으로 t로 작성해도 먹힘

a=int(t.textinput("원의 크기를 결정하세요 : ", ""))
b=str(t.textinput("색상을 결정하세요 : ", "영어로 작성하세요"))
t.shape ("turtle")
t.color(b)
t.circle(a)
t.done()
