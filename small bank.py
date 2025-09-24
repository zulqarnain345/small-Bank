class bank:
    def __init__(self):
        print(f"{"-"*6} welcome to the BANK {"-"*6}")
        print(" ")
        print(" ")


    def choice(self):
        print("1)NEW BANK ACCOUNT OPEN")
        print("2)CHECK ACCOUNT BALANCE")    
        print("3)ATM USE")    

        while True:
            self.num=input("choice the type of the bank (1,2,3):: or prees q to exit ")
            if(self.num.lower()=="q"):
                print("thanks for visting")
                break
            if not self.num.isdigit():
                print("enter the valid number between the 1,2 ,3")
                continue
            self.num=int(self.num)

            if self.num not in [1,2,3]:
                print("enter the valid number between the 1,2 ,3")
                continue
            break

        if(self.num==1):
            self.new_bank_account()

        elif(self.num==2):
            self.check_balance()   

        elif(self.num==3):
            self.ATM()




    


        
    def check_balance(self):
        while True:
            self.cnic1=input("enter the 3 number cnic no:: ")
            self.pin1=input("enter the 4 digit pin:: ")
            if(len(self.cnic1) !=3 ):
                print("invalid cnic no enter correct cnic ")
            elif(len(self.pin1)!=4):
                print("invalid pin enter correct pin ")

            else:
                break
        self.read()    


    def read(self):
        found=False
        with open("atm.txt","r")as f:
            for line in f:
                self.data=line.strip().split(",")
                if len(self.data)<6:
                    continue
                if self.data[0].lower() == "name":  
                    continue

                self.name=self.data[0]
                self.cnic=self.data[2]
                self.pin=self.data[3]
                self.deposite_new_account=int(self.data[4])
                if(self.cnic==self.cnic1 and self.pin==self.pin1):
                    found =True
                    break
        if found:
            print(f"DATA MATCH \n welcome back {self.name}")   
            print(f"MR {self.name} YOUR BANK BALANCE IS {self.deposite_new_account}")

        else:
            print("DATA NOT FOUND ")    


             


        

    def write(self):

        with open("atm.txt","a")as f:
           
            f.write(f"{self.name},{self.age},{self.cnic},{self.pin},{self.deposite_new_account},{self.card}\n")

            
    def ATM(self):
        print(f"{"-"*6} welcome to the ATM {"-"*6}")

        self.check_balance()



        self.witdraw=int(input("enter how many cash you have to withdraw "))

        if self.witdraw > self.deposite_new_account:
            print("you donot have that much money in your account ")
        else:    
            self.deposite_new_account=self.deposite_new_account-self.witdraw
            print(f"you remaning balance is {self.deposite_new_account}")
        lines=[]
        with open("atm.txt","r") as f:
            for line in f:
                data=line.strip().split(",")
                if len(data)<6:
                    continue
                if data[2] == self.cnic1 and data[3] ==self.pin1:
                    data[4]=str(self.deposite_new_account)
                    line=",".join(data) +"\n"
                lines.append(line)    

        with open("atm.txt","w") as f:
            f.writelines(lines)




    def new_bank_account(self):
        self.name=input("enter the name:: ")
        self.age=int(input("enter the age:: "))
        if (self.age<15):
            print("sorry we will not open your account")
        else:    
            while True:
                self.cnic=input("enter the 3 number cnic no:: ")
                self.pin=input("enter the pin of your account in 4 digit:: ")

                if(len(self.cnic) !=3 or len(self.pin) !=4):
                    print("invalid cnic no or pin ")
                    print("enter the 4 digit pin and 3 digit cnic to continue ")
                else:
                    break
            

            print("1)SAVING ACCOUNT")
            print("2)CURRENT ACCOUNT")    
            print("3)MONEY ACCOUN") 
            while True:
                self.type=input("choice the type of the bank (1,2,3):: or prees q to exit ")
                if(self.type.lower()=="q"):
                    print("thanks for visting")
                    break
                if not self.type.isdigit():
                    print("enter the valid number between the 1,2 ,3 ")
                    continue
                self.type=int(self.type)

                if self.type not in [1,2,3]:
                    print("enter the valid number between the 1,2 ,3 ")
                    continue
                print(f"user enter the {self.type} ")
                break

            self.choice1()
            

    
    def atm_type(self):
        print("1)DEBIT CARD")
        print("2)MASTER CARD")  
        while True:
            self.card=int(input(f"YOU CHOICE THE CARD CATEGORY:: "))
            if self.card not in [1,2]:
                print("PLZ SELECT THE CARD TYPE (1,2) ")
            else:
                break    
        if(self.card==1):
            print("YOUR DEBIT CARD WILL ARVIED IN 3 WROKING DAYS")
        else:
           print("YOUR MASTER CARD WILL ARVIED IN 5 WROKING DAYS")

                                  


    def choice1(self):
            if(self.type==1):
                print("SAVING ACCOUNT")
                print("to open the saving account you have to deposit the more then 1 lac ")

                self.deposite_new_account=int(input("enter the amount you want to deposit:: "))

                if(self.deposite_new_account<=100000):
                    print("sorry you donot open the saving account becuse of small amount")
                else:
                    print("welcome to the bank")

                    print("")

                    self.atm_type()

                                  

                self.write()    


            elif(self.type==2):
                print("CURRENT ACCOUNT")
                print("to open the CURRENT ACCOUNT you have to deposit the more then 10000 ")

                self.deposite_new_account=int(input("enter the amount you want to deposit:: "))

                if(self.deposite_new_account<=10000):
                    print("sorry you donot open the CURRENT ACCOUNT becuse of small amount")
                else:
                    print("welcome to the bank")

                self.write() 

                print("")
                self.atm_type()



                                  

            elif(self.type==3):
                print("MONEY ACCOUN") 
                print("to open the MONEY ACCOUN you have to deposit the more then 1000 ")

                self.deposite_new_account=int(input("enter the amount you want to deposit:: "))

                if(self.deposite_new_account<=1000):
                    print("sorry you donot open the MONEY ACCOUN becuse of small amount")
                else:
                    print("welcome to the bank")

                self.write() 

                print("")

                self.atm_type()

                                            
                    

            else:
                print("enter invalid number")        





b=bank()
b.choice()
    

