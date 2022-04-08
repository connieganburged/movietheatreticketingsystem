"""
Cinema
By Connie
"""
from tkinter import N

#If rebook is chosen, the program will restart 
rebook = 'yes'
while rebook == 'yes':  
   #Seats 
   seats = (([3,4], [ ], [ ]), ([ ], [ ], [ ]), ([ ], [ ], [ ]))

   def func1():
      print("Being processed, please wait.")
   
   info = None
   while info not in ('yes','no'):
      info= input('Would you like to connect to a live admin? (yes/no): ')
   if info == 'yes':
      print('An admin will contact you shortly, please wait. Thank you.')
   if info == 'no':
      choice = input('1. Location and Work Hours, 2. Phone Number and Contact, 3. Prices 4. Book a Movie: ')

   #Provide the service they requested
      func1()
      match choice:
        case '1':
            print('We are located in Encanto Tower and Zaisan Hill from 10:00-0:00')
        case '2':
            print('Call us at +976 7510 0000. Our website is primecineplex.mn')
        case '3':
            print('a. General Admission, b. Dolby Atmos, c. VIP')
            choice = input ('a b or c: ')
            match choice:
                case 'a':
                    print('ADULT 2D: 9,00 3D: 10,000 CHILD 2D: 6,000 3D: 7,000')
                case 'b':
                    print('ADULT 2D: 6,500 3D: 11,000 CHILD 2D: 6,500 3D: 7,000')
                case 'c':
                    print('20,000')
                case 'd':
                    print('2D: 15,000 3D: 16,000')
        case '4':
        #Display movies
            print ('Here are the movie choices. 1. Barbie 2. Zootopia 3. Annabelle')
        #validate movie choice
            movie_choice = None
            while movie_choice not in ('1', '2', '3'):
                movie_choice = input ("Choose 1 2 or 3: ")        
            movie_choice = int(movie_choice)
        
        #Display movies
            print ('Here are the sessions. 1. Morning 2. Afternoon 3. Evening')
        #validate movie choice
            session_choice = None
            while session_choice not in ('1', '2', '3'):
                session_choice = input ("Choose 1 2 or 3: ")
            session_choice = int(session_choice)

        #Display seats
            print ('Available seats')
            seats_text = ''
            for seat in range(1,21):
                if seat in seats[movie_choice-1][session_choice-1]:
                    seats_text = seats_text + ' X'
            else:
                seats_text = seats_text + f' {seat}'
            print (seats_text)

        #Seat number
            chosen_seat = None
            while chosen_seat not in range(1,21):
                try: 
                    chosen_seat = int(input("What is your seat choice: "))
                except: 
                    print("Sorry, that is not valid")
                continue
            if chosen_seat not in range(1,21): 
                print("Seat not available, choose a different seat")
                chosen_seat = None
               
   #print order information
   print(f"Movie: {movie_choice}, Time: {session_choice}, Seat: {chosen_seat}")

   correct = None
   #check if information is correct
   while correct not in ('yes', 'no'):
       correct = (input("Is the information correct? ")).lower()
       if correct == 'yes':
           print('Thank you for your order. ')
       elif correct == 'no':
           print(movie_choice, session_choice, chosen_seat)

   rebook = None
   #Ask if they want to rebook
   while rebook not in ('yes','no'):
      rebook = (input("Would you like to rebook your order? "))
      if rebook == 'yes':
         print('Rebooking is starting: ')
         continue
      elif rebook == 'no':
         print("Thank you for choosing Prime Cineplex!")

   print('Have a nice day!')
