n = int(input())
n_dict = {}
for i in input().split(' '):
    n_dict[i] = 1

m = int(input())
mm = input().split(' ')
m_lst = [0] * m

for i in range(len(mm)):
    try:
        if n_dict[mm[i]]:
            m_lst[i] = 1
    except:
        pass
print(*m_lst, sep="\n")