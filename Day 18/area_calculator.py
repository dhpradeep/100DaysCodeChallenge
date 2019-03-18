# Area calculation program
print("Area Calculation Program")
print("1. Triangle")
print("2. Circle")
print("3. Rectangle")
print("4. Quit")
print
# Get the user’s choice:
shape = 1
# Calculate the area:
while shape != 4:
        shape = int(input("Please select a number 1-4: "))
        if shape == 1:
                height = int(input("Please enter the height: "))
                width = int(input("Please enter the width of the base: "))
                area = 0.5*(height*width)
                print("The area is: " + str(area))
        if shape == 2:
                radius = int(input("Please enter the radius: "))
                area = 3.14159*(radius**2)
                print("The are is: " + str(area))
        if shape == 3:
                height = int(input("Please enter the height: "))
                width = int(input("Please enter the width: "))
                area = height*width
                print("The area is: " + str(area))