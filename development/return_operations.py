import datetime
import operations

def ask_rent_days():
    """asks the no of renting days to the user"""
    days_success = False
    while days_success == False:#to check if the input days is valid or not
        try:
            positive = False
            while positive == False:#to check if the input days is positive or not
                rent_days = int(input("Enter the no of renting days: "))
                if rent_days > 0:
                    positive = True
                else:
                    print("\n")
                    print("Invalid value for no of renting days! Please enter a positive number.")
                    print("\n")
            
            days_success = True
        except:#exception when invalid input is given
            print("\n")
            print("Invalid value for no of renting days! Please enter a number.")
            print("\n")
    return rent_days

def return_bill_text(name,bill_no,record,total_price,rent_days,fine):
    """creates the bill of returning in text file"""
    file = open("Return_"+name.lower()+"_"+bill_no+".txt","w")
    file.write("Name of customer: "+name)
    file.write("\n")
    file.write("Date Time of return: "+str(datetime.datetime.now()))
    file.write("\n")
    file.write("No of renting days: "+str(rent_days))
    file.write("\n \n")
    file.write("SN \t\t Costume Name \t\t Brand \t\t Unit Price \tQuantity")
    file.write("\n")
    file.write("--------------------------------------------------------------------------------")
    file.write("\n")
    for each in record.values(): #writing the list of costumes along with brand, price and quantity into txt file
        file.write(str(each[0])+"\t\t "+each[1]+"\t\t "+each[2]+"\t\t "+str(each[3])+"\t\t "+str(each[4]))
        file.write("\n")
    file.write("--------------------------------------------------------------------------------")
    file.write("\n \n")
    file.write("Total price is: "+str(total_price))
    file.write("\n")
    if fine !=0: #writing the fine into txt file if returned late
        file.write("\n")
        file.write("** Since the costumes were returned "+str(rent_days-5)+" days late;")
        file.write("\n")
        file.write("Fine: "+str(fine))
        file.write("\n")
        file.write("Total price with fine: "+str(fine+total_price))
        file.write("\n")
    file.close()

def return_bill(name,bill_no,record,total_price,rent_days):
    """displays the bill of returning"""
    fine = 0
    print("====================================================")
    print("                 Bill Details")
    print("====================================================")
    print("****************************************************")
    print("\n")
    print("Name of customer:",name)
    print("Date Time of return:",datetime.datetime.now())
    print("No of renting days:",rent_days)
    print("\n")
    print("SN \t Costume Name \t\t Brand \t\t Unit Price \t Quantity")
    print("-------------------------------------------------------------------------")
    for each in record.values(): #printing the list of costumes along with brand, price and quantity
        print(str(each[0])+"\t"+each[1]+"\t\t"+each[2]+"\t   "+str(each[3])+"\t\t ",str(each[4]))
        print("\n")
    print("-------------------------------------------------------------------------")
    print("\n")
    print("Total price:",total_price)
    if rent_days > 5:#to check if the costumes are returned within the timelimit
        fine = 7.5 * (rent_days - 5)
        print("\n")
        print("** Since the costumes were returned",rent_days-5,"days late;")
        print("Fine:",fine)
        print("Total price with fine:",total_price + fine)
    print("\n")
    print("****************************************************")
    print("\n")
    return_bill_text(name,bill_no,record,total_price,rent_days,fine)#calls the function to generate text bill
    print("-------------------------------------------------")
    print("|       Return bill has been generated.         |")
    print("-------------------------------------------------")
    print("\n")
    
def return_update(record):
    """updates the costume dictionary when costume is returned"""
    costume_dictionary = operations.dictionary_creation()#calls the function to create dictionary from text file of costume details
    for value in costume_dictionary.values():
        for records in record.values():
            if value[0] == records[1]:
                value[3] = str(int(value[3])+int(records[4]))
    operations.text_update(costume_dictionary)# call the function to update the text file

def details_from_bill(name,bill_no):
    file = open("Rent_"+name.lower()+"_"+bill_no+".txt","r")
    iteration = 0
    lines = list(file)
    record = {}
    rID = 0
    total_price = 0
    for line in lines:#extracting the records from the rent bill and storing in a dictionary
        iteration += 1
        if iteration>5 and iteration<(len(lines)-2):
            rID += 1
            line = line.replace("\n","")
            record.update({rID:line.split("\t\t ")})
        if iteration == len(lines):
            total_price = float(line.replace("Total price is: ",""))
    file.close()
    return record,total_price

def returning():
    """for returning costumes"""
    success = False
    while success == False:
        name = input("Enter your name: ")
        if name.lower() == "back":
            break
        bill_no = input("Enter your bill no: ")
        print("\n")
        try:
            file = open("Rent_"+name.lower()+"_"+bill_no+".txt","r")
            file.close()
            success = True
        except:#exception when the bill of input name or bill no does not exist
            print("The input customer name or bill no is incorrect! Please enter the correct value.")
            print("\n")
    if name.lower() != "back":   
        bill_details = details_from_bill(name,bill_no)
        record = bill_details[0]
        total_price = bill_details[1]
        
        rent_days = ask_rent_days()#calls function to ask no of days
        return_update(record)#calling the function to update dictionary after renturning
        return_bill(name,bill_no,record,total_price,rent_days)# calls function to generate bill after returning
        

