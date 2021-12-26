# 3.1 넘파이 배열
 # 3.1.1 배열 생성
import numpy as np
A = np.array([[1, 2,], [3, 4]])
print(A)


 # 3.1.2 배열 정보 보기
print(type(A))
print(A.ndim) # 배열의 차원
print(A.shape) # 배열 크기
print(A.dtype) # 원소 자료형


 # 3.1.3 배열의 접근
print(A[0], A[1])
print(A[0, 0], A[0, 1])
print(A[1, 0], A[1, 1])
print(A[A > 1])


 # 3.1.4 배열 형태 바꾸기
print(A)
print(A.T) # A.transpose()와 같다. 주대각선을 기준으로 뒤바꾸는 함수.
print(A)
print(A.flatten()) # flatten() 함수는 다차원 배열을 1차원 배열로 바꿔줌.


 # 3.1.5 배열의 연산
print(A)
print(A + A)
print(A - A)
print(A * A)
print(A / A)


 # 3.1.6 브로드캐스팅
print(A)
B = np.array([10, 100])
print(A * B)


 # 3.1.7 내적 구하기
print(B.dot(B))
print(A.dot(B))



# 3.2 팬더스 시리즈
 # 3.2.1 시리즈 생성
import pandas as pd
s = pd.Series([0.0, 3.6, 2.0, 5.8, 4.2, 8.0]) # 리스트로 시리즈 생성
print(s)


 # 3.2.2 시리즈의 인덱스
s.index = pd.Index([0.0, 1.2, 1.8, 3.0, 3.6, 4.8]) # 인덱스 변경
s.index.name = 'MY_IDX' # 인덱스명 설정
print(s)
s.name = 'MY_SERIES'
print(s)