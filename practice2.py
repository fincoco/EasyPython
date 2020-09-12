#탈출문자
# \n: 줄바꿈
print("백문이 불여일견 백견이 불여일타") 
print("백문이 불여일견 \n백견이 불여일타") 
 # \", \': 따옴표 그대로
print("저는 'finco'입니다")
print('저는 "finco"입니다')
print("저는 \"finco\"입니다")
# \\: 문장내에서 \
print("C:\\Anaconda3\\envs\\JCode\\python")
# \r: 커서를 맨 앞으로 이동(덮어쓰기)
print("Red Apple\rPine")
# \b: 백스페이스(한 글자 삭제), 삭제할 글자 바로 다음에 입력
print("Redd\bApple")
# \t: 탭
print("Red\tapple")

#Quiz_2 사이트별로 비밀번호를 만들어주는 프로그램
#규칙1: http:// 부분은 제외
#규칙2: 처음 만나는 점(.) 이후 부분은 제외
#규칙3: 남은 글자 중 처음 세자리+글자 개수+글자 내 'e'개수+"!"로 구성
url = "http://naver.com"
url = "http://daum.net"
my_str = url.replace("http://", "") #규칙1
my_str = my_str[:my_str.index(".")] #규칙2
pwd = str(my_str[:3])+str(len(my_str))+str(my_str.count("e"))+"!" #규칙3
print(f"{url}의 비밀번호는 {pwd} 입니다.")


#리스트 []
#지하철 칸별로 10, 20, 30명
subway = [10, 20, 30]
print(subway)
subway = ["유재석", "조세호", "박명수"]
print(subway)

#조세호씨가 몇 번쨰 칸에 있는가?
print(subway.index("조세호")) #리스트 인덱스 
#다음 정류장에서 하하씨 승차
subway.append("하하") #리스트 추가(마지막에)
print(subway)
subway.insert(1, "정형돈") #원하는 위치에 리스트 추가
print(subway)
#지하철에 있는 사람 마지막에서 꺼내기
print(subway.pop())
print(subway)
#같은 이름의 사람 몇 명 있는지 확인
subway.append("유재석")
subway.count("유재석")

#정렬
num_list = [5, 2, 4, 3, 1]
num_list.sort()
print(num_list)
#순서 뒤집기
num_list.reverse()
print(num_list)
#모두 지우기
num_list.clear()
print(num_list)

#다양한 자료형 함께 사용
mix_list = ["조세호", 20, True]
print(mix_list)
#리스트 확장
num_list.extend(mix_list) #오른쪽으로 리스트 확장
print(num_list)


#사전(Dictionary)
cabinet = {3: "유재석", 100: "김태호"}
#key 가져오기
print(cabinet[3])
print(cabinet.get(3))

print(cabinet[5]) #없는 key를 입력하면 프로그램 종료됨
print(cabinet.get(5)) #get()을 이용하면 자료가 없을 시 None 출력
print(cabinet.get(5, "사용 가능")) #바로 추가해서 사용할 수 있음(원래 사전에는 저장되지 않음)

print(3 in cabinet) #boolean으로 존재하는 key 확인 가능
print(5 in cabinet)

cabinet = {"A-3": "유재석", "B-100": "김태호"}
print(cabinet)
#추가
cabinet["C-20"] = "조세호" #key와 value 추가 or 업데이트
print(cabinet)

#삭제
del cabinet["A-3"]
print(cabinet)

#key 들만 출력
print(cabinet.keys())
#value만 출력
print(cabinet.values())
#key, value 모두 출력
print(cabinet.items())

#모두 삭제
cabinet.clear()
print(cabinet)


#튜플(내용 변경 및 추가 불가능, 속도는 빠름)
menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

name = "김종국"
age = 20
hobby = "코딩"
print(name, age, hobby)

name, age, hobby = ("유재석", 30, "축구")
print(name, age, hobby)

#집합(set); 중복 안됨, 순서 없음
my_set = {1, 2, 3, 3, 3}
print(my_set) #{1, 2, 3}

#교집합 출력
java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])
print(java & python)
print(java.intersection(python))

#합집합 출력
print(java | python)
print(java.union(python))

#차집합 출력
print(java - python)
print(java.difference(python))

#집합에 변수 추가
python.add("김태호")
print(python)

#제거
java.remove("김태호")
print(java)


#자료구조의 변경
menu = {"커피", "우유", "주스"} #세트로 생성
print(menu)
print(menu, type(menu))

menu = list(menu) #리스트 구조로 변경
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))

#Quiz_4
#파이썬 코딩 대회 댓글 이벤트, 추첨 통해 1명은 치킨, 3명은 커피 쿠폰
#조건1: 편의상 댓글은 20명이 작성, 아이디는 1~20
#조건2: 댓글 내용과 상관없이 무작위로 추첨하되 중복 불가
#조건3: random 모듈의 shuffle과 sample을 활용

from random import *
id = list(range(1, 21)) #range는 마지막 수 포함하지 않음
shuffle(id)
print(id)

winners = sample(id, 4) #리스트에서 변수 무작위로 뽑기
print(winners)
print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}" .format(winners[0]))
print("커피 당첨자 : {0}" .format(winners[1:]))
print("-- 축하합니다 --")
