def maior_primo(n):
    for i in range(n, 1, -1):
        primo = True
        for j in range(2, i):
            if i % j == 0:
                primo = False
                break
        if primo:
            return i