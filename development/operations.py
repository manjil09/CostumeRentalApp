import datetime,random
import return_operations

def costumes():
    """displays the details of the costumes"""
    print("---------------------------------------------------------------------------------------------------")
    print("ID      Costume Name            Company Name          Rent Price        Quantity")
    print("---------------------------------------------------------------------------------------------------")
    file = open("costume_details.txt","r")
    id = 1
    #reading from file and printing the costume details
    for line in file:        
        print(id,"\t"+line.replace(",","\t\t"))
        id += 1
    print("\n")
    file.close()

def dictionary_creation():
    """stores the costume details in a dictionary and returns it"""
    file = open("costume_details.txt","r")
    costume_dictionary = {}
    costume_id = 1
    #reading from the text file and storing the details in a dictionary
    for line in file:
        line = line.replace("\n","")
        costume_dictionary.update({costume_id:(line.split(","))})
        costume_id += 1
    file.close()
    return costume_dictionary

def text_update(costume_dictionary):
    """updates the text file"""
    file = open("costume_details.txt","w")
    #updating the text file after renting costumes
    for key,value in costume_dictionary.items():
        file.write(value[0] +","+ value[1] +","+ value[2] +","+ value[3])        
        file.write("\n")
    file.close()

def quantity_update(input_id,quantity):
    """updates ditcionary after renting"""
    costume_dictionary = dictionary_creation()
    available_quantity = int(costume_dictionary[input_id][3])
    while quantity<=0 or quantity>available_quantity: #to check the input quantity is available
        if quantity>available_quantity:
            print("Quantity provided is greater than what we have in stock.")
        else:
            print("Enter a valid quantity.")
        print("\n")
        success = False
        while success == False:
            try:
                quantity = int(input("Enter the quantity of costume: "))
                success = True
            except:
                #exception when invalid input is given as quantity
                print("\n")
                print("+++++++++++++++++++++++++++++++++++++++++++++")
                print("Invalid value for quantity! Please enter a number.")
                print("+++++++++++++++++++++++++++++++++++++++++++++")
                print("\n")
            
        print("\n")
    costume_dictionary[input_id][3] = str(available_quantity - quantity)#updating quantity in dictionary
    text_update(costume_dictionary)#calling function to update the text file
    return costume_dictionary,quantity

def generate_bill(name,total_price,item_list,bill_no):
    """creates the bill in text file"""
    SN = 0
    file = open("Rent_"+name.lower()+"_"+bill_no+".txt","w")
    file.write("Name of customer: "+name)
    file.write("\n")
    file.write("Date Time of borrow: "+str(datetime.datetime.now()))
    file.write("\n \n")
    file.write("SN \t\t Costume Name \t\t Brand \t\t Unit Price \tQuantity")
    file.write("\n")
    file.write("--------------------------------------------------------------------------------")
    file.write("\n")
    for each in item_list: #writing the list of costumes along with brand, price and quantity into txt file
        SN += 1
        file.write(str(SN)+"\t\t "+each[0]+"\t\t "+each[1]+"\t\t "+str(each[2])+"\t\t "+str(each[3]))
        file.write("\n")
    file.write("--------------------------------------------------------------------------------")
    file.write("\n \n")
    file.write("Total price is: "+str(total_price))
    file.write("\n")
    file.close()

