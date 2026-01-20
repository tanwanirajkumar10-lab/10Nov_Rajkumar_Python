#Write Python programs to demonstrate method overloading and method overriding.

#Method Overloading

class company:

    def empdata(self,id):
        print("ID:",id)
        
    def empdata(self,name):
        print("Name:",name)

cp=company()
cp.empdata(1)
cp.empdata("Rajkumar")


#Method Overriding

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