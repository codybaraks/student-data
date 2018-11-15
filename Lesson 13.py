# functions
def talk_to_the_parrot():
    print("hello world lets learn python")

talk_to_the_parrot()


def conversation(name,names):
        print("Keneth is a good guy and he's ok!")
        print("{} sleeps all day and {} works all day".format(name,names))


conversation("KENNETH", "he")

# handling exceptions

try:
    count = int(input("Give me a number:"))
except ValueError:
    print("Thats not a number")
else:
    print(count * "hello world")

# Shopping cart
shopping_cart = []
print("Choose the items you want in the shopping cart")
print("Enter [DONE] once your done!")

while True:
     try:
      new_item = str(input(" > "))
      if new_item == 'DONE'.lower() or new_item == 'done'.upper():
          break
      # Add new items
      shopping_cart.append(new_item)
     except:
         pass

print("Here's your list")

for item in shopping_cart:
      print(item)
print("--------------------")

if len(shopping_cart) > 3:
    print(shopping_cart[0], shopping_cart[1])
else:
    for item in shopping_cart:
        print(item)