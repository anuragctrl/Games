import random 
choice = random.randint(1,100)
c=0
while True :
    try:
        n = int(input("Guess The  Number "))
        c+=1
        if n > choice :
           print("Too High")    
        elif n < choice: 
          print("Too Low")
        else: 
          print(f"Congratulations You Successfully Guess The Number At {c} Attempt ")
          break
        
    except ValueError:
          print("Enter a Valid Number ") 
         
      