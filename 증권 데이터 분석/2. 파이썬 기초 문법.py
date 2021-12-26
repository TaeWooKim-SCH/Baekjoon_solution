# for 반복문
for i in [1, 3, 5] :
    print(i)
 # range([시작값,] 멈춤값[, 증가값])
for i  in range(1, 7, 2) :
    print(i)

 # enumerate(반복자료형[, 인덱스의 시작값])
FAANG = ['FB', 'AMZN', 'AAPL', 'NFLX', 'GOOGL']
for idx, symbol in enumerate(FAANG, 1) :
    print(idx, symbol)


# while 반복문
i = 1
while i < 7 :
    print(i)
    i += 2
 # while else 와 for else
i = 0
while i >= 0 :
    i += 1
    if i % 2 == 0 :
        continue
    if i > 5 :
        break
    print(i)
else :
    print('Condition is False.')


# try except 예외 처리
try :
    1 / 0 
except Exception as e :
    print('Exception occured :', str(e))


# 리스트 내포
nums = [1, 2, 3, 4, 5]
squares = []
for x in nums :
    squares.append(x ** 2)
print(squares)

squares = [x ** 2 for x in nums]
print(squares)

even_squares = [x ** 2 for x in nums if x % 2 == 0]
print(even_squares)


# {키:값} 형태 딕셔너리
crispr = {'EDIT': 'Editas Medicine', 'NTLA': 'Itellia Therapeutics'}
crispr['CRSP'] = 'CRISPR Therapeutics'
print(crispr)
print(len(crispr))


# 문자열 포맷 출력
 # % 기호 방식
for x in crispr :
    print('%s: %s' %(x, crispr[x]))

 # {} 기호 방식
for x in crispr :
    print('{}: {}'.format(x, crispr[x]))

 # f-string 방식
for x in crispr :
    print(f'{x}: {crispr[x]}')


# 타임잇으로 성능 측정하기 ==> timeit(테스트 구문, steup = 테스트 준비 구문, number = 테스트 반복 횟수)
 # 순회 속도 비교하기
import timeit
iteration_test = """
for i in itr :
    pass
"""
print(timeit.timeit(iteration_test, setup = 'itr = list(range(10000))', number = 1000))
print(timeit.timeit(iteration_test, setup = 'itr = tuple(range(10000))', number = 1000))
print(timeit.timeit(iteration_test, setup = 'itr = set(range(10000))', number = 1000))

 # 검색 속도 비교하기
search_test = """
import random
x = random.randint(0, len(itr) - 1)
if x in itr :
    pass
"""
print(timeit.timeit(search_test, setup = 'itr = list(range(10000))', number = 1000))
print(timeit.timeit(search_test, setup = 'itr = tuple(range(10000))', number = 1000))
print(timeit.timeit(search_test, setup = 'itr = set(range(10000))', number = 1000))


# 변수
 # 예약어: 변수명으로 사용할 수 없는 단어
help('keywords')


# 함수
 # 연평균 성장률(CAGR: Compound Annual Growth Rates) 구하기
def getCAGR(first, last, years) :
    return (last / first) ** (1 / years) - 1
    # 삼성전자 예시
cagr = getCAGR(65300, 2669000, 20)
print("SEC CAGR: {:.2%}".format(cagr))

 # 메서드
    # 클래스에 속하지 않는 함수를 함수라고 하고, 클래스에 속하는 함수를 메서드로 구분.
    

# 모듈
 # help() 함수
help('modules')
help('modules time')
help('datetime')

 # import
    # import 모듈명
    # import 패키지명.모듈명
import keyword
print(keyword.kwlist)
print(keyword.__file__)

 # from ~ import ~
    # from 모듈명 import 클래스명, 함수명 등
    # from 패키지명 import 모듈명
import calendar
print(calendar.month(2020, 1)) # 모듈명(calendar) 생략불가
from calendar import month
print(month(2020, 1)) # 모듈명(calendar) 생략 가능

 # import ~ as ~ : 이름이 긴 모듈명을 프로그래머가 원하는 별칭으로 줄여서 사용할 수 있다.
    # import 이름이 긴 모듈명 as 별칭
    # from ~ import ~ as 별칭
from datetime import datetime as dt    
print(dt.now()) # 별칭(dt)


# 패키지
import urllib.request
print(type(urllib.request))

 # 파이썬의 선
import this


# 클래스
class MyFirstClass :
    clsVar = 'The best way to predict the futuer is to invent it'
    def clsMethod(self) :
        print(MyFirstClass.clsVar + '\t- Alan Curtis Katy -')
mfc = MyFirstClass() # 인스턴스화
print(mfc.clsVar) # 클래스 변수에 접근
mfc.clsMethod() # 클래스 메서드 호출


# 상속
 # class 자식 클래스(부모 클래스 1, 부모 클래스 2, ....) :
 #     pass
class A :
    def methodA(self) :
        print("Calling A's methodA")
    def method(self) :
        print("Calling A's method")
class B :
    def methodB(self) :
        print("Calling B's methodB")
class C(A, B) :
    def methodC(self) :
        print("Calling C's methodC")
    def method(self) :
        print("Calling C's overridden method")
        super().method() # 부모의 변수나 메소드를 사용할 때는 super() 내장 함수를 호출하면 된다.
c = C()
c.methodA()
c.methodB()
c.methodC()
c.method() # 자식 클래스에서 부모 클래스와 같은 변수나 메소드가 존재하면 자식 클래스에 정의된 것이 사용된다. 그러나, super().method() 내장 함수를 호출하면 부모 것을 가져옴.


# 클래스 변수와 인스턴스 변수: 클래스 내부에 존재하면서 메서드 밖에 정의된 변수를 클래스 변수, 인스턴스 변수는 메서드 내부에서 정의되며 변수명 앞에 self가 붙음.
 # __del__ 소멸자
class NasdaqStock :
    """Class for NASDAQ stocks""" # 독스트링
    count = 0 # 클래스 변수
    def __init__(self, symbol, price) :
        """Constructor for NasdaqStock""" # 독스트링
        self.symbol = symbol # 인스턴스 변수
        self.price = price # 인스턴스 변수
        NasdaqStock.count += 1
        print('Calling __init__({}, {:.2f}) > count: {}'.format(self.symbol, self.price, NasdaqStock.count))
    def __del__(self) :
        """Destructor for NasdaqStock""" # 독스트링
        print('Calling __del__({})'.format(self))
gg = NasdaqStock('GOOG', 1154.05)
del(gg)
ms = NasdaqStock('MSFT', 102.44)
del(ms)
amz = NasdaqStock("AMZN", 1746.00)
del(amz)
help(NasdaqStock)


# # 파일 처리 및 외부 라이브러리 활용
#  # 리퀘스트로 인터넷에서 이미 파일 가져오기
# import requests
# url = 'http://bit.ly/2JnHnT'
# r = requests.get(url, stream = True).raw

#  # 필로로 이미지 보여주기
# from PIL import Image
# img = Image.open(r)
# img.show()
# img.save('src.png')
