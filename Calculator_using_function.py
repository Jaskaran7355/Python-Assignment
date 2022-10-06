#Define all the funtions of all areas used in the code(area of circle,rectangle,square)

def area_square(side):
    area_s = side * side
    return area_s

def area_rectangle(length, breadth):
   area_r = length * breadth
   return area_r

def area_circle(r):
   area_c = 3.14 * r * r 
   return area_c

#defining all the functios for all the perimeter used in code (perimeter of square, rectangle, circle)

def perimeter_square(side):
   perimeter_s= 4 * side
   return perimeter_s

def perimeter_rectangle(length, breadth):
   perimeter_r = 2 * length + breadth
   return perimeter_r

def perimeter_circle(r):
   perimeter_c = 2 * 3.14 * r
   return perimeter_c
   
#Header Statement of the Geometry Calculator
print("Geometry Calculator")

#Options for the Calculator
print("1.Calculate the Area of Square")
print("2.Calculate the Area of Rectangle")
print("3.Calculate the Area of Circle")
print("4.quit")

#This command is to enter the choice from the user
print("Enter Your Choice(1-4)")
number=int(input())

#conditions and calling all the functions which were metioned above

#calling the area function for square
if number==1:
   print("Enter the side of square to calculate the area of square")
   side=float(input())
   area_s = area_square(side)
   print("")
   print("The area of square is:", area_s, "square cm")

#calling the perimeter function for square
   perimeter_s = perimeter_square(side)
   print("")
   print("The perimeter of square is:", perimeter_s, "cm")

#calling the area function for rectangle
elif number==2:   
   print("Enter the length and breadth of rectangle to calculate the area of rectangle")
   length=int(input())
   breadth=int(input())
   area_r = area_rectangle(length, breadth)
   print("")
   print("The area of rectangle is:", area_r, "square cm")

#calling the perimeter function for rectangle
   perimeter_r = perimeter_rectangle(length,breadth)
   print("")
   print("The perimeter of rectangle is:", perimeter_r, "cm")

#calling the area function for circle
elif number==3:
   print("Enter the radius of circle to calculate the area of circle")
   r=int(input())
   area_c = area_circle(r)
   print("")
   print("The area of circle is:", area_c, "square cm")

#calling the perimeter function for square
   perimeter_c = perimeter_circle(r)
   print("")
   print("The perimeter of raduis is:", perimeter_c, "cm")

elif number==4:
   print("Thanks")

else:
   print("Enter a Valid number")