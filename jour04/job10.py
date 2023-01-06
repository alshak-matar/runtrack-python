def produit():
    L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
    x = []

    for i in L:
        if i>=25 and i<=90:
            x.insert(1,i)

    produit = 1

    for i in x:
        produit = produit * i
    print(produit)

produit() 
