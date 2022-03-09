#Mert Erciyas 99058235
# Solicitatie print

from unicodedata import numeric

personCompitence = ["0_personErvaring", "1_mboDiploma", "2_vrachtWagenRijbewijs", "3_bezittingHoed", "4_certificaat"]
personPhysical = ["0_name", "1_haar", "2_lengte", "3_gewicht"]
distraction = ["0_sokken", "1_artiest", "2_pepsi", "3_eten"]


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
    global personErvaring
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
    global mboDiploma
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
    global vrachtWagenRijbewijs
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
    global bezittingHoed
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
        hat()

def gender():
    global haar
    try:
        gender = input("Are you a male or a female?\n").lower()
        if gender == "male":
            haar = input("How long is your moustache?\n") # Vraag voor een man
            haar = True
        elif gender == "female":
            haar = input("How long is your curly hair?\n") # Vraag voor een Vrouw
            haar = True
    except:
        print("Sorry i didnt understand.")

def length():
    global lengte
    try:
        lengte = int(input("How tall are you?\n")) 
        if lengte >= 180:
            lengte = True
        elif lengte < 180:
            if lengte < 0:
                print('I dont understand negative numbers.')
                length()
            else:
                lengte = False
    except:
        print('Please input numbers')
        length()

def weight():
    global gewicht
    try:
        gewicht = int(input("How much do you weigh?\n"))
        if gewicht >= 90:
            gewicht = True
        elif gewicht < 90:
            if gewicht < 0:
                print('I dont understand negative numbers.')
                weight()
            else:
                gewicht = False
    except:
        print('Please input numbers.')
        weight()

def certificate():
    global certificaat
    try:
        certificaat = input("Do you have a certificate of Survival with dangerous personnel? (J/N)\n")
        if certificaat == "J":
            certificaat = True
        elif certificaat == "N":
            certificaat = False
    except:
        print('Please input words.')
        certificate()

def questionsThatDontMatter():
    try:
        sokken = input("What kinds of socks do you wear?\n")
        artiest = input("What is your favorite artist?\n")
        pepsi = input("Coca cola or Pepsi?\n")
        eten = input("What is your favorite food?\n")
    except:
        print('i dont understand numbers.')

def main():
    solicitatieFormulier()
    name() #asks for Name
    experience() #asks for Experience
    diploma() #asks for Diploma
    truckLicense() #asks for Truck License <
    hat() #asks for hat
    gender() #asks for gender (no sexisme)
    length() #asks for length
    weight() #asks for weight
    certificate() #asks for Certificate
    questionsThatDontMatter() #these dont matter
    if name == True and personErvaring == True and mboDiploma == True and vrachtWagenRijbewijs == True and bezittingHoed == True and haar == True and lengte == True and gewicht == True and certificaat == True:
        print("U bent aangenomen ", name, "!")
    else:
        print("U bent helaas niet angenomen ", name, "!")
main()