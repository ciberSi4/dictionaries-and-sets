# Словари и множества

# 2. Работа со словарями:

print("2. Работа со словарями:")
my_dict = { "Ivan" : 1997, "Kaban" : 1999, "Bratan" : 2011 }
print( my_dict , type ( my_dict ) )
print( my_dict ["Kaban"])
print( my_dict.get ("Petr", "Такого нет"))
my_dict.update ( { "Sergei" : 2000,
                   "Grisha" : 2002} )
a = my_dict.pop( "Bratan")
print ( "Братан -", a )
print( my_dict )

# 3. Работа с множествами:

print("3. Работа с множествами:")
my_set  = { 1, 2, 3, 4, 5, 4, 3, 2, 1 }
my_set.add( 6 )
my_set.add( 7 )
print( "Проконтролировали добавление: ", my_set )
my_set.discard ( 4 )
print( "Вывод на экран измененного множества my_set: ", my_set )