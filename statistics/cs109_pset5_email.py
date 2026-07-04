# Do NOT add any other import statements.
# Don't remove this import statement.
import numpy as np
from cs109_pset5_util import get_filepath
import os
import csv
import math

# Name:
# Stanford email:

"""
Assembled by Lisa Yan and CS109 TA Anand Shankar
*************************IMPORTANT*************************
For the functions we ask you to write, do NOT modify the name  
of the functions. Do not add or remove parameters to them
either. Moreover, make sure your return value is exactly as
described in the PDF handout and in the provided function 
comments. Remember that your code is being autograded. 
You are free to write helper functions if you so desire.
Do NOT rename this file.
*************************IMPORTANT*************************
"""

def get_filepath(filename):
    """
    filename is the name of a data file, e.g.,
    "learningOutcomes.csv". You can call this helper
    function in all parts of your code.

    Return a full path to the data file, located in the
    directory datasets, e.g., "datasets/learningOutcomes.csv"
    """
    return os.path.join("datasets", filename)

def get_expectation(filepath):
    """
    filepath is the path to a data file.
    You must use the filepath variable. Do NOT 
    alter the filepath variable, and do NOT 
    hard-code a filepath; if you do, you'll 
    likely fail the autograder.

    Let X be a random variable as defined in the 
    assignment handout. You should compute and
    return E[X] (which is of type float).
    """
    print(filepath)
    
    expectation=0
    timings=[]
    keys=[]
    
    with open(filepath) as file :
        data=csv.reader(file)

        for row in data :
            timings.append(float(row[0])) #timings in one list 
            keys.append(row[1])  #keys in one list
        
    n=len(keys)
    
    for i in range(n) :
        expectation+=timings[i]*(keys.count(keys[i]))/n
    return expectation
def get_squared_expectation(filepath):
    """
    filepath is the path to a data file.
    You must use the filepath variable. Do NOT 
    alter the filepath variable, and do NOT 
    hard-code a filepath; if you do, you'll 
    likely fail the autograder.

    Let X be a random variable as defined in the 
    assignment handout. You should compute and
    return E[X^2] (which is of type float).
    """
    squared_expectation=0
    timings=[]
    keys=[]
    
    with open(filepath) as file :
        data=csv.reader(file)
        for row in data :
            timings.append(float(row[0])) #timings in one list 
            keys.append(row[1])  #keys in one list

    n=len(keys)
    
    for i in range(n) :
        squared_expectation+=(timings[i]*timings[i]*(keys.count(keys[i])/n))
        
    return squared_expectation


def optional_function():
    """
    We won't grade anything you write in this function.
    But we've included this function here for convenience. 
    It will get called by our provided main method. Feel free
    to do whatever you want here, including leaving this function 
    blank. We won't read or grade it.
    """

    a_path = get_filepath('personKeyTimingA.txt')
    b_path = get_filepath('personKeyTimingB.txt')
    given_text=get_filepath('given_text.csv')
    
    expectation_A=get_expectation(a_path)
    expectation_B=get_expectation(b_path)
    squared_expectation_A=get_squared_expectation(a_path)
    squared_expectation_B=get_squared_expectation(b_path)

    variance_A=(expectation_A**2)-squared_expectation_A
    variance_B=(expectation_B**2)-squared_expectation_B

    standard_A=math.sqrt(variance_A)
    standard_B=math.sqrt(variance_B)

    
    expectation_giventext=get_expectation(given_text)
    z_A=(expectation_giventext-expectation_A)/standard_A
    z_B=(expectation_giventext-expectation_B)/standard_B

    if(z_A<z_B) :
        print("A wrote the piece of text")
    elif(z_B<z_A) :
        print("B wrote the piece of text")
    else :
        print("Sorry the text might have been written by both")
     
    return 0

def main():
    """
    We've provided this for convenience, simply to call 
    the functions above. Feel free to modify this 
    function however you like. We won't grade anything in 
    this function.
    """
    a_path = get_filepath('personKeyTimingA.txt')
    b_path = get_filepath('personKeyTimingB.txt')

    print(f"Calling get_expectation with {a_path}")
    print("\tReturn value was:", get_expectation(a_path))

    print(f"Calling get_expectation with {b_path}")
    print("\tReturn value was:", get_expectation(b_path))

    print(f"Calling get_squared_expectation with {a_path}")
    print("\tReturn value was:", get_squared_expectation(a_path))

    print(f"Calling get_squared_expectation with {b_path}")
    print("\tReturn value was:", get_squared_expectation(b_path))

    print("Calling optional_function")
    print("\tReturn value was:", optional_function())

    print("Done!")


# This if-condition is True if this file was executed directly.
# It's False if this file was executed indirectly, e.g. as part
# of an import statement.
if __name__ == "__main__":
    main()
