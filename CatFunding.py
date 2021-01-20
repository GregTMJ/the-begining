from CatFunction import Cat, Client, info

cat_1 = Cat("Baron", 2, "Male")
cat_2 = Cat("Sam", 2, "Male")
print("the cats names are", cat_1.name, "and", cat_2.name)
print("Cat is", cat_2.age, "years old")
print("The cat is a", cat_2.gender)


client_1 = Client("Jimmy", 5000)
client_2 = info("Ivan Petrov", 5000, "Moscow", "Doctor")
print("Client:", client_1.name)
print("Balance:", client_1.balance)

man = [str(client_2.client_name()), str(client_2.client_balance()),
       str(client_2.adress_1()), str(client_2.prof_1())]
print(man)
