#Mert Erciyas 99058235
# Solicitatie print
# ""

# personCompitence = ["0_personErvaring", "1_mboDiploma", "2_vrachtWagenRijbewijs", "3_bezittingHoed", "4_certificaat"]
# personPhysical = ["0_naam", "1_haar", "2_lengte", "3_gewicht"]
# distraction = ["0_sokken", "1_artiest", "2_pepsi", "3_eten"]


# 


# # Vragen voor iedereen
# lengte = int(input("hoelang bent u?\n")) 
# if lengte >= 180:
#     lengte = True
# elif lengte < 180:
#     lengte = False
# else:
#     print("invalid input, exiting program")
#     exit()
# gewicht = int(input("Hoeveel weegt u?\n"))
# if gewicht >= 90:
#     gewicht = True
# elif gewicht < 90:
#     gewicht = False
# certificaat = input("Heeft u een certificaat van Overleven met gevaarlijke personeel? (J/N)\n")
# if certificaat == "J":
#     certificaat = True
# elif certificaat == "N":
#     certificaat = False
# # Vragen die niet uitmaken
# sokken = input("Wat voor merk sokken draagt u graag?\n")
# artiest = input("Wat is u favoriete artiest\n")
# pepsi = input("Coca cola of Pepsi?\n   ")
# eten = input("Wat is u favoriete eten?\n")

# if naam == True and personErvaring == True and mboDiploma == True and vrachtWagenRijbewijs == True and bezittingHoed == True and haar == True and lengte == True and gewicht == True and certificaat == True:
#     print("U bent aangenomen ", naam, "!")
# else:
#     print("U bent helaas niet angenomen ", naam, "!")

from unicodedata import numeric


def solicitatieFormulier():
    print("\n\
    ----------------------------------------------\n\
    |             Sollicitatieformulier          |\n\
    ----------------------------------------------\n\
    |Er word een aantal relevante vragen gesteld |\n\
    |Liefst invullen met eer en geweten          |\n\
    |Als het blijkt dat u aan de citeria voldoet |\n\
    |dan komt in aanmerking voor de sollicitatie |\n\
    |Veel Succes!                                |\n\
    ----------------------------------------------")

def name():
    name = input("What is ur name?\n").lower()
    if name == 'peter':
        raise NameError('Peter is not welcome here!')
    else:
        name = True

def experience():
    try:
        personErvaring = int(input("How many years of practical experience do you have in animal dressage or juggling or acrobatics?\n"))
        if personErvaring >= 3:
            personErvaring = True
        elif personErvaring < 3:
            if personErvaring < 0:
                print('I dont understand negative numbers.')
                experience()
            else:
                personErvaring = False
        else:
            print("I didnt understand that.")
            experience()
    except:
        print('I didnt understand that.')
        experience()

def diploma():
    try:
        mboDiploma = int(input("How long have you had an MBO diploma in business?\n"))
        if mboDiploma >= 4:
            mboDiploma = True
        elif mboDiploma < 4:
            if mboDiploma < 0:
                print('I dont understand negative numbers.')
                diploma()
            else:
                mboDiploma = False
    except:
        print('I didnt understand that.')
        diploma()

def truckLicense():
    try:
        vrachtWagenRijbewijs = input("Do you have a truck license?(J/N)\n").lower()
        if vrachtWagenRijbewijs == "j":
            vrachtWagenRijbewijs = True
        elif vrachtWagenRijbewijs == "n":
            vrachtWagenRijbewijs = False
        elif vrachtWagenRijbewijs.isnumeric():
            print('I dont understand numbers.')
            truckLicense()
        else:
            print('Sorry i didnt quite get that.')
            truckLicense()
    except:
        print('I dont understand numbers.')
        truckLicense()

def hat():
    try:
        bezittingHoed = input("Do you have a big hat? (J/N)\n").lower()
        if bezittingHoed == "j":
            bezittingHoed = True
        elif bezittingHoed == "n":
            bezittingHoed = False
        elif bezittingHoed.isnumeric():
            print("I dont understand numbers.")
    except:
        print('I dont understand numbers.')

def gender():
    try:
        gender = input("Are you a male or a female?\n").lower
        if gender == "male":
            haar = input("How long is your moustache?\n") # Vraag voor een man
            haar = True
        elif gender == "female":
            haar = input("How long is your curly hair?\n") # Vraag voor een Vrouw
            haar = True
        elif gender.isnumeric():
            print('Sorry i dont understand numbers.')
    except:


def main():
    solicitatieFormulier()
    name() #asks for Name
    experience() #asks for Experience
    diploma() #asks for Diploma
    truckLicense() #asks for Truck License <
    hat() #asks for hat
    gender() #asks for gender (no sexisme)
main()