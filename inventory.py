from tabulate import tabulate

#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        '''
        In this function, you must initialise the following attributes:
            ● country,
            ● code,
            ● product,
            ● cost, and
            ● quantity.
        '''
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        pass
        '''
        Add the code to return the cost of the shoe in this method.
        '''
        return self.cost

    def get_quantity(self):
        pass
        '''
        Add the code to return the quantity of the shoes.
        '''
        return self.quantity

    def __str__(self):
        pass
        '''
        Add a code to returns a string representation of a class.
        '''
        return f"{self.country}, {self.code}, {self.product}, R{self.cost:.2f}, {self.quantity}"


#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []
#==========Functions outside the class==============
def read_shoes_data():
    pass
    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    '''
    #Using try/except for checking if the file exists
    try:
        with open("./inventory.txt", "r") as f:
            shoes = f.readlines()
    except FileNotFoundError as e:
        print("Loading Shoe Inventory Failed. File not found.")
        return
    
    #Popping away the first line to remove the file template
    shoes.pop(0)

    #Looping over the shoes to create an object with them
    for i in range(0, len(shoes)):
        #Print how far along the process is
        # if round((i / len(shoes)) * 100) == 25 or round((i / len(shoes)) * 100) == 50 or round((i / len(shoes)) * 100) == 75:
        print(f"{'=' * round((i / len(shoes)) * 10)}{'-' * (10 - round((i / len(shoes)) * 10))} {round((i / len(shoes))* 100)}% complete")
        
        #Splitting the line into its individual values
        country, code, product, cost, quantity = shoes[i].split(",")
        #Changing the values that need to be into int version
        cost, quantity = int(cost), int(quantity)

        shoe_list.append(Shoe(country,code,product,cost,quantity))
    print("Loading Complete. Creating Menu...")
        

def capture_shoes():
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''
    #Getting the data from the user
    country, code, product, cost, quantity = (input("Please input the data for the shoe in this order: country, code, product, cost, quantity\n")).split(", ")
    
    #Creating the shoe object and adding it to the shoe list
    shoe_list.append(Shoe(country, code, product, int(cost), int(quantity)))
    print(f"Successfully added the shoe with code '\033[1m{code}\033[0m to the inventory list")

def view_all():
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''
    #adding shoes data from the shoe objects in the shoe list to an empty list
    shoe_data = []
    for shoe in shoe_list:
        shoe_data.append((shoe.__str__()).split(", "))
    
    #Printing that string with all the shoes data
    print(tabulate(shoe_data, headers=["Country", "Code", "Product", "Cost (Rand)", "Quantity"]))

def re_stock():
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''
    #Open the txt file to grab the lines of shoes
    try:
        with open("./inventory.txt", "r") as f:
            shoes = f.readlines()
    except FileNotFoundError as e:
        print("Loading Shoe Inventory Failed. File not found.")
        return
    
    #Empty list to hold the quantity values
    quantities = []

    #Removing the first template line
    shoes.pop(0)

    #Loop over each line and split them into their data and add the 4th index to a list
    for shoe in shoes:
        quantities.append(int(shoe.split(",")[4]))

    #Now get the minimum value
    minimum_quantity = min(quantities)

    #And get the index of this value
    index = quantities.index(minimum_quantity)

    #Get the data on the shoe with lowest quantity
    shoe_data = shoes[index].split(",")

    #Prompt to ask how much stock to add
    restock_quantity = input(f"We have found the shoe '\033[1m{shoe_data[2]}\033[0m' with a quantity of '\033[1m{shoe_data[4]}\033[0m'.\nHow much stock would you like to add?\n")

    #Check the input value is a number
    if not restock_quantity.isdigit():
        while not restock_quantity.isdigit():
            restock_quantity = input(f"Incorrect input. Please use digits.\nWe have found the shoe '\033[1m{shoe_data[2]}\033[0m' with a quantity of '\033[1m{shoe_data[4]}\033[0m'.\nHow much stock would you like to add?\n")
    
    #Change the shoes lines to match the now updated stock
    shoe_data[4] = str(int(shoe_data[4]) + int(restock_quantity))
    shoe_data_string = ",".join(shoe_data)
    shoes[index] = shoe_data_string + "\n"

    #Now write the updated list into the file
    with open("./inventory.txt","w") as f:
        for shoe in shoes:
            f.write(shoe)

    #Notification that the code worked
    print(f"Succesfully added {restock_quantity} stock to {shoe_data[2]}")

