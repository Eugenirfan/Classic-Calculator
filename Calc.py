class Arithmetic:
    print("hello")

    a=0
    b=0
    
        
    def __init__(self):
        print("Welcome to your calculator: ")
        print("1.Addition, 2.Subtraction, 3.Multiplication, 4.Division".replace(",", "\n"))

        x= int(input("choose the function you would like to perform: "))

        if x==1:
            self.varname()
            print(self.addition())

        if x==2:
            self.varname()
            print(self.subtraction())

        if x==3:
            self.varname()
            print(self.multiplication())

        if x==4:
            self.varname()
            print(self.division())
            
    def varname(self):
        global a
        global b
    
    
        a=int(input("enter the number: "))
        b=int(input("enter the number: "))
    
        

    def addition(self):
        print("your answer is:",a+b)

    def subtraction(self):
        print("Your answer is:",a-b)

    
    def multiplication(self):
        print("Your answer is :",a*b)

    
    def division(self):
        print("Your answer is:",a/b)

        
  

ob= Arithmetic()


        
        
    








        




        
        
        
