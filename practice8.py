#모듈 사용과 불러오기
#theater_module.py 파일
import theater_module
theater_module.price(3)
theater_module.price_morning(4)
theater_module.price_soldier(5)

import theater_module as mv #모듈 이름을 mv로 가져오기
mv.price(3)
mv.price_morning(4)
mv.price_soldier(5)

from theater_module import *
price(3)
price_morning(4)
price_soldier(5)

from theater_module import price, price_morning #특정 함수만 입력할 수도 있음

from theater_module import price_soldier as price #price_soldier 함수의 이름이 price로 가져오기


#패키지(여러 모듈 파일의 집합)
#travel폴더가 패키지가 됨.
import travel.thailand #모듈이나 패키지만 import 바로 할 수 있음/클래스는 호출 안 됨.
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()

from travel.thailand import ThailandPackage
trip_too = ThailandPackage()
print(trip_too)
trip_too.detail()

from travel import vietnam
trip_to = vietnam.VietnamPackage()
trip_to.detail()

#__all__
from travel import * #*을 통해 공개된 모든 패키지 불러오기 가능(범위 설정 해야줘야 함.)
trip_to = vietnam.VietnamPackage()
trip_to.detail()

#모듈 직접 실행
from travel import * 
trip_to = ThailandPackage()
trip_to.detail()


#패키지, 모듈 위치
from travel import *
import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(thailand))


#pip install, pypi 검색해서 쉽게 설치
#beatiful soup, 웹스크래핑
#pip list, 깔려 있는 pip 종류 확인
#pip show 패키지명, 해당 패키지에 대한 설명
#pip install --upgrade 패키지명, 패키지 업그레이드
#pip uninstall 패키지명, 패키지삭제
pip install beautifulsoup4
from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())


#내장함수(python builtibns)
#input: 사용자 입력을 받는 함수
lang = input("무슨 언어를 좋아하세요?")
print("{0}은 아주 좋은 언어입니다." .format(lang))

#dir: 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
print(dir())
import random #외장함수
print(dir())
print(dir(random))

lst = [1, 2, 3]
print(dir(lst))

#외장함수(python module index)
#glob: 경로 내의 폴더/파일 목록 조회
import glob
print(glob.glob("*.py")) #py로 끝나는 파일 모두 찾기

#os: 운영체제에서 제공하는 기본 기능
import os
print(os.getcwd())

folder = "sample_dir"
if os.path.exists(folder):
    print("이미 존재하는 폴더입니다.")
    os.rmdir(folder)
    print(folder, "폴더를 삭제하였습니다.")
else:
    os.makedirs(folder) #폴더 생성
    print(folder, "폴더를 생성하였습니다.")

print(os.listdir())

#time
import time
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S"))

#datetime
import datetime
print("오늘 날짜는 ", datetime.date.today())