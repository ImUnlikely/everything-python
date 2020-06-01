names = ["Bruce", "Clark", "Peter", "Logan", "Wade"]
heros = ["Batman", "Superman", "Spiderman", "Wolverine", "Deadpool"]

my_dict = {name: hero for name, hero in zip(names, heros)}
print(my_dict)

# if name not equal to Peter
my_dict = {name: hero for name, hero in zip(names, heros) if name != "Peter"}
print(my_dict)