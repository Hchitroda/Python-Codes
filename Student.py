class Student: #defining what a student is, what the student data type is
    
    def __init__(self, name, major, gpa, is_on_probation): #self is the object
        self.name = name #name of the student object will be equal to the name that we passed in)
        self.major = major 
        self.gpa = gpa 
        self.is_on_probation = is_on_probation