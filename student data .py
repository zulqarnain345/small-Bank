class student:
    def __init__(self):
        print(f"{"-"*6} welcome to the student data app {"-"*6}")
        self.name=[]
        self.Marks=[]
        self.age=[]
        while True:
            self.num=input("enter how many student data you have " \
            "to enter or press q to exit:: ")
            if self.num.isdigit() or self.num.lower() == "q":
                self.exit()
                break
            else:
                print("Invalid entry")

    def exit(self):
        if self.num =="q" or self.num=="Q":
            print("thanks visting our website ")
            exit()
        elif (self.num.isdigit()):
            self.num=int(self.num)
        else:
            print("invalid entery")
            exit()   
            
        

    def data(self):
        for i in range(1,self.num+1):
            name=input(f"enter the name of {i}:: ")
            age=int(input(f"enter the age of student {i}:: "))
            marks=int(input(f"enter the marks of student {i}:: "))
            print(" ")

            self.name.append(name)
            self.age.append(age)
            self.Marks.append(marks)
            
            

           


    def show(self):
        print("student record\n")
        for i in range(self.num):
            print(f"NAME of {i+1}:: {self.name[i]}")
            print(f"AGE of {i+1}:: {self.age[i]}")
            print(f"MARK of {i+1}:: {self.Marks[i]}")
            print(" ")


    def average(self):
        self.sum=0
        for i in range(self.num):
           self.sum=   self.sum+self.Marks[i]

        self.avg=self.sum/self.num
        print(f"the average of the class is:: {self.avg} ")


    def filewrite(self):
        with open("student.txt","w")as f:
            f.write("student record\n")
            for i in range(self.num):
                f.write(f"NAME of {i+1}:: {self.name[i]}\n")
                f.write(f"AGE of {i+1}:: {self.age[i]}\n")
                f.write(f"MARK of {i+1}:: {self.Marks[i]}\n")
                f.write(" \n")
                        
    
    def find_topper(self):
        highest_mark = max(self.Marks)  
        topper_index = self.Marks.index(highest_mark) 
        print(f"topper is {self.name[topper_index]} with {highest_mark} marks")


    def find_lower(self):
        lower_mark= min(self.Marks)
        lower_index= self.Marks.index(lower_mark)
        print(f"lower is {self.name[lower_index]} with {lower_mark} marks")


    def datashow(self):
        print("1) STUDENTS DATA ")
        print("2) HIGHEST MARKS  ")
        print("3) LOWERST MARKS ")
        print("4) AVERAGE OF THE CLASS ")
        while True:
            self.num3=input("enter the number (1,2,3.....) what you want to see "
            "or press q to exit::  ")
            if (self.num3=="q" or self.num3=="Q"):
                print(" thanks for visiting ")
                break
            if not self.num3.isdigit():
                print("enter the valid number between the 1 to 4 ")
                continue
            self.num3=int(self.num3)


            if(self.num3==1):
                print(" STUDENTS DATA ")
                self.show()

            elif(self.num3==2):
                print(" HIGHEST MARKS  ")
                self.find_topper()
                    

            elif(self.num3==3):
                print(" LOWERST MARKS ")
                self.find_lower()

            elif(self.num3==4):
                print(" AVERAGE OF THE CLASS ")
                self.average()   
                        




            

       



s=student()
s.data()
s.datashow()
s.filewrite()


                    

                

