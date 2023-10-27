"""
Main module for the deltatextsplitter-class
"""

# Import Python base-functionality:

# Import functionality from pdftextsplitter
from pdftextsplitter import textsplitter

# Import all the memberfunctions of this class or other classes we need;
# always use relative imports as from this directory:
from .printclass import printclass_deltatextsplitter

# Main class definition:
class deltatextsplitter:
    """
    This class is the mother-class of the deltatextsplitter-package. It handles
    the comparison of outputs from the pdftextsplitter-package against references.
    These references must be user-provided. The idea is that the user selects a
    certain number of reference-PDF documents (a testset) and provides
    references for those documents; meaning that the user specifies which
    structure elements are supposed to be found.

    The deltatextsplitter then compares these references against the actual
    output of pdftextsplitter and generates a clear KPI of the overall
    performance of pdftextsplitter in text structure recognition.
    """
    
    # ------------------------------------------------------------------------------------
    
    # Definition of the default-constructor:
    def __init__(self):

        # Class members:
        self.label = "deltatextsplitter"
        self.splitter = textsplitter()
        
    # Definition of class member functions:
    printclass = printclass_deltatextsplitter
