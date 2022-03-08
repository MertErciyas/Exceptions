# Mert Erciyas Pizza calculator 
import time,os

def clearScreen(sleepTime):
    time.sleep(sleepTime)
    os.system("cls")

def order():
    orderAgain = input("Would you like to order again? (yes/no)\n").lower()
    if orderAgain == "yes":
        clearScreen(1)
        askPizza()
    elif orderAgain == 'no':
        print("Have a nice day")
    else:
        print("Im sorry i didnt understand that.")
        clearScreen(3)
        order()

def askPizza():
    smallPizzaPrice = 7.50 # hier zie je de prijs van de small pizza
    mediumPizzaPrice = 9.50 # hier zie je de prijs van de medium pizza
    largePizzaPrice = 11.50 # hier zie je de prijs van de large pizza  

    try:
        smallPizza = int(input("How many little pizza's would you like?\n")) # hierbij kan je invoeren hoeveel small pizzas je wilt
        if smallPizza < 0:
            print("I dont understand negative numbers\n")
            askPizza()
        else:
            mediumPizza = int(input("How many medium pizza's would you like?\n")) # hierbij kan je invoeren hoeveel medium pizzas je wilt
            if mediumPizza < 0:
                print("i dont understand negative numbers, try again")
                askPizza()
            else:
                largePizza = int(input("How many large pizza's would you like?\n")) # hierbij kan je invoeren hoeveel large pizzas je wilt
                if largePizza < 0:
                    print("i dont understand negative numbers, try again")   
                    askPizza()
                else:
                    print("Your order has been recieved")

        smallPizzaKosten = (smallPizza * smallPizzaPrice)
        mediumPizzaKosten = (mediumPizza * mediumPizzaPrice)
        largePizzaKosten = (largePizza * largePizzaPrice)

        print("So you have:" , smallPizza , "small pizzas" , mediumPizza , "medium pizzas" , largePizza , "large pizzas\nthat will be" , smallPizzaKosten , "euro and for the small pizza's" , mediumPizzaKosten , "euro for the medium pizza's" , largePizzaKosten , "euro for the large pizza's\nthat will be:" )
        kosten = (float((smallPizza * smallPizzaPrice) + (mediumPizza * mediumPizzaPrice) + (largePizza * largePizzaPrice))) # hier berekend hij de kosten van alle pizzas
        print(kosten , "euro") # hier laat hij zien hoeveel de pizzas in totaal kosten
    except:
        print("Please type in a number (int)")
        clearScreen(3)
        askPizza()
    finally:
        order()

askPizza()