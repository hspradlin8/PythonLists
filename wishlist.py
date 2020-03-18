#list insert() method: adds an element at the specified position. 

# list pop() method: removes an element from a list:
# Ex: books.pop(1): this will remove the 2nd book from the list.

books = [
    "Learning Python: Powerful Object-Oriented Programming - Mark Lutz",
    "Automate the Boring Stuff with Python: Practical Programming for Total Beginners - Al Sweigart",
    "Python for Data Analysis - Wes McKinney",
    "Fluent Python: Clear, Concise, and Effective Programming - Luciano Ramalho",
    "Python for Kids: A Playful Introduction To Programming - Jason R. Briggs",
    "Hello Web App: Learn How to Build a Web App - Tracy Osborn",
]

video_games = [
    "The Legend of Zelda: Breath of the Wild",
    "Splatoon 2",
    "Super Mario Odyssey",
]



#print("Books:")
#for book in books:
    #print("*" + book)
    
def display_wishlist(display_name, wishes):
    items = wishes.copy()
    print(display_name + ":") 
    suggested_gift = items.pop(0)
    print("=======>", suggested_gift, "<=======")
    for item in items:
        print("*" + item)
    print()

display_wishlist("Books", books)
display_wishlist("Video Games", video_games)