def bill(name,total_price,item_list):
    """displays the bill"""
    SN = 0
    bill_no = str(random.randint(0,10000))# generates random number
    print("====================================================")
    print("                 Bill Details")
    print("====================================================")
    print("****************************************************")
    print("\n")
    print("Name of customer:",name)
    print("Date Time of rent:",datetime.datetime.now())
    print("\n")
    print("SN \t Costume Name \t\t Brand \t\t Unit Price \t Quantity")
    print("-------------------------------------------------------------------------")
    for each in item_list: #printing the list of costumes along with brand, price and quantity
        SN += 1
        print(str(SN)+"\t"+each[0]+"\t\t"+each[1]+"\t   "+str(each[2])+"\t\t "+str(each[3]))
        print("\n")
    print("-------------------------------------------------------------------------")
    print("\n")
    print("Total price:",total_price)
    print("\n")
    print("****************************************************")
    print("\n")
    generate_bill(name,total_price,item_list,bill_no)#calls the function to generate text bill
    print("-------------------------------------------------")
    print("|       Rent bill has been generated.           |")
    print("|       Your bill no is:",bill_no,"                  |")
    print("-------------------------------------------------")
    print("\n")
    print("**   Note: If the costumes are not returned within 5 days,   **")
    print("**         there will be additional fine of $7.5 per day     **")
    print("\n")

def valid_id():
    """to check if input id is valid and returns the valid id """
    costume_dictionary=dictionary_creation()
    success = False
    while success == False:
        try:
            input_id = int(input("Enter the ID of the costume: "))
            if int(costume_dictionary[input_id][3])==0:
                print("\n")
                print(" The costume is out of stock!!")
                print("\n")
            else:
                success = True
        except:
            #exception when the input id is invalid
            print("\n")
            print("+++++++++++++++++++++++++++++++++++++++++++++")
            print("The input Costume ID in invalid! Please enter a valid ID.")
            print("+++++++++++++++++++++++++++++++++++++++++++++")
            print("\n")             
    print("\n")
    print("++++++++++++++++++++++")
    print("Costume is available")
    print("++++++++++++++++++++++")
    print("\n")
    return input_id

def renting(name):
    """for renting costumes"""
    rent_more = True
    item_list = []
    SN = 0
    total_price = 0
    while rent_more:#loops as long as the user wants to rent more
        input_id = valid_id()#calls the function to check if input id is valid and stores the valid id
        success = False
        while success == False:
            try:
                quantity = int(input("Enter the quantity of costume: "))
                success = True
            except:
                #exception when the input quantity is invalid
                print("\n")
                print("+++++++++++++++++++++++++++++++++++++++++++++")
                print("Invalid value for quantity! Please enter a number.")
                print("+++++++++++++++++++++++++++++++++++++++++++++")
                print("\n")                
        print("\n")

        updating_dictionary = quantity_update(input_id,quantity)#calls the function to update quantity in dictionary
        costume_dictionary = updating_dictionary[0]
        quantity = updating_dictionary[1]
        price = float((costume_dictionary[input_id][2]).replace("$",""))
        total_price += price*quantity
        print("The price is:",price)
        print("\n")
        item_list.append([costume_dictionary[input_id][0],costume_dictionary[input_id][1],price,quantity])
        costumes()
        print("Rent another costume as well?")
        more = input("Please enter 'y' to rent more costume or any other key to stop.")
        print("\n")
        if more.lower() != "y":#asking user if they wand to rent more costumes
            rent_more = False
    bill(name,total_price,item_list)#calls the function to display the bill

def options():
    """displays the options to the user"""
    print("Please select an option:")
    print("(1) || Press 1 to rent costumes.")
    print("(2) || Press 2 to return costumes.")
    print("(3) || Press 3 to exit.")
    print("\n")

def option_1():
    """when renting costumes"""
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print(" Let's rent a costume. You can enter 'back' as name to go back.")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("\n")
    costumes()#to display the available costumes
    print("\n")
    name = input("Enter your name: ")
    print("\n")
    if name.lower() != "back":
        renting(name)

def option_2():
    """for returning costumes"""
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print(" Let's return a costume. You can enter 'back' as name to go back.")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("\n")
    costumes()#to display the available costumes
    return_operations.returning()#calls the function to return costumes
    
def option_3():
    """to exit the application"""
    print("          Thank you for using the application.")
    print("\n")

def invalid_option():
    """displays error when invalid option is input"""
    print("Invalid Option!!!!")
    print("Please select the value as per the given options.")
    print("\n")


