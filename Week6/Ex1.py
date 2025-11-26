from collections import defaultdict

songs = []
genre_count = defaultdict(int)

def data_entry(n):
    for i in range(n):
        song_name = input("Enter song name: ")
        genre = input("Enter genre: ")
        songs.append((song_name, genre))
        genre_count[genre] += 1

def display_results():
    print("Welcome to Music Library Manager!\n\n")
    print("=== YOUR MUSIC LIBRARY ===")
    for tup in songs:
        print(f"{songs.index(tup)+1}. {tup[0]}({tup[1]})")
    print("\n")
    print("=== GENRE STATISTICS ===")
    most_popular_genre = list(genre_count.keys())[0]
    c = genre_count[most_popular_genre]
    for genre, count in genre_count.items():
        print(f"{genre}: {count} song(s)")
        if count > c:
            most_popular_genre = genre
            c = count
    print(f"\nMost popular genre: {most_popular_genre}")

data_entry(5)
display_results()
