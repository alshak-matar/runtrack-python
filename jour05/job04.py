mot = input('Entrer le message a modifier : ')
decalage = int(input('Entrer le rang de décalge pour votre message positif vers la droite négatif vers la gauche : '))

def message_code(mot, decalage):
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  code = ''
  for i in mot:
    if i.lower() in alphabet:
      lettre = alphabet.index(i.lower())
      modif = (lettre + decalage) % 26
      lettre_code = alphabet[modif]
      if i.isupper():
        code += lettre_code.upper()
      else:
        code += lettre_code
    else:
      code += i  
  return code
message_code(mot,decalage)

print(message_code(mot,decalage))
