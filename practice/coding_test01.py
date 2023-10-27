# 입력값 〉	4, 3, [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]

def solution(k, m, score):
    if 3 <= k <= 9 and 3 <= m <= 10:
        score.sort(reverse=True) # 내림차순으로 정렬
        total_price = 0
        
        remains = score.copy()
        while m <= len(remains):
            temp = remains[:m]
            del remains[:m]
            temp.sort() # 오름차순으로 재정렬
            price = temp[0] * m
            total_price += price
            if m > len(remains):
                break
                            
        return total_price
    else:
        answer = 0
        return answer

result = solution(5, 3, [1, 2, 3, 5, 7, 5, 7])
print(result)

"""
채점 결과
정확성: 79.2
합계: 79.2 / 100.0
"""

def solution(k, m, score):
    answer = 0
    if 3 <= k <= 9 and 3 <= m <= 10:
        score.sort(reverse=True) # 내림차순으로 정렬
        remains = score.copy()
        while m <= len(remains):
            temp = remains[:m]
            del remains[:m]
            price = min(temp) * m
            answer += price
            if m > len(remains):
                break
                            
        return answer
    else:
        return answer

"""
채점 결과
정확성: 79.2
합계: 79.2 / 100.0
"""

def solution(k, m, score):
    answer = 0
    if 3 <= k <= 9 and 3 <= m <= 10:
        score.sort(reverse=True) # 내림차순으로 정렬
        i = 0
        while i + m <= len(score):
            temp = score[i : i + m]
            price = min(temp) * m
            answer += price
            i += m
            if m > len(score):
                break
                            
        return answer
    else:
        return answer
    
"""
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
"""
