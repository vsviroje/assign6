class Demo:
    clsvariable=50;
    def __init__(self,n1,n2):
        self.no1=n1;
        self.no2=n2;
    def Fun(self):
        print("Instance variable- no1",self.no1,"no2",self.no2);
    def Gun(cls):
        print("class variable",cls.clsvariable)


def main():
    obj1=Demo(10,20)
    obj2 = Demo(30,40)
    obj1.Fun()
    obj1.Gun()
    obj2.Fun()
    obj2.Gun()


if __name__=='__main__':
    main()

