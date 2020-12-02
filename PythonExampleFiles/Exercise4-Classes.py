# Examples of working with classes

class myClass():
    def method1(self):
        print("myClass method1")
    
    def method2(self, someString):
        print("myClass method2: " + someString)

class anotherClass(myClass):
    def method2(self):
        print("anotherClass method2")
    
    def method1(self):
        myClass.method1(self);
        print("anotherClass method1")
    
def main():
    #exercise in the class methods
    c = myClass()
    c.method1()
    c.method2("This is my string")
    c2 = anotherClass()
    c2.method1()
    c2.method2()

if __name__ == "__main__":
    main()