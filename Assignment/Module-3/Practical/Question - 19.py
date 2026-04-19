#Write a Python program to show method overloading

class company:

    def empdata(self,id):
        print("ID:",id)
        
    def empdata(self,name):
        print("Name:",name)

cp=company()
cp.empdata(1)
cp.empdata("Rajkumar")
