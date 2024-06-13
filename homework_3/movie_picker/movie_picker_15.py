if __name__ == '__main__':
    print('Task 15. Movie picker Version 1.')
GENRES = {
    'comedy': ['Meet the Parents', 'Anger Management'],
    'adventures': ['Mummy'],
    'romantic': ['Vanilla Sky', 'Meet Joe Black'],
    'drama': ['Meet Joe Black'],
    'thriller': ['Vanilla Sky'],
    'action': ['Mission Impossible']
}

ACTORS = {
    'Robert De Niro': ['Meet the Parents'],
    'Ben Stiller': ['Meet the Parents'],
    'Adam Sandler': ['Anger Management'],
    'Jack Nicholson': ['Anger Management'],
    'Brendan Fraser': ['Mummy'],
    'Rachel Weisz': ['Mummy'],
    'Tom Cruise': ['Vanilla Sky', 'Mission Impossible'],
    'Penelope Cruz': ['Vanilla Sky'],
    'Cameron Diaz': ['Vanilla Sky'],
    'Brad Pitt': ['Meet Joe Black'],
    'Anthony Hopkins': ['Meet Joe Black'],
    'Jeremy Renner': ['Mission Impossible']
}

ask_search_by_genre = input("Search by Genre: ")
while ask_search_by_genre not in ["y", "n"]:
    ask_search_by_genre = input("Search by Genre: ")

found_movies = list()

if ask_search_by_genre == 'y':
    print("Available Genres: ", list(GENRES.keys()))
    pick_genre = input("Enter genre: ")
    if pick_genre in GENRES:
        for movie in GENRES[pick_genre]:
            found_movies.append(movie)
    print("Available Movies:", found_movies)
    picked_movie = input("Enter movie: ")
    if picked_movie in found_movies:
        print("Movie to watch: ", picked_movie, ". Genre: ", pick_genre)
    else:
        print("No such movie in the list")

elif ask_search_by_genre == 'n':
    ask_search_by_actor = input("Search by Actor: ").strip()
    while ask_search_by_actor not in ["y", "n"]:
        ask_search_by_actor = input("Search by Actor: ")
    if ask_search_by_actor == 'y':
        print("Available Actors: ", list(ACTORS.keys()))
    elif ask_search_by_actor == 'n':
        print("You chose not to see the list of actors.")
    else:
        print("Please provide a correct answer (y/n).")
    pick_actor = input("Enter actor: ").strip()
    if pick_actor in ACTORS:
        for movie in ACTORS[pick_actor]:
            found_movies.append(movie)
        print("Movies available for the actor '{}': {}".format(pick_actor, found_movies))
        picked_movie = input("Enter movie: ").strip()
        if picked_movie in found_movies:
            print("Movie to watch: ", picked_movie, " Starring: ", pick_actor)
        else:
            print("No such movie in the list")
    else:
        print("Actor not found in the database.")
