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

# ACTORS = {
#     'Robert De Niro': ['Meet the Parents'],
#     'Ben Stiller': ['Meet the Parents'],
#     'Adam Sandler': ['Anger Management'],
#     'Jack Nicholson': ['Anger Management'],
#     'Brendan Fraser': ['Mummy'],
#     'Rachel Weisz': ['Mummy'],
#     'Tom Cruise': ['Vanilla Sky', 'Mission Impossible'],
#     'Penelope Cruz': ['Vanilla Sky'],
#     'Cameron Diaz': ['Vanilla Sky'],
#     'Brad Pitt': ['Meet Joe Black'],
#     'Anthony Hopkins': ['Meet Joe Black'],
#     'Jeremy Renner': ['Mission Impossible']
# }


CAST = {
    'Meet the Parents': ['Robert De Niro', 'Ben Stiller'],
    'Anger Management': ['Adam Sandler', 'Jack Nicholson'],
    'Mummy': ['Brendan Fraser', 'Rachel Weisz'],
    'Vanilla Sky': ['Tom Cruise', 'Penelope Cruz', 'Cameron Diaz'],
    'Meet Joe Black': ['Brad Pitt', 'Anthony Hopkins'],
    'Mission Impossible': ['Tom Cruise', 'Jeremy Renner']
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
        found_actors = list()
        for cast in CAST.values():
            for actor in cast:
                if actor not in found_actors:
                    found_actors.append(actor)
        print("Available Actors: ", found_actors)
        pick_actor = input("Enter actor: ").strip()
        available_movies = list()
        if pick_actor in found_actors:
            for movie, cast in CAST.items():
                for actor in cast:
                    if actor == pick_actor:
                        available_movies.append(movie)
        print("Movies available for the actor '{}': {}".format(pick_actor, available_movies))
        picked_movie = input("Enter movie: ").strip()
        if picked_movie in available_movies:
            print("Movie to watch: ", picked_movie, " Starring: ", pick_actor)
        else:
            print("No such movie in the list")
    else:
        print("Actor not found in the database.")












# if __name__ == '__main__':
#     print('Task 16. Movie picker Version 2.')
#     GENRES = {
#         'comedy': ['Meet the Parents', 'Anger Management'],
#         'adventures': ['Mummy'],
#         'romantic': ['Vanilla Sky', 'Meet Joe Black'],
#         'drama': ['Meet Joe Black'],
#         'thriller': ['Vanilla Sky'],
#         'action': ['Mission Impossible']
#     }
#
#     CAST = {
#         'Meet the Parents': ['Robert De Niro', 'Ben Stiller'],
#         'Anger Management': ['Adam Sandler', 'Jack Nicholson'],
#         'Mummy': ['Brendan Fraser', 'Rachel Weisz'],
#         'Vanilla Sky': ['Tom Cruise', 'Penelope Cruz', 'Cameron Diaz'],
#         'Meet Joe Black': ['Brad Pitt', 'Anthony Hopkins'],
#         'Mission Impossible': ['Tom Cruise', 'Jeremy Renner']
#     }
#
#     genre_search = input("Search by Genre: ")
#     if genre_search == "y":
#         print(f"Available Genres: {list(GENRES.keys())}")
#         genre = input("Enter genre: ")
#         if genre in GENRES.keys():
#             print(f"Available Movies: {GENRES[genre]}")
#             movie = input("Enter movie: ")
#             if movie in GENRES[genre]:
#                 print(f"Movie to watch: {movie}. Genre: {genre}")
#             else:
#                 print("Movie not found. Exiting")
#         else:
#             print("Genre not found. Exiting")
#     elif genre_search == "n":
#         actor_search = input("Search by Actor: ")
#         if actor_search == "y":
#             actors = list()
#             for cast in CAST.values():
#                 for actor in cast:
#                     actors.append(actor)
#             actors = list(set(actors))
#             print(f"Available Actors: {actors}")
#             chosen_actor = input(" Enter actor: ")
#             if chosen_actor in actors:
#                 movies = list()
#                 for movie, cast in CAST.items():
#                     if chosen_actor in cast:
#                         movies.append(movie)
#                 print(f"Available Movies: {movies} with {chosen_actor}")
#                 movie = input("Enter movie: ")
#                 if movie in movies:
#                     print(f"Movie to watch: {movie}. Starring: {chosen_actor}")
#                 else:
#                     print("Movie not found. Exiting")
#             else:
#                 print("Actor not found. Exiting")
#         else:
#             print("Input not supported. Exiting")
#     else:
#         print("Input not supported. Exiting")