'''
Jacob Haslam
IS 303 - A01

Paint Estimator
This program calculates the number of gallons of paint needed to cover
the walls of a specific room based on height and total width.

Inputs: 
- Room name (string)
- Wall height (float)
- Wall width (float)

Processes: 
- Convert height and width to float
- Calculate total area = (height * width)
- Calculate gallons needed: (total area / 350)

Outputs:
- Formatted message showing the room name and how many gallons of paint 
  are needed to cover the walls of the room.
'''

# 1.) Inputs
room_name = input("Which room are you painting? ")
wall_height = float(input("What is the height of the walls in feet? "))
wall_width = float(input("What is the total width of the walls in feet? "))

# 2.) Processes 
# Note: 1 gallon of paint covers approximately 350 square feet
total_area = wall_height * wall_width
gallons_needed = total_area / 350

# 3.) Outputs
print(f"For the {room_name}, you will need {gallons_needed:.2f} gallons of paint.")