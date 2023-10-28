# ex. [[3, 2], [3, 4], [7, 2], [7, 4]]

def solution(v):
    xs = []
    ys = []

    for point in v:
        xs.append(point[0])
        ys.append(point[1])
    
    # x좌표 찾기
    for x in xs:
        if xs.count(x) == 1:
            missing_x = x
    
    # y좌표 찾기
    for y in ys:
        if ys.count(y) == 1:
            missing_y = y
    
    result = [missing_x, missing_y]
    
    return result

"""
채점 결과
정확성: 100.0
효율성: 0.0
합계: 100.0 / 100.0
"""
    
    

     


    print('Hello Python')

    return answer

