# ::tesla_start::
# ::class_start::

class Example:

    def __init__(self):
        self.number = 0
        self.word = "A"

    # ::tesla_start::
    # ::case_start::
    # >> getNumber()
    # << self.number
    # ::case_end::
    # ::code_start::

    # Getter for number
    def getNumber(self):
        return self.number

    # ::code_end::
    # ::tesla_end::



    # ::tesla_start::
    # ::case_start::
    # >> getNumber()
    # << number
    # ::case_end::
    # ::code_start::

    # Setter for number
    def setNumber(self, num):
        self.number = num
    
    # ::code_end::
    # ::tesla_end::



    # ::tesla_start::
    # ::case_start::
    # >> getNumber()
    # << number
    # ::case_end::
    # ::code_start::

    # Getter for word
    def getWord(self):
        return self.word
    
    # ::code_end::
    # ::tesla_end::



    # ::tesla_start::
    # ::case_start::
    # >> getNumber()
    # << number
    # ::case_end::
    # ::code_start::

    # Setter for word
    def setWord(self, w):
        self.word = w
    
    # ::code_end::
    # ::tesla_end::




    # ::tesla_start::
    # ::case_start::
    # >> getNumber()
    # << number
    # ::case_end::
    # ::code_start::

    def returnWordAndNumber(self):
        return str(self.word)+str(self.number)
    
    # ::code_end::
    # ::tesla_end::

# ::class_start::
# ::tesla_end::