# 알람 시계

H, M = input().split()
H = int(H)
M = int(M)

if H == 0:
    if M < 45:
        print(23, M+15)
    else:
        print(0, M-45)
else:
    if M < 45:
        print(H-1, M+15)
    else:
        print(H, M-45)