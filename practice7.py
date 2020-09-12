#예외처리(error)
try: 
    print("나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요: "))
    num2 = int(input("두 번째 숫자를 입력하세요: "))
    print("{0}/{1} = {2}" .format(num1, num2, int(num1/num2)))
except ValueError: #에러가 발생했을 때 except에 있는 명령을 실행
    print("에러! 잘못된 값을 입력했습니다")
except ZeroDivisionError as err: #error내용이 출력
    print(err)

try: 
    print("나누기 전용 계산기입니다.")
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력하세요: ")))
    nums.append(int(input("두 번째 숫자를 입력하세요: ")))
    #nums.append(int(nums[0]/nums[1]))
    print("{0}/{1} = {2}" .format(nums[0], nums[1], nums[2]))
except ValueError: #에러가 발생했을 때 except에 있는 명령을 실행
    print("에러! 잘못된 값을 입력했습니다")
except ZeroDivisionError as err:
    print(err)
except Exception as err:
    print("알 수 없는 에러가 발생하였습니다") #위에서 설정한 에러 외에 다른 모든 에러 처리
    print(err)

#에러 발생시키기 
try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요: "))
    num2 = int(input("두 번째 숫자를 입력하세요: ")) 
    if num1 >= 10 or num2 >= 10:
        raise ValueError #두자리 이상 수 자체를 에러값으로 처리, 에러 처리하는 구문으로 바로 이동 
    print("{0}/{1} = {2}" .format(num1, num2, int(num1/num2)))
except ValueError: 
    print("에러! 잘못된 값을 입력했습니다")

#사용자 정의 예외 처리
class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요: "))
    num2 = int(input("두 번째 숫자를 입력하세요: ")) 
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError("입력값: {0}, {1}" .format(num1, num2))
    print("{0}/{1} = {2}" .format(num1, num2, int(num1/num2)))
except BigNumberError as err:
    print("에러! 잘못된 값을 입력했습니다")
    print(err)


#finally; 에러가 발생하든 말든 마지막에 실행됨
class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요: "))
    num2 = int(input("두 번째 숫자를 입력하세요: ")) 
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError("입력값: {0}, {1}" .format(num1, num2))
    print("{0}/{1} = {2}" .format(num1, num2, int(num1/num2)))
except BigNumberError as err:
    print("에러! 잘못된 값을 입력했습니다")
    print(err)
finally:
    print("계산기를 이용해주셔서 감사합니다.")


#Quiz_9
#항상 대기 손님이 있는 치킨집의 자동 주문 시스템.
#조건1: 1보다 작거나 숫자가 아닌 입력값이 들어올 때는 ValueError로 처리
#      출력메세지: "잘못된 값을 입력하였습니다."
#조건2: 대기 손님이 주문할 수 있는 총량은 10마리 한정. 치킨 소진시 사용자 정의 에러 발생 시키고 프로그램 종료
#      출력메세지: "재고가 소진되어 더 이상 주문을 받지 않습니다."
class SoldOutError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

chicken = 10
waiting = 1
while(True):
    try: 
        print("[남은 치킨: {0}]" .format(chicken))
        order = int(input("치킨 몇 마리 주문하시겠습니까?"))
        if order > chicken:
            print("재료가 부족합니다.")
        elif order <=0:
            raise ValueError
        else:
            print("[대기번호 {0}] {1}마리 주문이 완료되었습니다." .format(waiting, order))
            waiting += 1
            chicken -= order
        
        if chicken == 0:
            raise SoldOutError("재료가 소진되어 더 이상 주문을 받지 않습니다.")

    except ValueError:
        print("잘못된 값을 입력하였습니다.")
    except SoldOutError as err:
        print(err)
        break #while문 탈출

