# # 15649: N과 M (1)
# import sys
# from itertools import product 
# from itertools import permutations 
# from itertools import combinations
# N, M = map(int, sys.stdin.readline().split())
# number_list = list(range(1, N + 1))
# permutation_list = list(permutations(number_list, M)) # 순열 뽑기
# for i in permutation_list:
#     print(*i)



# # 15650: N과 M (2)
# import sys
# import itertools
# N, M = map(int, sys.stdin.readline().split())
# number_list = list(range(1, N + 1))
# combination_list = itertools.combinations(number_list, M)
# for i in combination_list:
#     print(*i)



# # 15651: N과 M (3)
# import sys
# import itertools
# N, M = map(int, sys.stdin.readline().split())
# num_list = list(range(1, N + 1))
# product_list = itertools.product(num_list, repeat = M) # product(반복 가능한 객체, repeat = 1(기본))
# for i in product_list:
#     print(*i)



# # 15652: N과 M (4)
# import sys
# import itertools
# N, M = map(int, sys.stdin.readline().split())
# num_list = list(range(1, N + 1))
# combi_replace = itertools.combinations_with_replacement(num_list, M)
# for i in combi_replace:
#     print(*i)



# 9663: N-Queen
import sys
def chess(n):
    # 체스판 만들기: 열과 행의 방식으로
    row = [0] * n
    column = [0] * n
    
    # 경우의 수 세기
    
            
    
    





    
