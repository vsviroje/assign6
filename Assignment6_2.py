class Circle:
    PI=3.14;
    def __init__(self):
        self.radius=0.0;
        self.area=0.0;
        self.circum = 0.0;

    def Accept(self):
        self.radius=int(input("Enter Radius"));

    def cArea(self):
        if self.radius!=0.0:
            self.area=(self.radius*self.radius)*self.PI
        else:
            print("Radius is not given use Accept()")

    def cCircumference(self):
        if self.radius!=0.0:
            self.circum=self.radius*(self.PI*2)
        else:
            print("Radius is not given use Accept()")

    def Display(self):
        print("Radius-",self.radius," Area-",self.area," Circumference-",self.circum)


def main():
    obj1=Circle()
    obj2=Circle()

    obj1.Accept()
    obj1.cArea()
    obj1.cCircumference()
    obj1.Display()

    obj2.cArea()
    obj2.Display()


if __name__=='__main__':
    main()

