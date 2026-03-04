#첫째 줄에 N(2 <= N <= 1,000), M(1 <= M <= 10,000), K(1 <= K <= 10,000)의 자연수가 주어지며, 각 자연수는 공백으로 구분한다.
#둘째 줄에 N개의 자연수가 주어진다. 각 자연수는 공백으로 구분한다. 단, 각가의 자연수는 1 이상 10,000 이하의 수로 주어진다.
#입력으로 주어지는 K는 항상 M보다 작거나 같다.

#출력조건: 첫째 줄에 큰 수의 법칙에 따라 더해진 답을 출력한다.

n, m, k = map(int, input("N M K 입력>> ").split())
n_list = list(map(int, input("N개의 자연수 입력>> ").split()))

n_list.sort(reverse=True)

mm = m // k
kk = m % k

result = n_list[0] * k * mm + n_list[1] * kk
print(result)
