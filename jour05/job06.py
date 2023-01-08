note=[]

while True:
    note_entrer = input('entrer les notes : ')
    if note_entrer == "":
        break
    else:
        note.append(float(int(note_entrer)))
        
def calcule_note(note):
    r=[]
    for i in note : 
        if i % 5 >= 3 :
            x = 5 - ( i % 5 )
            i =  i + x
            r.append(i)
        else:
            r.append(i)
    return r
print(calcule_note(note))