def search_shoe():
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''
    #Get shoes code from user
    search_shoe_code = input("Please enter the code for the shoe: ")

    #Create an empty variable for the shoe object to be placed in
    found_shoe_object = None

    #Loop over every shoe in the object list and see if the code matches and keep the shoe that matches
    for shoe in shoe_list:
        if shoe.code == search_shoe_code:
            found_shoe_object = shoe
            break
    
    return found_shoe_object

def value_per_item():
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''

    #Have an empty list for the code and total cost combo
    total_value_list = []

    #Loop over each shoe object and create a list of its code combined with its total value
    for shoe in shoe_list:
        total_value_list.append([shoe.code, f"R{(shoe.get_cost() * shoe.get_quantity()):.2f}"])
    
    #Now print the details in table form
    print(tabulate(total_value_list, headers=['Shoe Code', 'Total Stock Value']))

def highest_qty():
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''
    #Keep an empty list to store the quantities of shoes later
    quantities = []

    #Loop over the shoes in the shoe_list of objects and store the quantity
    for shoe in shoe_list:
        shoe_data = shoe.__str__().split(", ")
        quantities.append(int(shoe_data[4]))
    
    #Get max of the quantity from the list
    max_quantity = max(quantities)

    #Get object index with max value
    index = quantities.index(max_quantity)

    #Get object data with the index
    max_quantity_shoe_data = shoe_list[index].__str__().split(", ")

    #Display the shoe with the highest quantity for sale
    print(f"The shoe with a high quantity ({max_quantity_shoe_data[4]}) for sale is {max_quantity_shoe_data[2]} ({max_quantity_shoe_data[1]}) from {max_quantity_shoe_data[0]} for {max_quantity_shoe_data[3]}")
        

#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''
#Setting up the shoe objects
print("Loading Current Shoe Inventory...")
read_shoes_data()

#Creating the menu and looping
while 1:
    print("\n--------------------=================================================--------------------\n"\
      "Welcome to the \033[1m\033[4mNike Inventory Manager\033[0m\033[0m. Please make a selection with the \033[4mappropriate number\033[0m below:")
    choice = input("1. Reload shoes inventory\t\t\t\t2. Add a shoe to the invetory\n3. View all shoes in the inventory\t\t\t4. Restock a shoe\n5. Search for a shoe\t\t\t\t\t6. Total stock value for all shoes\n7. Show the shoe with the highest amount of stock\t8. Quit\n--------------------=================================================--------------------\nChoice: ")

    #Checking if the choice is a number only
    if not choice.isdigit():
        while not choice.isdigit():
            print("Incorrect choice made. Please try again")
            continue

    #Now that choice is confirmed number only, convert it to int
    choice = int(choice)
    
    #Checking what choice has been made and redirecting there
    match int(choice):
        case 1: 
            user_is_sure = input("This will remove any shoes capture by you previously. Are you sure you want to do this? Y/N\n")
            if user_is_sure.upper() in ["Y","YES"]:
                read_shoes_data()
            else:
                print("Aborting...")
        case 2: capture_shoes()
        case 3: view_all()
        case 4: re_stock()
        case 5: 
            found_shoe = search_shoe()
            if found_shoe:
                shoe_data = [(found_shoe.__str__()).split(", ")]
                print(f"Found a shoe with the following details\n{tabulate(shoe_data, headers=['Country', 'Code', 'Product', 'Cost (Rand)', 'Quantity'])}")
            else:
                print("No shoe found matching that code. Please try again.")
        case 6: value_per_item()
        case 7: highest_qty()
        case 8: 
            print("Thank you for using the \033[1m\033[4mNike Inventory Manager\033[0m\033[0m. Goodbye!")
            break
        case _:
            print("Unknown choice. Please try again")