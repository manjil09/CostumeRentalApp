from operations import options,option_1,option_2,option_3,invalid_option

print("---------------------------------------------------------------------------------------------------")
print("                        Welcome to Costume Rental Application")
print("---------------------------------------------------------------------------------------------------")
print("\n")

run = True
while run:
    options()
    user_input = input("Enter your option: ")
    print("\n")
    
    if user_input == "1":
        option_1()#calls the function for renting costumes           
    elif user_input == "2":
        option_2()#calls the function for renting costumes
    elif user_input == "3":
        option_3()#for exiting the program
        run = False
    else:
        invalid_option()#displays invalid message when wrong input is entered
