# -*- coding: utf-8 -*-

class car:
    
    def __init__(self,typec,days,km):
        self.typec=typec
        self.days=days
        self.km=km
        
    def status(self):
        
                
        if self.typec=="Sedan":
            
            payment=8*self.days+2*self.km
            print("Payment amount of your rentcar {}  type is {} $ for {} days and {} km.".format(self.typec,payment,self.days,self.km))
            
            

        elif self.typec=="Hatchback":
            
            payment=10*self.days+4*self.km
            print("Payment amount of your rentcar {}  type is {} $ for {} days and {} km.".format(self.typec,payment,self.days,self.km))
            
            

        elif self.typec=="Sport":
            
            payment=12*self.days+6*self.km
            print("Payment amount of your rentcar {}  type is {} $ for {} days and {} km.".format(self.typec,payment,self.days,self.km))
            
             
        else:
            print("we have not this car.")
                                   
print(""""
      Welcome to our Car Rental application.
      1.Sedan
      2.Hatchback
      3.Sport
      4.Exit
      
      Please select the numbers.""")
while True:
    
    choice=input("Which one? : ")
    
    km=float(input("how many km will you drive? :"))
    
    days=int(input("how many days will you drive? :"))
    
    if choice=="1":
        care="Sedan"
    elif choice=="2":
        care="Hatchback"
    elif choice=="3":
        care="Sport"
    elif choice=="4":
        print("You are logged out. Have a nice day.")
        break
    else:
        print("You made the wrong choice.")
    
    c=car(care,days,km)
    c.status()
        





          
    