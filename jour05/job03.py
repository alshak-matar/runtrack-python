ligne = int(input("combien de ligne et colone ?: "))

def tapis(n):
    for i in range(n+1):
        if (i == 0) or (i == n):
            print('+' + ('-'*(n)) + '+')
        else :
            print('|' + '#'* (n-(i+1)) + ' ' + '#'*(i-1) + '|')
tapis(ligne)
