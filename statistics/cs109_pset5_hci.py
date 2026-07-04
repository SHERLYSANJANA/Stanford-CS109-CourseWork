# Do NOT add any other import statements.
# Don't remove this import statement.
import numpy as np
from cs109_pset5_util import get_filepath

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

def get_sample_mean(filepath):
    grades = np.loadtxt(filepath)

    return (np.mean(grades))
    
        

def get_mean_var(filepath, seed=109):
    """
    filepath is the path to a data file.
    You must use the filepath variable. Do NOT alter the 
    filepath variable, and do NOT hard-code a filepath; 
    if you do, you'll likely fail the autograder.
    Do not alter the seed variable either.

    You MUST use np.random.choice with replace=True
    to draw random samples. You may NOT use any other 
    function to draw random samples. See assignment 
    handout for details.

    Return the variance of the mean grade that the 
    control experiment described in the assignment 
    handout would have been given.
    """
    np.random.seed(seed)  # DO NOT ALTER OR DELETE THIS LINE

    ### BEGIN YOUR CODE FOR PART (B) ###
    mean_data=[]
    grades = np.loadtxt(filepath)
    for _ in range(10000):
        sample=np.random.choice(grades,size=5,replace=True)
        mean_data.append(np.mean(sample))
    
    return np.var(mean_data)
    

    ### END YOUR CODE FOR PART (B) ###


def get_median_var(filepath, seed=109):
    """
    filepath is the path to a data file.
    You must use the filepath variable. Do NOT alter the 
    filepath variable, and do NOT hard-code a filepath; 
    if you do, you'll likely fail the autograder.
    Do not alter the seed variable either.

    Just like above, you MUST use np.random.choice.

    Return the variance of the median grade that the 
    control experiment described in the assignment 
    handout would have been given.
    """
    np.random.seed(seed)  # DO NOT ALTER OR DELETE THIS LINE

    ### BEGIN YOUR CODE FOR PART (C) ###

    median_data=[]
    grades = np.loadtxt(filepath)
    for _ in range(10000):
        sample=np.random.choice(grades,size=5,replace=True)
        median_data.append(np.median(sample))
        
    return np.var(median_data)

    ### END YOUR CODE FOR PART (C) ###


def optional_function():
    """
    We won't autograde anything you write in this function.
    But we've included this function here for convenience. 
    It will get called by our provided main method. Feel free
    to do whatever you want here, including leaving this function 
    blank. We won't read or grade it.
    """
    pass


def main():
    """
    We've provided this for convenience, simply to call 
    the functions above. Feel free to modify this 
    function however you like. We won't grade anything in 
    this function.
    """
    filepath = get_filepath('peerGrades.csv')
    print(f"Calling get_sample_mean with {filepath}")
    print("\tReturn value was:", get_sample_mean(filepath))

    print(f"Calling get_mean_var with {filepath}")
    print("\tReturn value was:", get_mean_var(filepath))

    print(f"Calling get_median_var with {filepath}")
    print("\tReturn value was:", get_median_var(filepath))

    print("Calling optional_function:")
    print("\tReturn value was:", optional_function())

    print("Done!")


# This if-condition is True if this file was executed directly.
# It's False if this file was executed indirectly, e.g. as part
# of an import statement.
if __name__ == "__main__":
    main()
