# 셀프 넘버


def sequence(n):
    seq_list = []
    dn = n
    while True:
        seq_list.append(dn)

        change = dn
        for i in range(len(str(dn))):
            change += int(str(dn)[i])
        dn = change

        if dn > 10000:
            break

    del seq_list[0]
    return set(seq_list)

all_list = [ x for x in range(1, 10001)]
all_list_set = set(all_list)

total_list = {}
for i in range(1, 10000):
    all_list_set = all_list_set - sequence(i)

all_list = list(all_list_set)
all_list.sort()

for i in range(len(all_list)):
    print(all_list[i])
