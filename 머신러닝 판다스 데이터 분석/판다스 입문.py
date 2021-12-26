# #  1. 데이터 과학자가 판다스를 배우는 이유


# # 2. 판다스 자료구조
#     # 2-1. 시리즈
#         # 데이터가 순차적으로 나열된 1차원 배열의 형태를 갖는다.
#         # 파이썬 딕셔너리와 비슷한 형태
#         # 시리즈 만들기: pandas.Series(딕서너리)
#             # 예제 1-1: 딕셔너리 -> 시리즈 변환
# # 판다스 불러오기
# import pandas as pd
# # key:value 쌍으로 딕셔너리를 만들고, 변수 dict_data에 저장
# dict_data = {"a": 1, "b": 2, "c": 3}
# # 판다스 Series() 함수로 dictionary를 Series로 변환. 변수 sr에 저장
# sr = pd.Series(dict_data) 
# # sr의 자료형 출력
# print(type(sr))
# print("\n")
# # 변수 sr에 저장되어 있는 시리즈 객체를 출력
# print(sr)
# print(dict_data)

#         # 인덱스 구조
#             # 예제 1-2: 시리즈 인덱스
# import pandas as pd
# # 리스트를 시리즈로 변환하여 변수 sr에 저장
# list_data = ['2019-01-02', 3.14, 'ABC', 100, True] 
# sr = pd.Series(list_data)
# print(sr)
# # 인덱스 배열은 변수 idx에 저장. 데이터 값 배열은 변수 val에 저장
# idx = sr.index
# val = sr.values
# print(idx)
# print("\n")
# print(val)

#        # 원소 선택
#             # 예제 1-3: 시리즈 원소 선택
# import pandas as pd
# # 튜플을 시리즈로 변환(인덱스 옵션 지정)
# tup_data = ('영인', '2010-05-01', '여', True)
# sr = pd.Series(tup_data, index = ['이름', '생년월일', '성별', '학생여부'])
# print(sr)
# print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
# # 원소를 1개 선택
# print(sr[0])
# print(sr['이름'])
# print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
# # 여러 개의 원소를 선택(인덱스 리스트 활용)
# print(sr[[1, 2]]) # 여러개를 직접 선택할 때에는 대괄호안에 인덱스를 리스트 형태로 입력해야 함. (범위 지정은 다름)
# print('\n')
# print(sr[['생년월일', '성별']])
# print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
# # 여러 개의 원소를 선택(인덱스 범위 지정)
# print(sr[1:2])
# print('\n')
# print(sr['생년월일':'성별']) # 인덱스 이름을 사용하면 범위의 끝(성별)이 포함됨


#     # 2-2 데이터프레임
#         # 딕셔너리 -> 데이터프레임 변환: pandas.DataFrame(딕셔너리 객체)
#         # 데이터프레임 만들기
#             # 예제 1-4: 딕셔너리 -> 데이터프레임 변환
# import pandas as pd
# # 열 이름을 key로 하고, 리스트를 value로 갖는 딕셔너리 정의(2차원 배열)
# dict_data = {'c0': [1, 2, 3], 'c1': [4, 5, 6], 'c2': [7, 8, 9], 'c3': [10, 11, 12], 'c4': [13, 14, 15]}
# # 판다스 DataFrame() 함수로 딕셔너리를 데이터프레임으로 변환. 변수 df에 저장
# df = pd.DataFrame(dict_data)
# # df의 자료형 출력
# print(type(df))
# print('\n')
# # 변수 df에 저장되어 있는 데이터프레임 객체를 출력
# print(df)

#         # 행 인덱스/열 이름 설정: pandas.DataFrame(2차원 배열, index: 행 인덱스 배열, columns = 열 이름 배열)
#             # 예제 1-5: 행 인덱스/열 이름 설정
# import pandas as pd
# # 행 인덱스/열 이름 지정하여 데이터프레임 만들기
# df = pd.DataFrame([[15, '남', '덕영중'], [17, '여', '수리중']], 
#                     index = ['준서', '예은'], 
#                     columns = ['나이', '성별', '학교'])
# # 행 인덱스, 열 이름 확인하기
# print(df) # 데이터프레임
# print('\n')
# print(df.index) # 행 인덱스
# print('\n')
# print(df.columns) # 열 이름
# print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
# # 행 인덱스, 열 이름 변경하기
# df.index = ['학생1', '학생2'] # DataFrame 객체.index = 새로운 행 인덱스 배열
# df.columns = ['연령', '남녀', '소속'] # DataFrame 객체.columns = 새로운 열 이름 배열
# print(df) # 데이터프레임
# print("\n")
# print(df.index) # 행 인덱스
# print('\n')
# print(df.columns) # 열 이름

