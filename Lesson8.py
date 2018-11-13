# tuples, list, dictinary
# days=("Monday", "Tuesday","Wednesday","Thursday","Friday")
#
# print(days[0] ,  days[1])
#
# d1= days[1:]
#
# print(d1)
#
# d2= days[1:3]
# print(d2)
#
#
# d3=days[:2]
# print(d3)
#
# size = len(days)
# print(size)
#
# print(len(days[0]))
#
# days2=["Monday", "Tuesday","Wednesday","Thursday","Friday"]
# print(days2[3])
# print(days2[2:3])
# print(len(days2))
# days2.append("Saturday")
# print(len(days2))
#
# # days2.clear()
# # print(len(days2))
# days2.remove("Tuesday")
# print(days2)
# days2.pop(1)
# print(days2)

#

# sort it ascending
# sort desc
# avg
# least and the highest
# top ten
scores = [80, 67, 99, 45, 63, 95, 11, 34, 56, 778, 784, 73, 858, 53, 90, 85, 38, 59, 43, 21, 11, 23, 48, 525, 537, 657,
          849, 848, 267, 788, 257, 73, 736, 889, 4567, 567]
# scores.sort()
#
# print(scores)
# scores.reverse()
# print(scores)
#
# x = len(scores)
# cal = sum(scores)
#
# print("Length is ", x)
# print("avarage is " , cal/x)
#
# print(max(scores))
# print(min(scores))
#
# print(scores[26:])
# print(scores[:10])

from operator import itemgetter

# scores.sort(reverse=True)
#
# print(scores)
#
# student={"names":"Mike Doe", "age":19, "gender":"Male"}
#
# print(student["gender"], student["names"])


