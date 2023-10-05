class rbi:
    def __init__(self):
        self.Total_funds1=100000
        self.Total_accounts1=10000
        


class sbi(rbi):
    def __init__(self):
        self.Total_funds2=50000
        self.Total_accounts2=5000
        
        super().__init__()

class Tamilnadu_bank(sbi):
    def __init__(self):
        self.Total_funds3=25000
        self.Total_accounts3=2500
        
        super().__init__()

class cub(Tamilnadu_bank):
    def __init__(self):
        self.Total_funds4=12000
        self.Total_accounts4=1000
        super().__init__()
        

    def deposit(self):
        self.dep = int(input("Enter amount to be deposited: "))
        
        self.Total_funds4 = (self.Total_funds4 + self.dep)
        print("Amount Deposited:",self.dep)
        print("Your City Union Bank Account Balance is: ",self.Total_funds4)
        self.Total_funds3 = (self.Total_funds3 + self.dep)
        print("TamilNadu Bank Account Balance is: ",self.Total_funds3)
        self.Total_funds2 = (self.Total_funds2 + self.dep)
        print("State Bank Account Balance is: ",self.Total_funds2)
        self.Total_funds1 = (self.Total_funds1 + self.dep)
        print("Reserve Bank Account Balance is: ",self.Total_funds1)

        
        

        self.withdraw()

    def withdraw(self):
        self.wd = int(input("\nEnter your withdrawn amount: "))
        if self.Total_funds4 >= self.wd:
            self.Total_funds4 = (self.Total_funds4 - self.wd)
            print("your amount is withdrawn: ", self.wd)
            print("Your City Union Bank Account Balance is: ",self.Total_funds4)

            self.Total_funds3 = (self.Total_funds3 - self.wd)
            print("Tamilnadu Bank Account Balance is: ",self.Total_funds3)

            self.Total_funds2 = (self.Total_funds2 - self.wd)
            print("State Bank Account Balance is: ",self.Total_funds2)

            self.Total_funds1 = (self.Total_funds1 - self.wd)
            print("Reserve Bank Account Balance is: ",self.Total_funds1)

        else:
            print("\nInsuficient Balance")
            print("Please Enter Your Available Balance")
            self.withdraw()

        #self.deposit()
        self.open_acc()
    
    def open_acc(self):
        self.open=int(input("\nEnter the Number of to open New Account: "))
        self.Total_accounts4 = (self.Total_accounts4 + self.open)
        print("Your Account is Successfully Created from our Chennai Bank")
        print("Total Account of City Union Bank is: ",self.Total_accounts4)

        self.Total_accounts3 = (self.Total_accounts3 + self.open)
        print("Total Account of Tamilnadu Bank is: ",self.Total_accounts3)
        self.Total_accounts2 = (self.Total_accounts2 + self.open)
        print("Total Account of State Bank is: ",self.Total_accounts2)
        self.Total_accounts1 = (self.Total_accounts1 + self.open)
        print("Total Account of Reserve Bank is: ",self.Total_accounts1)

        self.close_acc()

    def close_acc(self):
        self.close=int(input("\nEnter the Number of to Close Account: "))
        if self.Total_accounts4 >= self.close:
            self.Total_accounts4 = (self.Total_accounts4 - self.close)
            print("Your Account is successfully closed from our Bank")
            print("Total Account of City Union Bank is: ",self.Total_accounts4)

            self.Total_accounts3 = (self.Total_accounts3 - self.close)
            print("Total Account of Tamilnadu Bank is: ",self.Total_accounts3)
            self.Total_accounts2 = (self.Total_accounts2 - self.close)
            print("Total Account of State Bank is: ",self.Total_accounts2)
            self.Total_accounts1 = (self.Total_accounts1 - self.close)
            print("Total Account of Reserve Bank is: ",self.Total_accounts1)
        else:
            print("Sorry ",self.close," accounts is not here in our Chennai Bank")

        # self.deposit()


    
B=open(r"C:\Users\kaarv\Desktop\Bankingservice.txt","r+")
c=B.readlines()
B.close()

if c:
    y = eval(c[-1].replace("\n"," "))

    x=cub()
    x.Total_accounts1= y['rbi'][0]
    x.Total_funds1 = y['rbi'][1]
    x.Total_accounts2= y['sbi'][0]
    x.Total_funds2= y['sbi'][1]
    x.Total_accounts3= y['Tamilnadu_bank'][0]
    x.Total_funds3= y['Tamilnadu_bank'][1]
    x.Total_accounts4= y['cub'][0]
    x.Total_funds4= y['cub'][1]


   
else:
    x = cub()    

x.deposit()
# x.open_acc()
# x.close_acc()



A={'rbi':[],'sbi':[],'Tamilnadu_bank':[],'cub':[] }     

A['rbi'].extend([x.Total_accounts1,x.Total_funds1])


A['sbi'].extend([x.Total_accounts2,x.Total_funds2])


A['Tamilnadu_bank'].extend([x.Total_accounts3,x.Total_funds3])

A['cub'].extend([x.Total_accounts4,x.Total_funds4])

B=open(r"C:\Users\kaarv\Desktop\Bankingservice.txt","a+")
B.write('\n\n{0}'.format(A))
B.close()


#print(c[23])
