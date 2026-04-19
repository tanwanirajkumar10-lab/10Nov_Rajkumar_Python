#Write a Python program to show method overriding.

class company:

    def empdata(self,name):
        print("Name:",name)
    
class employee(company):
        
    def empdata(self,name):
        print("Name:",name)

emp = employee()
emp.empdata("Rajkumar")
cp = company()
cp.empdata("Ashish")