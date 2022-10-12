#Name- Jaskaran Singh
#Instructor Name- Madiha Kazmi
#Date Created = 10 October 2022
#Last Modified= 11 October 2022


#This is the global variable for the loop
global i 
i=0

#This is the function for discount total function
def dis(total1):
    discount=total1*0.05
    return discount

#This function is for the 10% discount for student
def dis1(total1):
    discount4=total1*0.10
    return discount4

#This Function is for subtotal
def stdis(total1):
    discount2=(total1)*0.85
    return discount2

def stdis1(total1):
    discount3=total1*0.95
    return discount3

#This function is for tax
def tax(total1):
    taxx=total1*0.13
    return taxx

def st(total1):
    sub_total=total1*0.95
    return sub_total

#This function us for meal1+quantity
def mea1l(quantity):
    total1 = 10 * quantity
    return total1

#This function us for meal1+quantity
def mea12(quantity):
    total2 = 15 * quantity
    return total2

#This is the introduction of the restraunt 
print("Welcome!!!")
print("Arnold's Amazing Eats II")
print("")

print("Fill the personal information for store")
print("")

# Here are the all input command for entering the information of customer 
First_name=str(input("Enter your First Name\n"))
Last_name=str(input("Enter your Last Name\n"))
address=(input("Enter your full delivery address (street number, street name, unit)\n"))
city=str(input("Enter your City\n"))
province=str(input("Enter your Province\n"))
PostalCode=(input("Enter your Postal Code\n"))
Phonenumber=(input("Enter your Phone-Number\n"))

#These print command is for the printing the information of the customer
print("")
print("First Name==", First_name)
print("Last Name==", Last_name)
print("Address==", address)
print("City==", city)
print("Province==", province)
print("Phone-Number==", PostalCode)
print("")

#This is the starting of while loop if the customer not confirm he order to restart the menu
while i==0:
    print("     Menu    ")
    print("")
    print("1. Mexican Pizza     $15")
    print("2. Noodles           $10")
    number=str(input("Pick up the dinner items\n"))
        
    #here is the statement for choice if the customer select the option 1    
    if number=="1":
            print("How many of those meals are being ordered today")
            quantity=int(input("Quantity\n"))
            total1=int(quantity*15)

            #This command is for input of confirmation yes or no
            Confirmation=str(input("Confirm Your Order [Y] or [N]"))
            if Confirmation=='Y' or Confirmation=='y':
                print("Thanks For Confirming")

                #This command is for input of confirmation yes or no
                student=(input("Are you a student [Y] or [N]"))
            
                #if the total1 is greater than 100
                if total1<= 100:
                    discount=dis(total1)
                    print("")
                    print("Total $",total1)
                    print("Discount on order is 5% -",discount)
                    if student == 1:
                        print("Additional offer for a student of 10%","discount")
                        discount2=dis(total1)
                        print("")
                        print("Your final Price for Pizza is without 13% HST: ",discount2)
                    else:
                            discount3=dis(total1)
                            print("")
                            print("Your final Price for Pizza is without 13% HST: ",discount3)
                    
                    #These are the print commands for reciept
                    print()
                    print ("Reciept")
                    print("Order                Quantity       Price     Total")
                    print("-----                --------       -----     -----")
                    print("Mexican Pizza        ",quantity,"   $10     $",total1)

                    if student=='y' or student=='Y':
                        total1=mea1l(quantity)
                        print("")
                        discount4=dis1(total1)
                        print("")
                        print("10% Student Savings                      -$",discount4)
                        print("Discount of 5%                           -$",discount)
                        discount2=stdis(total1)
                        print("")
                        print("                           Sub Total      $",discount2)
                        taxx= tax(total1)
                        print("")

                        print("                           Tax (13%)         $",taxx)
                        print("--------------------------------------------------")
                        print("                           Grand Total    $",total1*0.98)
                    else:
                            print("Discount of 5%                           -$",total1*0.05)
                            sub_total=st(total1)
                            print("") 
                            print("                           Sub Total      $",total1*0.95)
                            print("                           Tax (13%)      $",total1*0.13)
                            print("--------------------------------------------------")
                            print("                           Grand Total    $",total1*1.08)
                    break 

    #here is the statement for choice if the customer select the option 1            
    elif number=="2":
            print("How many of those meals are being ordered today")
            quantity=int(input("Quantity\n"))
            total1=int(quantity*15)

            #This is the confirmation for the Second meal
            Confirmation=str(input("Confirm Your Order [Y] or [N]"))
            if Confirmation=='Y' or Confirmation=='y':
                print("Thanks For Confirming")
                student=(input("Are you a student [Y] or [N]"))

                #This is the if else for the diiscount            
                if total1<= 100:
                    discount=dis(total1)
                    print("")
                    print("Total $",total1)
                    print("Discount on order is 5% -",discount)
                    if student == 1:
                        print("Additional offer for a student of 10%","discount")
                        discount2=dis(total1)
                        print("")
                        print("Your final Price for Noodle is without 13% HST: ",discount2)
                    else:
                            discount3=dis(total1)
                            print("")
                            print("Your final Price for Noodle is without 13% HST: ",discount3)

                    print()
                    print ("Reciept")
                    print("Order                Quantity       Price     Total")
                    print("-----                --------       -----     -----")
                    print("Noodle        ",quantity,"   $10     $",total1)

                    if student=='y' or student=='Y':
                        total1=mea1l(quantity)
                        print("")
                        discount4=dis1(total1)
                        print("")
                        print("10% Student Savings                      -$",discount4)
                        print("Discount of 5%                           -$",discount)
                        discount2=stdis(total1)
                        print("")
                        print("                           Sub Total      $",discount2)
                        taxx= tax(total1)
                        print("")

                        print("                           Tax (13%)         $",taxx)
                        print("--------------------------------------------------")
                        print("                           Grand Total    $",total1*0.98)
                    else:
                            print("Discount of 5%                           -$",total1*0.05)
                            sub_total=st(total1)
                            print("") 
                            print("                           Sub Total      $",total1*0.95)
                            print("                           Tax (13%)      $",total1*0.13)
                            print("--------------------------------------------------")
                            print("                           Grand Total    $",total1*1.08)
                    break 
      
       #This is the command if the customer put wrong option
    else:
            print("Enter a valid option") 

        