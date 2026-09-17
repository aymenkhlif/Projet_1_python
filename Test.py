print("Bonjour tous le monde ")
print("Hello de Olivier")
class AdresseIPInvalideError(Exception):
    def __init__(self,message):
        super().__init__(message)

def valider_ip(ip):
    parties=ip.split(".")

    if not len(parties)==4:
        raise AdresseIPInvalideError("❌ Erreur: L'adresse ip doit avoir 4 parties.")

    for partie in parties:
        if not partie.isdigit():
            raise AdresseIPInvalideError(f"❌ Erreur: {partie} n'est pas un entier valide.")

        nombre=int(partie)

        if not 0<=nombre<=255:
            raise AdresseIPInvalideError("❌ Erreur : l'adresse ip doit etre entre 0 et 255.")
while True :
    try:
        ip=input("Entrez l'adresse ip : ")
        valider_ip(ip)
        print("adresse ip valide")
        break
    except AdresseIPInvalideError as e:
        print(e)
