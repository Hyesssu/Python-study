
#9

print("="*40)
print("1. 전원 끄기")
print("2. 전원 켜기")
print("3. 볼륨 조절")
print("4. 채널 조절")
print("5 현재의 상태 출력")
print("6. 프로그램 종료")
print("="*40)

choice = int(input("원하는 기능의 번호를 입력하세요 >> "))
power_default = 0
setVolumn_default=0
setChannel_default=0

def power() :
    global power_default
    global power_change
    if power_default == 0 :
        if power_change == 0 :
            print("이미 꺼졌습니다.")
    else :
        if power_change == 1 :
            print("이미 켜졌습니다.")
    return power_default

def setVolumnUp(size) :
    global setVolumn_default
    setVolumn_default+=size
    if setVolumn_default >20 :
        setVolumn_default = 20
    return setVolumn_default

def setVolumnDown(size) :
    global setVolumn_default
    setVolumn_default+=size
    if setVolumn_default <1 :
        setVolumn_default = 1
    return setVolumn_default

def setChannelUp(size) :
    global setChannel_default
    setChannel_default += size
    if setChannel_default > 10 :
        setChannel_default = 10
    return setChannel_default

def setChannelDown(size) :
    global setChannel_default
    setChannel_default += size
    if setChannel_default <1 :
        setChannel_default = 1
    return setChannel_default

def getNow() :
    global setChannel_default
    global setVolumn_default
    global power_default
    
    if power_default == 0 :
        print("꺼졌습니다.", "볼륨 : "+str(setVolumn_default), ", 채널 : "+str(setChannel_default))
    else :
        print("켜졌습니다.", "볼륨 : "+str(setVolumn_default), ", 채널 : "+str(setChannel_default))

while choice != 6 :
    
    if choice == 1 :
        power_change = 0
        power()
        power_default = 0

    elif choice == 2 :
        power_change = 1
        power()
        power_default = 1

    elif choice == 3 :
        if power_default == 1 :
            size = int(input("조절할 볼륨 크기를 입력하세요 : "))
            if size >0 :
                setVolumnUp(size)
            else :
                setVolumnDown(size)
        else :
            print("Tv가 꺼져있습니다.")

    elif choice == 4 :
        if power_default == 1 :
            size = int(input("채널을 입력해주세요 : "))
            if size >0 :
                setChannelUp(size)
            else :
                setChannelDown(size)
        else :
            print("Tv가 꺼져있습니다.")

    elif choice == 5 :
        getNow()
    
    
    choice = int(input("원하는 기능의 번호를 입력하세요 >> "))
