import time 

#베이스라인 만들어 놓기
# 시간 측정 코드 

start_time = time.time()

#n: 배열 크기 
#m: 숫자가 더해지는 횟수 
#k: 연속해서 초과를 할 수 없는 수 
n, m, k = 5, 8, 3 

#배열을 받는 방식을 의미하고 
data = [2,4,5,4,6]

sortedData = sorted(data, reverse=True)

#아예 '큰 수'를 만들어야 하기 때문에, 답안을 보면 가장 큰 수 두 개를 가져와서 연속적으로 더했음 
#그런데 여기서 큰 수를 얼마나 더하는지가 관건임 
#어떻게 하느냐, 전체 횟수에서 나누고, 그 다음에 나머지 수는 두번째로 큰 수를 더하는 데 사용하면 될 것으로 보임 
result = 0 

bigNumber = sortedData[0]
smallNumber = sortedData[1]

bigNumberCount = m // k 
print(bigNumberCount)
smallNumberCount = m % k 


result = result + (bigNumberCount*k*bigNumber)
result = result + (smallNumberCount*smallNumber)



print(result)

end_time = time.time()


print(start_time - end_time )