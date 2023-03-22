n = int(input())
m = int(input())

if m > 0:
    channel = list(map(int, input().split()))
else:
    channel = []

minV = abs(n-100)
for i in range(1000001):
    for num in str(i):
        if int(num) in channel:
            break
    else:
        minV = min(minV, len(str(i)) + abs(i - n))
print(minV)








# now = 100
# can = []
# cann = set()
# cnt = [abs(n-100)]


# if m == 0:
#     cnt.append(len(str(n)))
# elif m == 10:
#     pass
# else:
#     for i in str(n):
#         j = int(i)
#         k = int(i)
#         while j in channel:
#             j -= 1
#             if j < 0:
#                 j += 10
        
#         while k in channel:
#             k += 1
#             if k >9:
#                 k -= 10
        
#         can.append([j, k])
# print(can)

# def s(st, l, i):
#     if l == len(str(n)) - 1:
#         if can[l][i] < 0 or can[l][i] >9:
#             return
#         else:
#             cann.add(st + str(can[l][i]))
#             return st + str(can[l][i])
#     else:
#         if can[l][i] < 0 or can[l][i] >9:
#             return
#         else:
#             s(st + str(can[l][i]), l+1, 0)
#             s(st + str(can[l][i]), l+1, 1)

# if m!= 0:
#     s('', 0, 0)
#     s('', 0, 1)
# for i in cann:
#     cnt.append(abs(int(i)-n) + len(str(i)))
# print(cann)
# print(min(cnt))