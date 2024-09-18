import time 

#베이스라인 만들어 놓기
# 시간 측정 코드 

start_time = time.time()

n, m = 3, 3
data = [[3, 1, 2],[4, 1, 4],[2, 2, 2]]
newArray = list()

for element in data :
    result = min(element)
    newArray.append(result)

print(max(newArray))


end_time = time.time()


print(start_time - end_time )