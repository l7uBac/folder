for k in range(3, 21):
    password = ''
    for i in range(1, k):
        for j in range(i + 1, k):
            if k % (i + j) == 0:
                password += str(i)
                password += str(j)

    print(k)
    print(password)
