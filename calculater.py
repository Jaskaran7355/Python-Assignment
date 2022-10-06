#This is the header statement fot the Calculator
print("Geometry Calculator")

#Options for the Calculator
print("1.Calculate the Area of Circle")
print("2.Calculate the Area of Rectangle")
print("3.Calculate the Area of Triangle")
print("4.quit")

#This command is to enter the choice from the user
number=int(input())
print("Enter Your Choice(1-4)")

#This is the different is and else statement for calcultion of areas after selecting the option from the user

#This is the first if statement for area of Circle
if number==1:
    print("Enter The radius of circle to find the area and perimeter of circle=")
    radius=int(input())
    print("The area of circle is:", 3.14*radius*radius)
    print("The perimeter of circle is:", 2 * 3.14 * radius)

#This is the second elif statement for area of Rectangle
elif number==2:
    print("Enter The Length and Breadth to find the area of Rectangle=")
    print("Enter The Length")
    Length=int(input())
    print("Enter The Breadth")
    Breadth=int(input())
    print("The area of Rectangle is:", Length*Breadth)
    print("The perimeter of rectangle is:", 2 * Length * Breadth)

#This is the third elif statement for area of Triangle
elif number==3:
    print("Enter The Base and Height to find the area of Triangle=")
    Base=int(input())
    Height=int(input())
    print("The area of Triangle is:", 0.5*Base*Height)
    print("The perimeter of triangle is:", 2 * 3.14 * radius)

#This is the fourth elif statement for quit and after quitting send a message to user
elif number==4:
    print("Thanks For Using the Calculator")


#This is the optional statement if user enters the wrong statement
else:
    print("Enter a valid option")