students = [{"names": "Cchaddie Grishaev", "age": 18, "gender": "Male"},
            {"names": "Gawen Sked", "age": 15, "gender": "Male"},
            {"names": "Arleyne Petofi", "age": 13, "gender": "Female"},
            {"names": "Laetitia Gounard", "age": 18, "gender": "Female"},
            {"names": "Alvinia Elven", "age": 15, "gender": "Female"},
            {"names": "Jocko Hinsch", "age": 16, "gender": "Male"},
            {"names": "Randa Laurenceau", "age": 16, "gender": "Female"},
            {"names": "Myranda Abrahmovici", "age": 18, "gender": "Female"},
            {"names": "Jackelyn Cusworth", "age": 13, "gender": "Female"},
            {"names": "Corenda Geeritz", "age": 19, "gender": "Female"},
            {"names": "Emmit Beals", "age": 15, "gender": "Male"},
            {"names": "Penelope Spens", "age": 19, "gender": "Female"},
            {"names": "Chadwick Gershom", "age": 19, "gender": "Male"},
            {"names": "Martie Bernini", "age": 14, "gender": "Female"},
            {"names": "Pandora Olyet", "age": 16, "gender": "Female"},
            {"names": "Craggie Summerlee", "age": 18, "gender": "Male"},
            {"names": "Dredi Sprouls", "age": 16, "gender": "Female"},
            {"names": "Noelani Clemmett", "age": 17, "gender": "Female"},
            {"names": "Arda Edel", "age": 14, "gender": "Female"},
            {"names": "Lidia Caruth", "age": 14, "gender": "Female"},
            {"names": "Christian Mayho", "age": 18, "gender": "Female"},
            {"names": "Kelli Kunert", "age": 17, "gender": "Female"},
            {"names": "Irvin Hoffmann", "age": 12, "gender": "Male"},
            {"names": "Marion Berthon", "age": 20, "gender": "Female"},
            {"names": "Alida Haig", "age": 15, "gender": "Female"},
            {"names": "George Menci", "age": 17, "gender": "Female"},
            {"names": "Karola Prentice", "age": 16, "gender": "Female"},
            {"names": "Tallie Boston", "age": 18, "gender": "Male"},
            {"names": "Jeffie Beed", "age": 17, "gender": "Male"},
            {"names": "Fleming Bilsford", "age": 14, "gender": "Male"},
            {"names": "Sterne Schimpke", "age": 17, "gender": "Male"},
            {"names": "Gertrudis Labuschagne", "age": 13, "gender": "Female"},
            {"names": "Nikolos Mogridge", "age": 20, "gender": "Male"},
            {"names": "Lira Ayree", "age": 15, "gender": "Female"},
            {"names": "Deeanne Levicount", "age": 14, "gender": "Female"},
            {"names": "Maribel Sibson", "age": 20, "gender": "Female"},
            {"names": "Vernen Mariot", "age": 14, "gender": "Male"},
            {"names": "Biron Nial", "age": 20, "gender": "Male"},
            {"names": "Jeffie Shallcross", "age": 19, "gender": "Male"},
            {"names": "Katusha Veivers", "age": 18, "gender": "Female"},
            {"names": "Benedick Harkness", "age": 20, "gender": "Male"},
            {"names": "Tarrance Millichap", "age": 15, "gender": "Male"},
            {"names": "Emiline Kemitt", "age": 15, "gender": "Female"},
            {"names": "Charmaine Cluelow", "age": 20, "gender": "Female"},
            {"names": "Daisi Bugbird", "age": 20, "gender": "Female"},
            {"names": "Dorelia Hartford", "age": 14, "gender": "Female"},
            {"names": "Gothart Olyfant", "age": 14, "gender": "Male"},
            {"names": "Udell Brunker", "age": 20, "gender": "Male"},
            {"names": "Della Seeviour", "age": 19, "gender": "Female"},
            {"names": "Robinet Itzchaki", "age": 13, "gender": "Male"},
            {"names": "Read Danbi", "age": 12, "gender": "Male"},  # 2
            {"names": "Maire Pippin", "age": 13, "gender": "Female"},
            {"names": "Fee Gillon", "age": 13, "gender": "Male"},
            {"names": "Eloisa Drawmer", "age": 16, "gender": "Female"},
            {"names": "Elladine MacRirie", "age": 14, "gender": "Female"},
            {"names": "Cordie Asprey", "age": 18, "gender": "Male"},
            {"names": "Cliff Philip", "age": 20, "gender": "Male"},
            {"names": "Etta Corkhill", "age": 19, "gender": "Female"},
            {"names": "Angeli Monahan", "age": 15, "gender": "Male"},
            {"names": "Fawn Goring", "age": 15, "gender": "Female"},
            {"names": "Rurik Gurner", "age": 13, "gender": "Male"},
            {"names": "Shaw Polet", "age": 12, "gender": "Male"},  # 1
            {"names": "Ketty Meininking", "age": 13, "gender": "Female"},
            {"names": "Roosevelt O'Henehan", "age": 16, "gender": "Male"},
            {"names": "Farica Mobbs", "age": 15, "gender": "Female"},
            {"names": "Beryl O'Tuohy", "age": 17, "gender": "Female"},
            {"names": "Any Gallone", "age": 19, "gender": "Male"},
            {"names": "Birdie Gino", "age": 16, "gender": "Female"},
            {"names": "Alexander Lundy", "age": 17, "gender": "Male"},
            {"names": "Berkley Brawn", "age": 14, "gender": "Male"},
            {"names": "Brock Metzke", "age": 13, "gender": "Male"},
            {"names": "Vance Vella", "age": 19, "gender": "Male"},
            {"names": "Francisca Volet", "age": 15, "gender": "Female"},
            {"names": "Audrie Jarnell", "age": 12, "gender": "Female"},  # 3
            {"names": "Michell Sangra", "age": 16, "gender": "Female"},
            {"names": "Arman Bowery", "age": 13, "gender": "Male"},
            {"names": "Bebe Jeandillou", "age": 14, "gender": "Female"},
            {"names": "Donnell Eneas", "age": 18, "gender": "Male"},
            {"names": "Tammie Gamil", "age": 16, "gender": "Male"},
            {"names": "Dyana Strattan", "age": 18, "gender": "Female"},
            {"names": "Florenza Haulkham", "age": 17, "gender": "Female"},
            {"names": "Catherine Hise", "age": 20, "gender": "Female"},
            {"names": "Wyndham Janes", "age": 20, "gender": "Male"},
            {"names": "Claudio Putson", "age": 17, "gender": "Male"},
            {"names": "Jeffie Janicki", "age": 20, "gender": "Male"},
            {"names": "Pepi Metham", "age": 16, "gender": "Female"},
            {"names": "Billie Carlisi", "age": 20, "gender": "Male"},
            {"names": "Martin Aiston", "age": 18, "gender": "Male"},
            {"names": "Lezlie Paulus", "age": 14, "gender": "Female"},
            {"names": "Scott Brydie", "age": 18, "gender": "Male"},
            {"names": "Tucky Marsie", "age": 16, "gender": "Male"},
            {"names": "Loreen Sarver", "age": 20, "gender": "Female"},
            {"names": "Brigit Whilder", "age": 14, "gender": "Female"},
            {"names": "Elwin Raiston", "age": 13, "gender": "Male"},
            {"names": "Lindie Peckham", "age": 17, "gender": "Female"},
            {"names": "Alexia O'Glassane", "age": 13, "gender": "Female"},
            {"names": "Nevins Callcott", "age": 20, "gender": "Male"},
            {"names": "Olly Simcox", "age": 13, "gender": "Female"},
            {"names": "Arluene Wyss", "age": 19, "gender": "Female"},
            {"names": "Jorry Widdocks", "age": 20, "gender": "Female"}]

students.sort(key=itemgetter("age"), reverse=True)
# import pandas as pd
# import numpy as np
# s1= students[0]
#
# print(s1["names"])
#
print(len(students))
length = len(students)
ages = 0
for person in students:
    ages += person["age"]

print("total age", ages)
avg = ages / length
print(avg)

# print(students["name"])
for student in students:
 if student["age"] <= avg:
# print(len(students))
  print(student["names"], student["age"])
# print(len(student["names"]))

# scores.sort(reverse=True)

print(students[97:100])

# avg = ages/\
# l = len(students)
# print(ages/l)
# avg = ages/ l

# avg age
# Three youngest
# All students below avg age
# students.sort(key=itemgetter("age"), reverse=True)


#
#
# for students in students:
#      print( students[len("age"))
