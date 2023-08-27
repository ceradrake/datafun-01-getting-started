"""

Purpose: Calculate the expenses of your wedding flowers.

Author: Cera Drake


"""
# ----------------- INSTRUCTOR GENERATED CODE -----------------

# Use this handy logger to document your work automatically

# import setup_logger function from instructor-generated module
from util_logger import setup_logger

# setup the logger using the current file name (a built-in variable)
logger, logname = setup_logger(__file__)

# ----------------- END INSTRUCTOR GENERATED CODE -----------------

# Import from Python Standard Library

import math

# Use the math module's constant for pi
pi = math.pi

# get the radius from the user - input result is always a string
# Use \n to add a blank new line to the terminal before we ask for input
string1 = input("\nEnter the price of your centerpiece: ")
string2 = input("\nEnter the price of your bridal bouquet: ")
string3 = input("\nEnter the price of your corsage: ")

# convert the radius_string to a number
int1 = int(string1)
int2 = int(string2)
int3 = int(string3)
my_costs = {int1, int2, int3}



# 
min = min(my_costs)
max = max(my_costs)
sum = sum(my_costs)
count = len(my_costs)
average = sum / count
product = int1 * int2 * int3




# log the results
logger.info(f"The minimum expense is {min}")
logger.info(f"The maximum expense is {max}")
logger.info(f"The sum of my expenses is {sum}")
logger.info(f"The average cost of each piece is {average}")
logger.info(f"The product of my costs is {product}")








