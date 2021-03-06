# Preston Hudson 11/23/19 Challenge 5 Written in Python

#1. Create a list of your favorite musicians.

favorite_musicians = []
favorite_musicians.append("Eminem")
favorite_musicians.append("Shawn Mendez")
favorite_musicians.append("One Ok Rock")

print(favorite_musicians)

#2. Create a list of tuples that contains a longitude and latitude of places you've been.

locations = []

red_oak = (32.5332, 96.8153)
waxahachie = (32.3865, 96.8483)
dallas = (32.7767, 96.7970)

locations.append(red_oak)
locations.append(waxahachie)
locations.append(dallas)

print(locations)

#3. Create a dictionary of things that describe you.

me_dictionary = {"Eye Color":"Hazel",
                    "First Name":"Preston",
                    "Last Name":"Hudson",
                    "Age":"23",
                    "Favorite Color":"Blue",
                    "Height":"6'3",
                    "Favorite Author":"J.R.R Tolkien"}

print(me_dictionary)

#4. Write a program that lets the user ask details about you from the me_dictionary.

n = input("Type a detail about me you would like to know:")
if n in me_dictionary:
    meDetail = me_dictionary[n]
    print(meDetail)
else:
    print("Detail not found.")

#5. Create a dictionary mapping your favorite muscians to a list of your favorite songs by them.

songs = ["Not Afraid", "Can't stop the feeling", "Stitches"]
music = {"Eminem":songs[0],
            "Justin Timberlake":songs[1],
            "Shawn Mendez":songs[2]}

print(music)

#6. When would you use a set in python?

#A common use of sets in Python is computing standard math operations such as union, intersection, difference, and symmetric difference.


#Complete
