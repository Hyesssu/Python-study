#초보를 위한 파이썬 300제

#1
print("Hello World")

#2
print("Mary's cosmetics")

#3
print('신씨가 소리질렀다. "도둑이야"' )

#4
print('"C:\Windows"')

#5
print("안녕하세요.\n만나서\t\t반갑습니다.") # \n은 줄 바꿈, \t는  tap

#6
print("오늘은","일요일") #결과예측 : 오늘은 일요일

#7
print("naver;kakao;sk;samsung") #print("naver", "kakao", "samsung", sep=";") 이렇게도 사용 가능

#8
print("naver/kakao/sk/samsung")
print("naver","kakao","sk","samsung",sep="/")

#9
#print("first")=print("second")
print("first", end=" ") #줄 바꿈 없이 print함수 두 개를 이용해서 두 단어를 쓰고 싶으면 end=""쓰기 
print("second") 

#10
print(5/3)

#11
삼성전자 = 50000
보유주식 = 10
print(삼성전자*보유주식) #한글로도 사용 가능

#12

시가총액 = 2980000000000
현재가 = 50000
per = 15.79
print("시가총액 = ", 시가총액)
print("현재가 =", 현재가)
print("PER = ", per)

#13
s = "hello"
t = "python"
print(s+"!",t)

#14
print(2+2*3)

#15
a = 128
print (type(a))

a = "132"
print (type(a))

#16
num_str = "720"
num_int = int(str(num_str))
print(type(num_int))

#17
num = 100
num_str=str(int(num))
print(type(num_str))

#18
num_str = "15.79"
num_float = float(str(num_str))
print(type(num_float))

#19
year="2020"
int_year = int(str(year))
print(type(int_year))
print(int_year-1,int_year-2,int_year-3)

#20
aircon_month = 48584
free_interest = 36
total = aircon_month*free_interest
print(total)