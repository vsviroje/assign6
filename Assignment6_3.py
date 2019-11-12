class Arithmetics:
    def __init__(self):
        self.val1=0.0;
        self.val2=0.0;

    def Accept(self):
        self.val1=int(input("Enter 1st number"));
        self.val2 = int(input("Enter 2nd number"));

    def Add(self):
        isOk = self.datacheck()
        if isOk:
            print("Addition-",self.val1+self.val2)

    def Sub(self):
        isOk = self.datacheck()
        if isOk:
            print("Subtraction-", self.val1 - self.val2)


    def Mult(self):
        isOk = self.datacheck()
        if isOk:
            print("Multiplication-", self.val1 * self.val2)

    def div(self):
        isOk=self.datacheck()
        if isOk:
            print("Division is-", self.val1 / self.val2)

    def datacheck(self):
        if self.val1 != 0.0 and self.val2 != 0.0:
            return True
        else:
            print("Val1 and Val2 is not given use Accept()")
            return False


def main():
    obj1=Arithmetics()
    obj2=Arithmetics()

    obj1.Accept()
    obj1.Add()
    obj1.Mult()
    obj1.div()
    obj1.Sub()

    obj2.Sub()

if __name__=='__main__':
    main()

