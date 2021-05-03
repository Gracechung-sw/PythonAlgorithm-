# T = int(input())

# for t in range(T):  
#     N, s, e, k = map(int, input().split())

#     arr = list(map(int, input().split()))
#     arr = arr[s-1:e].sort()

#     print('#' + t+1 + ' ' + arr[k-1])

T = int(input())

for i in range(T):
    n, s, e, k = map(int, input().split())
    num_list = list(map(int, input().split()))
    answer = sorted(num_list[s-1:e])[k-1]
    print("#{} {}".format(i+1, answer))