#             # 예제 1-6: 행 인덱스/열 이름 변경
# import pandas as pd
# # 행 인덱스/열 이름을 지정하여 데이터프레임 만들기
# df = pd.DataFrame([[15, '남', '덕영중'], [17, '여', '수리중']], 
#                     index = ['준서', '예은'],
#                     columns = ['나이', '성별', '학교'])
# # 데이터프레임 df 출력
# print(df)
# print('\n')
# # 열 이름 중, '나이'를 '연령'으로, '성별'을 '남녀'로, '학교'를 '소속'으로 바꾸기
# df.rename(columns = {'나이': '연령', '성별': '남녀', '학교': '소속'}, inplace = True) # DataFrame 객체.rename(columns = {기존 이름: 새 이름})
# # df의 행 인덱스 중에서, '준서'를 '학생1'로, '예은'을 '학생2'로 바꾸기
# df.rename(index = {'준서': '학생1', '예은': '학생2'}, inplace = True) # DataFrame 객체.rename(index = {기존 인덱스: 새 인덱스})
# # df 출력(변경 후)
# print(df)

#         # 행/열 삭제
#             # 예제 1-7: 행 삭제
# import pandas as pd
# # DataFrame() 함수로 데이터프레임 변환. 변수 df에 저장
# exam_data = {'수학': [90, 80, 70], '영어': [98, 89, 95], 
#             '음악': [85, 95, 100], '체육': [100, 90, 90]}
# df = pd.DataFrame(exam_data, index = ['서준', '우현', '인아'])
# print(df)
# print('\n')
# # 데이터프레임 df를 복제하여 변수 df2에 저장. df2의 1개 행(row) 삭제
# df2 = df[:]
# df2.drop('우현', inplace = True)
# print(df2)
# print('\n')
# # 데이터프레임 df를 복제하여 변수 df3에 저장. df3의 2개 행(row) 삭제
# df3 = df[:]
# df3.drop(['우현', '인아'], axis = 0, inplace = True) # DataFrame 객체.drop(행 인덱스 또는 배열, axis = 0)
# print(df3)

#             # 예제 1-8: 열 삭제
# import pandas as pd
# # DataFrame() 함수로 데이터프레임 변환. 변수 df에 저장
# exam_data = {'수학': [90, 80, 70], '영어': [98, 89, 95], 
#             '음악': [85, 95, 100], '체육': [100, 90, 90]}
# df = pd.DataFrame(exam_data, index = ['서준', '우현', '인아'])
# print(df)
# print('\n')
# # 데이터프레임 df를 복제하여 변수 df4에 저장. df4의 1개 열(column) 삭제
# df4 = df.copy()
# df4.drop('수학', axis = 1, inplace = True) # DataFrame 객체.drop(열 이름 또는 배열, axis = 1)
# print(df4)
# print('\n')
# # 데이터프레임 df를 복제하여 변수 df5에 저장. df5의 2개 열(column) 삭제
# df5 = df.copy()
# df5.drop(['영어', '체육'], axis = 1, inplace = True)
# print(df5)

#         # 행 선택
#             # 예제 1-9: 행 선택
# import pandas as pd
# # DataFrame() 함수로 데이터프레임 변환. 변수 df에 저장
# exam_data = {'수학': [90, 80, 70], '영어': [98, 89, 95], 
#             '음악': [85, 95, 100], '체육': [100, 90, 90]}
# df = pd.DataFrame(exam_data, index = ['서준', '우현', '인아'])
# print(df)
# print('\n')
# # 행 인덱스를 사용하여 행 1개 선택
# label1 = df.loc['서준'] # 인덱스 이름을 이용하여 선택
# position1 = df.iloc[0] # 정수형 위치 인덱스를 이용하여 선택
# print(label1)
# print('\n')
# print(position1)
# # 행 인덱스를 사용하여 2개 이상의 행 선택
# label2 = df.loc[['서준', '우현']]
# position2 = df.iloc[[0, 1]]
# print(label2)
# print('\n')
# print(position2)
# # 행 인덱스의 범위를 지정하여 행 선택
# label3 = df.loc['서준':'우현']
# position3 = df.iloc[0:1]
# print(label3)
# print('\n')
# print(position3)

        # 열 선택
            # 예제 1-10: 열 선택
import pandas as pd
# DataFrame() 함수로 데이터프레임 변환. 변수 df에 저장
exam_data = {'이름': ['서준', '우현', '인아'], 
            '수학': [90, 80, 70], 
            '영어': [98, 89, 95],
            '음악': [85, 95, 100],
            '체육': [100, 90, 90]}
df = pd.DataFrame(exam_data)
print(df)
print(type(df))
print('\n')
# '수학' 점수 데이터만 선택. 변수  math1에 저장
math1 = df['수학']
print(math1)
print(type(math1))
print('\n')
# '영어' 점수 데이터만 선택. 변수 english에 저장
english = df.영어
print(english)
print(type(english))
print('\n')
# '음악', '체육' 점수 데이터를 선택. 변수 music_gym에 저장
music_gym = df[['음악', '체육']]
print(music_gym)
print(type(music_gym))
print('\n')
# '수학' 점수 데이터만 선택. 변수 math2에 저장
math2 = df[['수학']]
print(math2)
print(type(math2))
