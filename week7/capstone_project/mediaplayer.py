import random


class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.num = None

    def getTitle(self):
        return self.title

    def getArtist(self):
        return self.artist

    def __str__(self):
        return f"{self.num}. {self.title} by {self.artist}"

    def __eq__(self, other):
        return ((self.title, self.artist) == (other.title, other.artist))

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return ((self.title, self.artist) < (other.title, other.artist))

    def __gt__(self, other):
        return ((self.title, self.artist) < (other.title, other.artist))


class Playlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None
        self.num_songs = 0

    def addSong(self, song):
        newNode = Node(song)

        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

        if self.current is None:
            self.current = self.head

        self.num_songs += 1
        song.num = self.num_songs

    def removeSong(self, song):
        currNode = self.head
        prevNode = None

        while currNode is not None:
            if currNode.data == song:
                if prevNode is None:
                    self.head = currNode.next
                else:
                    prevNode.next = currNode.next

                if currNode.next is None:
                    self.current = self.tail
                else:
                    self.current = currNode.next

                if currNode is self.tail:
                    self.tail = prevNode
                self.num_songs -= 1  

                return True

            prevNode = currNode
            currNode = currNode.next

        return False

    def play(self):
        if self.current is None:
            return None
        else:
            return self.current.data

    def skip(self):
        if self.current is None:
            return None
        elif self.current.next is None:
            self.current = self.head
        else:
            self.current = self.current.next

        return self.current.data

    def goBack(self):
        if self.current is None:
            return None
        elif self.current is self.head:
            currNode = self.tail
            
        else:
            currNode = self.head
            while currNode.next is not None and currNode.next is not self.current:
                currNode = currNode.next

        self.current = currNode
        return self.current.data if self.current else None  

    def custom_shuffle(self):
        songList = []
        currNode = self.head
        while currNode is not None:
            songList.append(currNode.data)
            currNode = currNode.next
        print("Original playlist: ")
        self.showPlaylist()

        for last_index in range(len(songList)-1, 0, -1):
            random_index = random.randint(0, last_index)
            songList[last_index], songList[random_index] = songList[random_index], songList[last_index]

        self.head = None
        self.tail = None
        self.current = None
        self.num_songs = 0

        for song in songList:
            self.addSong(song)

        print("Shuffled playlist: ")
        self.showPlaylist()

    def getCurrentSong(self):
        if self.current is None:
            return "No song is currently playing"
        else:
            currNode = self.head
        while currNode is not None:
            if currNode.data == self.current.data:
                return currNode.data
            currNode = currNode.next
        return "Current song not found in playlist"
       
    def showPlaylist(self):
        if self.head is None:
            print("The playlist is empty.")
            return
        currNode = self.head
        while currNode is not None:
            print(currNode.data)
            currNode = currNode.next


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


def menu():
    print(20 * "-", "MENU", 20 * "-")
    print("1. Add Song to Playlist")
    print("2. Remove song from Playlist")
    print("3. Play")
    print("4. Skip")
    print("5. Go Back")
    print("6. Shuffle")
    print("7. Show Currently Playing Song")
    print("8. Show Current Playlist Order")
    print("0. Exit")
    print(47 * "-")


playlist = Playlist()
playlist.addSong(Song("Duke Of Earl", "Gene Chandler "))
playlist.addSong(Song("This I swear", "The Skyliners "))
playlist.addSong(Song("Those Oldies but Goodies",
                 "Little Cesar & The Romans "))
playlist.addSong(Song("You Were Mine", "The Fireflies "))
playlist.addSong(Song("Raindrops", "Dee Clark "))
playlist.addSong(Song("Twist and Shout", "The Isley Brothers "))

while True:
    menu()
    choice = int(input())

    if choice == 1:
        title = input("Enter song title: ")
        artist = input("Enter artist name: ")
        playlist.addSong(Song(title, artist))
        print("New Song Added to Playlist")
    elif choice == 2:
        title = input("Enter song title to remove: ")
        artist = input("Enter artist name: ")
        if playlist.removeSong(Song(title, artist)):
            print("Song Removed from Playlist")
        else:
            print("Song not found in Playlist")
    elif choice == 3:
        song = playlist.play()
        if song is None:
            print("Playlist is empty")
        else:
            print("Playing:", song)
    elif choice == 4:
        song = playlist.skip()
        if song is None:
            print("Playlist is empty")
        else:
            print("Skipping to:", song)
    elif choice == 5:
        song = playlist.goBack()
        if song is None:
            print("Playlist is empty")
        else:
            print("Going back to:", song)
    elif choice == 6:
        playlist.custom_shuffle()
        song = playlist.play()
        if song is None:
            print("Playlist is empty")
        else:
            print("Shuffling and playing:", song)
    elif choice == 7:
        song = playlist.getCurrentSong()
        if song is None:
            print("Playlist is empty")
        else:
            print("Currently playing:", song)
    elif choice == 8:
        playlist.showPlaylist()
    elif choice == 0:
        print("Goodbye.")
        break