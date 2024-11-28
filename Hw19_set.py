#start--
#HW19--
oscar_winners = {"Leonardo DiCaprio", "Meryl Streep", "Denzel Washington",
                 "Emma Stone", "TomHanks", "Natalie Portman", "Robert De Niro", "Al Pacino"}
titanic_actors = {"Leonardo DiCaprio", "Kate Winslet", "Billy Zane", "Kathy Bates"}
dark_knight_actors = {"Christian Bale", "Heath Ledger", "Michael Caine",
                      "Gary Oldman", "Aaron Eckhart"}
avengers_actors = {"Robert Downey Jr.", "Chris Evans", "Scarlett Johansson",
                   "Mark Ruffalo", "ChrisHemsworth", "Jeremy Renner"}
iron_man_actors = {"Robert Downey Jr.", "Gwyneth Paltrow", "Terrence Howard"}
legendary_actors = {"Al Pacino", "Robert De Niro", "Marlon Brando",
                    "Jack Nicholson", "Dustin Hoffman"}
actor_list = {"Robert Downey Jr.", "Chris Evans", "Scarlett Johansson",
              "Leonardo DiCaprio", "Tom Hanks"}
movie_cast = {"Tom Hanks", "Tom Cruise", "Will Smith", "Matt Damon", "Brad Pitt"}

#a -הוסף את השחקנית Watson Emma לרשימת זוכי הא
oscar_winners.add('Watson Emma')
print(oscar_winners)

# b. צור העתק של רשימת זוכי האוסקר . ב רשימת ההעתק:
oscar_winners_copy = oscar_winners.copy()
print("copy:", oscar_winners_copy)
# הסר את השחקנית מריל סטריפ
oscar_winners_copy.discard("Meryl Streep"'')
print(oscar_winners_copy)
# נקה את כל האיברים ברשימה
oscar_winners_copy.clear()
print(oscar_winners_copy)

# c. אילו שחקנים הופיעו גם בטיטניק וגם באביר האפל?
titanic_and_dark = titanic_actors.intersection(dark_knight_actors)
print('titanic and dark: ',titanic_and_dark)

# d. האם יש שחקנים שמופיעים ב-man iron ונוקמים?
marvel = iron_man_actors & avengers_actors
if len(marvel) > 0:
    print("True- 'marvel'",marvel)
else:
    print(False)

# e. האם כל השחקנים ברשימה "list_actor "זכו באוסקר?
actor_in_oscar = actor_list <= oscar_winners
print("actor_in_oscar",actor_in_oscar)

# f. האם שחקני "list_actor "כוללת את כל השחקנים שהופיעו בנוקמים?
if avengers_actors in actor_list:
    print(True)
else:
    print(False)

# g. הסר באופן אקראי שחקן אחד מתוך set השחקנים "cast_movie"
movie_cast.pop()
print(movie_cast)

# h. הסר את השחקן Damon Matt מתוך רשימת השחקנים "cast_movie"
movie_cast.discard("Matt Damon")
print(movie_cast)

# i. אילו שחקנים ששיחקו בטיטניק לא זכו באוסקר?
not_won = titanic_actors.difference(oscar_winners)
print("not_won: ",not_won)

# j. אילו שחקנים הופיעו רק באחד מהסרטים, טיטניק או האביר האפל?
print("j ----" ,titanic_actors ^ dark_knight_actors)
# k. עדכן את רשימת זוכי האוסקר והוסף את Blanchett Cate ו - Lewis-Day Daniel
actor_list.add('Cate Blanchett')
actor_list.add('Lewis-Day Daniel')
print('add: ',actor_list)

# l. אחד את רשימת השחקנים של טיטניק והאביר האפל כדי לראות את שמות
# כל השחקנים
union_set = titanic_actors.union(dark_knight_actors)
print('union_set: ',union_set)