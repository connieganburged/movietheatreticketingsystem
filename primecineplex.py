"""
Cinema
By Connie
"""
print ("Hello, welcome to Prime Cineplex. How can I help you today?")
info = None
while info not in ('yes','no'):
    info= input('Would you like to connect to a live admin? (yes/no): ')
if info == 'yes':
    print('An admin will contact you shortly, please wait. Thank you.')
if info == 'no':
    choice = input('1. Location and Work Hours, 2. Phone Number and Contact, 3. Prices 4. Book a Movie: ')

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
        print ('Here are the movie choices. 1. Barbie 2. Zootopia 3. Annabelle 4. Florence Maybe 5. Shang-Chi.')
        movie_choice = input ("Choose 1 2 3 4 or 5: ")




print('Thank you. Have a nice day!')
