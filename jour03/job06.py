alphabet = "abcdefghijklmnopqrstuvwxyz" * 10

for i in range(1, int((-1 + (1 + 8*len(alphabet))**0.5) // 2) + 1):
    print(alphabet[:i])  
    alphabet=alphabet[i:]
