#Project by Qudratullah Rajavi
#Built an interactive command-line ordering system in Python focused on one core principle:
#never trust user input. Every input point is treated as a potential failure, validated before
#moving forward, and handled with a specific recovery path.

# My program allows user to order pizza, taco and sandwich from my store.

#custom exception: to use when the entered order is not in our menu
class InvalidFoodError(Exception):
    pass

#custom exception: to use when the entered number is 0 or negative
class InvalidNumberError(Exception):
    pass

#custom exception: to use when the input is not the word "done"
class InputNotDoneError(Exception):
    pass

#dictionary showing what's on menu and their prices
menu_and_price = {"taco": 2, "sandwich": 3, "pizza": 5}

# function to show welcome message
def welcome_statement_function():
    print("Welcome to my restaurant EasyPeasy. I sell some delicious food and here's the list:")
    for item, price in menu_and_price.items():
        print(f"{item}: {price} dollars")
    print()

welcome_statement_function()

#defining variables with their initial values
total_taco_price = 0
total_sandwich_price = 0
total_pizza_price = 0

taco_num = 0
sandwich_num = 0
pizza_num = 0

plural_letter = ""

#Writing a while loop to take order
while True:
    while True:
        try:
            order_question = input("\nDo you want to order something/order more?"
                           "(type yes/no and press enter) ").lower().strip()
            if order_question not in ["yes", "no", "y", "n"]:
                raise ValueError("\nInvalid response, type yes or no only\n")
            break
        except ValueError as e:
            print(e)
        except Exception as e:
            print(f"\nSomething unexpected happened: {e}. Try again!\n")
        
#if the user says no, the while loop will break
    if order_question in ["no", "n"]:
        break

#getting order type
    while True:
        try:
            order_type = input("\nWhat would you like? (select only one item: taco/sandwich/pizza). ").lower().strip()
            if order_type not in ["taco", "sandwich", "pizza"]:
                raise InvalidFoodError("\nInvalid. Only select one among taco/sandwich/pizza\n")
            break
        except InvalidFoodError as e:
            print(e)
        except Exception as e:
            print(f"\nSomething unexpected happened: {e}. Try again!\n")
        
        
#getting order quantity:       
    while True:
        try:
            if order_type == "sandwich":
                plural_letter = "es"
            else:
                plural_letter = "s"
            order_quantity = int(input(f"\nHow many {order_type}{plural_letter}? ").strip())
            if order_quantity <= 0:
                raise InvalidNumberError("\nOnly a positive integer number, please!\n")
            break
        except InvalidNumberError as e:
            print(e)
        except ValueError:
            print("\nInvalid entry. Only enter an integer number!\n")
        except Exception as e:
            print(f"\nSomething unexpected happened: {e}. Try again!\n")
    
#if ordered taco, calculating total taco price
    if order_type == "taco":
        total_taco_price = total_taco_price + (order_quantity * menu_and_price["taco"])
        taco_num = taco_num + order_quantity
        
#if ordered sandwich, calculating total sandwich price
    elif order_type == "sandwich":
        total_sandwich_price = total_sandwich_price + (order_quantity * menu_and_price["sandwich"])
        sandwich_num = sandwich_num + order_quantity
        
#if ordered pizza, calculating total pizza price
    elif order_type == "pizza":
        total_pizza_price = total_pizza_price + (order_quantity * menu_and_price["pizza"])
        pizza_num = pizza_num + order_quantity

#caluclating total net amount, sales tax and total after tax
total_net_amount = total_taco_price + total_sandwich_price + total_pizza_price
sales_tax =  (0.0625 * total_net_amount)
total_after_tax = total_net_amount + sales_tax



print()

#Showing what has been ordered  
def your_order():
    return f"You have ordered: \n{taco_num} taco(s),      individual price: ${menu_and_price['taco']},    extended price: ${total_taco_price} \n{sandwich_num} sandwich(es), individual price: ${menu_and_price['sandwich']},    extended price: ${total_sandwich_price} \n{pizza_num} pizza(s),     individual price: ${menu_and_price['pizza']},    extended price: ${total_pizza_price}\n"

print(your_order())
print()

#Asking one last time if the user wants to add something else to their order
while True:
    try:
        order_again = input("Do you want to add anything else one last time? yes/no ").lower().strip()
        if order_again not in ["yes", "no", "y", "n"]:
            raise ValueError("\nInvalid response. Only say yes or no!\n")
        break
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"\n Something unexpected happened: {e}. Try again! \n")



#if the answer is yes, asking what they want to add to their order
if order_again in ["yes", "y"]:
    while True:
        try:
            order_type = input("\nWhat would you like? (select only one item: taco/sandwich/pizza) ").lower().strip()
            if order_type not in ["taco", "sandwich", "pizza"]:
                raise InvalidFoodError("\nInvalid. Only select one among taco/sandwich/pizza\n")
            break
        except InvalidFoodError as e:
            print(e)
        except Exception as e:
            print(f"\nSomething unexpected happened: {e}. Try again!\n")
       
    while True:
        try:
            if order_type == "sandwich":
                plural_letter = "es"
            else:
                plural_letter = "s"
            order_quantity = int(input(f"\nHow many {order_type}{plural_letter}? ").strip())
            print()
            if order_quantity <= 0:
                raise InvalidNumberError("\nOnly a positive integer number, please!\n")
            break
        except InvalidNumberError as e:
            print(e)
        except ValueError:
            print("\nInvalid entry. Only enter an integer number!\n")
        except Exception as e:
            print(f"\nSomething unexpected happened: {e}. Try again!\n")
                
    if order_type == "taco":
        total_taco_price = total_taco_price + (order_quantity * menu_and_price["taco"])
        taco_num = taco_num + order_quantity
    elif order_type == "sandwich":
        total_sandwich_price = total_sandwich_price + (order_quantity * menu_and_price["sandwich"])
        sandwich_num = sandwich_num + order_quantity
    elif order_type == "pizza":
        total_pizza_price = total_pizza_price + (order_quantity * menu_and_price["pizza"])
        pizza_num = pizza_num + order_quantity
        
#showing what has been ordered after the new addition    
    print(your_order())
    print()
    
else:
    print()
    

#calculating the total net amount, sales tax and total after tax, after the new addition to the order
total_net_amount = total_taco_price + total_sandwich_price + total_pizza_price
sales_tax =  (0.0625 * total_net_amount)
total_after_tax = total_net_amount + sales_tax

#Defining the function to show the net price, tax and total price

 
def calculate_function():
    return f"\nTotal net amount: ${total_net_amount}\nSales Tax of 6.25%: ${sales_tax:.2f}\nTotal due with tax included: ${total_after_tax:.2f}\n"

print(calculate_function())

#Asking the user to accept the order
while True:
    try:
        finishing_order = input("\nType done and press enter to accept the order and finish the program: ").lower().strip()
        if finishing_order != "done":
            raise InputNotDoneError("\nI said type done, nothing else!\n")
        break
    except InputNotDoneError as e:
        print(e)
    except Exception as e:
        print(f"\n Something unexpected happened: {e}. Try again!\n")


#Displaying a thank you message for the user's order
print("\nThank you for your business!\n")
    
#Saving the results in a file in the user's computer
with open("Your_Order_Summary_EasyPeasy_Restaurant.txt", "w", encoding="utf-8") as f:
    f.write(your_order())
    f.write(calculate_function())
    f.write("\nThanks again!")
    
print("Your order summary has been saved into a txt file named\n'Your_Order_Summary_EasyPeasy_Restaurant.txt'\nin your python/thonny program location!")

