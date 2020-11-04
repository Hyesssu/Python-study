#6-5
'''
num = int(input("정수를 입력하시오 >> "))

for i in range (num+2) :
    print(" "*(num+1-i)+"*"*(2*i-1))
for n in range (num+1,0,-1) :
    print(" "*(num+1-n)+"*"*(n*2-1))
'''

#7
'''
start = start2 = int(input("시작 수 : "))
last  = int(input("끝 수 : "))
distance = int(input("증가 값 : "))
total_sum = start
total_times = start2

print("="*30)

print("합 :",str(start),end = " ")

for _ in range((last-start)//distance) :
    start+=distance
    total_sum+=start
    if start <= last :
        print("+",str(start),end=" ")

print("=",str(total_sum))


print("곱 :",str(start2),end= " ")

for _ in range((last-start2)//distance) :
    start2+=distance
    total_times*=start2
    if start2 <= last :
        print("*",str(start2),end=" ")

print("=",str(total_times))

print("="*30)
'''
#8
'''
slist=[]

for i in range (1,11) : 
    num = int(input(str(i)+"번째 숫자를 입력하시오 >> "))
    slist.append(num)

big = slist[0]
small = slist[0]

for a in range (10) :
    if big < slist[a] :
        big = slist[a]
    if small > slist[a] :
        small = slist[a]

print("입력된 값은",str(slist)+"이며, 제일 큰 값은 ",str(big)+"이고,")
print("제일 작은 값은 "+str(small)+"이다.")
'''
