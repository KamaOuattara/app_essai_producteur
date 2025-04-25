
while True:
    nom_producteur =input("Quel est ton nom ?")
    if nom_producteur.isalpha():
        next
        break
    else:
        print("entrez des lettres")
    
while True :      
    speculation = input("Quel est la speculation ?")
    if speculation.isalpha():
        next
        break
    else:
        print("entrez des lettres")
    
while True :       
    superficie = input("Quel est la superficie ?")
    if superficie.isdigit():
        next
        break
    else:
        print("entrez des nombres")
 
while True :
    production = input("Quel est la production ?")
    if production.isdigit():
        next
        break
    else:
        print("entrez des nombres")
    
prix_kg = 438
certification = True

print("bonjour🫡",nom_producteur ,"vous avez un champ d'",speculation,"d'une superficie de",superficie,"ha","dont la production est de",production,"kg","qui coute",prix_kg,"fcfa/")
