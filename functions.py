"""def display_messages():
    print("I'm learning functions!")

display_messages()

def favourite_book(title):
    print(f"My favourite book is {title}")

favourite_book("Harry Potter")"""

"""def make_album(artist,title,amount_of_songs = None):
    if amount_of_songs:
        album = {"name_of_the_artist":artist,"title_of_the_album":title,"amount":amount_of_songs}
    else:
        album = {"name_of_the_artist":artist,"title_of_the_album":title}
    return album

albums=[]

while True:
    artist = input("Artist: ")
    if artist == "Q":
        break
    title = input("Title: ")
    amount_of_songs = input("Amount of songs (press enter to skip): ")
    if amount_of_songs.isdigit():
        album = make_album(artist, title, amount_of_songs)
    else:
        album = make_album(artist, title)
    albums.append(album)

print(albums)"""

short_messages = ["Watch out","Take a look","Take it", "Leave it"]
sent_messages = []

def show_messages(messages):
    for message in messages:
        print(message)

def transfer_messages(messages):
    for message in messages:
        sent_messages.append(message)
    print(sent_messages)

show_messages(short_messages)
transfer_messages(short_messages)
transfer_messages(short_messages[:])


    
