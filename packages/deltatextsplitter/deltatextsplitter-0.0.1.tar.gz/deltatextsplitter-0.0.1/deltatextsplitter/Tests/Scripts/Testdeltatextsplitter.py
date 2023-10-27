import sys
# caution: path[0] is reserved for script path (or '' in REPL)

# Imports from Source code:
sys.path.insert(1, '../../')
from Source.deltatextsplitter import deltatextsplitter

# Definition of unit tests:
def deltatextsplitter_printtest() -> bool:
    """
    # Unit test for the printclass-functionality of the deltatextsplitter-class:
    # Parameters: none; # Returns (bool): succes of the text.
    """
    
    # Generate the class:
    mydelta = deltatextsplitter()

    # Print the output:
    mydelta.printclass()
        
    # Define the answer:
    Answer = True

    # Return the answer:
    return Answer
    
# Definition of collection:    
def deltatextsplitter_tests() -> bool:
    """
    # Collection-function of unit-tests.
    # Parameters: none; # Returns (bool): succes of the text.
    """
    
    # Define answer:
    Answer = True
    
    # Call the tests:
    if (deltatextsplitter_printtest()==False):
        Answer=False
        print('\n==> deltatextsplitter_printtest() failed!\n')
    
    # Return answer:
    return Answer

if __name__ == '__main__':
    if deltatextsplitter_tests():
        print("Test Succeeded!")
    else:
        print("\n==> Test FAILED!!!\n")
