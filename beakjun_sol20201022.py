#1 세자리수 X 세자리수의 세로 계산식을 작성하시오.
'''
num_1 = int(input("첫 번째 세자리수를 입력하세요 : "))
num_2 = int(input("두 번째 세자리수를 입력하세요 : "))

Q2=num_2//10**2 # 첫번째/100
R1=num_2%10**2 # 첫번째수의 십의자리

Q3=R1//10 # 첫번째수의 십의자리 / 10
R2=R1%10 # 첫번째수의 십의자리의 일의자리

print(R2*num_1)
print(Q3*num_1)
print(Q2*num_1)
print(num_1*num_2)
'''

#2 R1 와 R2의 평균 S. R1과 S를 이용하여 R2를 구하라
'''

R1 = int(input("첫 번째 수를 입력하시오 (-1000 ~ 1000 사이) : "))
S = int(input("평균을 입력하시오 (-1000 ~ 1000 사이) : "))

R2 = 2*S-R1 # 이걸 조금 편하게 할 수 있는 방법이 없을까?

print("두 번째 수는 ? ", R2)
'''

