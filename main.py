MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
from art import logo
is_enter=True
print(logo)

while is_enter:

    user=input("What would you like? (espresso/latte/cappuccino):")
    if user=="q" or user=="Quit":
        print("Bye have a nice day")
        is_enter=False

    elif user=="report":
            print(f"water:{resources['water']}ml")
            print(f"milk:{resources['milk']}ml")
            print(f"coffee:{resources['coffee']}g")


    else:  
        print("please insert coins:")
        quarters=float(input("How many quarters? :" ))
        dimes=float(input("How many dimes? :" ))
        nickles=float(input("How many nickles? :" ))
        pennies=float(input("How many pennies? :" ))


        if resources['water']<MENU['latte']['ingredients']['water'] or resources['milk']<MENU['latte']['ingredients']['milk'] or resources['coffee']<MENU['latte']['ingredients']['coffee']:
            print("Sorry we dont have enough resources and returning your money")
        elif resources['water']>MENU['latte']['ingredients']['water'] and resources['milk']>MENU['latte']['ingredients']['milk'] and resources['coffee']>MENU['latte']['ingredients']['coffee']:
            if user=="latte":
                change=(quarters*0.25+dimes*0.1+nickles*0.05+pennies*0.01)-2.5
            if change<0:
                print("Sorry please provide some coins")
            else:   
                print(f"Here is ${change} in change")
                print(f"Here is your {user} Enjoy!")
                resources['water']=resources['water']-MENU['latte']['ingredients']['water']
                resources['milk']=resources['milk']-MENU['latte']['ingredients']['milk']
                resources['coffee']=resources['coffee']-MENU['latte']['ingredients']['coffee']
                

        
        
        elif resources['water']<MENU['espresso']['ingredients']['water'] or resources['milk']<MENU['espresso']['ingredients']['milk'] or resources['coffee']<MENU['espresso']['ingredients']['coffee'] :
            print("Sorry we dont have enough resources and returning your money")   
        elif resources['water']>MENU['espresso']['ingredients']['water'] and resources['milk']>MENU['espresso']['ingredients']['milk'] and resources['coffee']>MENU['espresso']['ingredients']['coffee'] :     
            if user=="espresso":
                change=(quarters*0.25+dimes*0.1+nickles*0.05+pennies*0.01)-1.5
            if change<0:
                print("Sorry please provide some coins")
            else:   
                print(f"Here is ${change} in change")
                print(f"Here is your {user} Enjoy!")
                resources['water']=resources['water']-MENU['espresso']['ingredients']['water']
                resources['milk']=resources['milk']-MENU['espresso']['ingredients']['milk']
                resources['coffee']=resources['coffee']-MENU['espresso']['ingredients']['coffee']

        

        elif resources['water']<MENU['espresso']['ingredients']['water'] or resources['milk']<MENU['espresso']['ingredients']['milk'] or resources['coffee']<MENU['espresso']['ingredients']['coffee'] :
            print("Soory we dont have enough resources and returning your money")  
        elif resources['water']>MENU['espresso']['ingredients']['water'] and resources['milk']>MENU['espresso']['ingredients']['milk'] and resources['coffee']>MENU['espresso']['ingredients']['coffee'] :    
            if user=="cappuccino":
                change=(quarters*0.25+dimes*0.1+nickles*0.05+pennies*0.01)-3.0
            if change<0:
                print("Sorry please provide some coins")
            else:   
                print(f"Here is ${change} in change")
                print(f"Here is your {user} Enjoy!")   
                resources['water']=resources['water']-MENU['cappuccino']['ingredients']['water']
                resources['milk']=resources['milk']-MENU['cappuccino']['ingredients']['milk']
                resources['coffee']=resources['coffee']-MENU['cappuccino']['ingredients']['coffee']     
        
        