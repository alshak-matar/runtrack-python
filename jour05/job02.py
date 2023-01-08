
ligne = int(input("combien de ligne ?: "))
colonne = int(input("combien de colonnes ?: "))


for i in range(ligne):
        if (i== 0) or i == ligne -1:
            print('|' + ('-'*(colonne-2)) + '|' )
        else :
            print('|' +(' '*(colonne-2)) + '|')
