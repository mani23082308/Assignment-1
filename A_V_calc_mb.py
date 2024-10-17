'''
TPRG 2131 Fall 202* Assignment 1
Sept, 202*
Phil J <philip.jarvis@durhamcollege>

Use this template as the start

*********
A/V calculator

(Level 0)
Enter Q/q to quit – select either will gracefully close the application and cancel the calculated view option.
Enter V/v to change the calculated view or D/d for default view.

	(Level 1)
    1.	First Area/Volume* calulation
    2.	Second Area/Volume* calculation
    3.	Third Area/Volume* calculation
    4.	Fourth Area/Volume* calculation
    5.	Fifth Area/Volume* calculation

*********

The above menu style (inside the asterix's) is expected, only 2 key entries to use the calculator.

The menu Level 1 , options 1...5 should be modified from the above to reflect the
function you selected.

After selection at level 1, the calculator expects data to entered (use appropiate data types).

(The Level 0 & 1 labels are for indication purpose and are not
to be included)

'''
# Name: Manpreet Badgal
# Student ID: 100945948
import math

print("************A/V calculator menu************")

def get_positive_value(message):
    while True:
        try:
            value = float(input(message))
            if value > 0.0:
                return value
            else:
                print("The value must be greater than zero.")
        except ValueError:
            print("Invalid Input. Try Again.")     # This function always asks the user to enter positive value

def calculated_rectangle_area(l,b):      #Applying all the formulas for area/volume calculations
    area_of_rectangle1 = l*b
    area = round(area_of_rectangle1,1)
    return area

def calculated_circle_area(r):
    area_of_circle1 = math.pi*r**2
    area = round(area_of_circle1,1)
    return area

def calculated_triangle_area(b,h):
    area_of_triangle1 = b*h/2
    area = round(area_of_triangle1,1)
    return area

def calculated_cuboid_volume(l,b,h):
    volume_of_cuboid1 = l*b*h
    volume = round(volume_of_cuboid1,1)
    return volume

def calculated_cylinder_volume(r,h):
    volume_of_cylinder1 = (1/3)*math.pi*(r**2)*h
    volume = round(volume_of_cylinder1,1)
    return volume


def main():
    view_type = 'd'# Default view type
if __name__ == "__main__":

    while True:
        choice = input("Enter Q/q to quit, V/v to change view, or D/d for default view: ").strip().lower()

        if choice == "q":
            print("Have a nice day!")
            break

        if choice == "v":          # switching to view modes
            view_type = choice
            print("You have switched to calculated view.")
        elif choice == "d":
            view_type = choice
            print("You are now in default view.")
        else:
            print("Invalid choice. Please enter Q/q, V/v, or D/d.")

        # Level 1
        while True:
            print("\nEnter your choice (1-6):")
            print("1. First Area Calculation: Rectangle")
            print("2. Second Area Calculation: Circle")
            print("3. Third Area Calculation: Triangle")
            print("4. Fourth Volume Calculation: Cuboid")
            print("5. Fifth Volume Calculation: Cylinder")
            print("6. Return to Main Menu.")

            choice = input("Select the option to start the calculator: ").strip()

            if choice == '1':    # area of rectangle
                length = get_positive_value("Enter length of the rectangle: ")
                breadth = get_positive_value("Enter breadth of the rectangle: ")
                area = calculated_rectangle_area(length, breadth)
                print(f"{length} * {breadth} = {area} {'(length * breadth = area)' if view_type == 'v' else ''}")

            elif choice == '2':  # area of circle
                radius = get_positive_value("Enter radius of the circle: ")
                area = calculated_circle_area(radius)
                print(f"π * {radius}^2 = {area} {'(π * r^2 = area)' if view_type == 'v' else ''}")

            elif choice == '3':    # area of triangle
                base = get_positive_value("Enter base of the triangle: ")
                height = get_positive_value("Enter height of the triangle: ")
                area = calculated_triangle_area(base, height)
                print(f"{base} * {height} / 2 = {area} {'(base * height / 2 = area)' if view_type == 'v' else ''}")

            elif choice == '4':     # volume of cuboid
                length = get_positive_value("Enter length of the cuboid: ")
                breadth = get_positive_value("Enter breadth of the cuboid: ")
                height = get_positive_value("Enter height of the cuboid: ")
                volume = calculated_cuboid_volume(length, breadth, height)
                print(f"{length} * {breadth} * {height} = {volume} {'(length * breadth * height = volume)' if view_type == 'v' else ''}")

            elif choice == '5': # volume of cylinder
                radius = get_positive_value("Enter radius of the cylinder: ")
                height = get_positive_value("Enter height of the cylinder: ")
                volume = calculated_cylinder_volume(radius, height)
                print(f"π * {radius}^2 * {height} = {volume} {'(π * r^2 * height = volume)' if view_type == 'v' else ''}")

            elif choice == '6':
                break  # Return to the main menu

            else:
                print("Invalid option. Please try again.")
