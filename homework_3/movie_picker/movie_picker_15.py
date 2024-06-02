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

my_genre = input("Search by Genre: ")
GENRES.keys()
if my_genre == 'y':
    print("Available Genres: ", list(GENRES.keys()))
elif my_genre == 'n':
    print(my_genre)
else:
    print("Give correct answer")

found_movies = list()
pick_genre = input("Enter genre: ")

if pick_genre in GENRES:
    for movie in GENRES[pick_genre]:
        found_movies.append(movie)

print("Available Movies:", found_movies)

picked_movie = input("Enter movie: ")
if picked_movie in found_movies:
    print("Movie to watch: ", picked_movie, ". Genre: ", pick_genre)

# Ask user if they want to see the list of available actors
show_actors = input("Do you want to see the list of available actors? (y/n): ").strip().lower()
if show_actors == 'y':
    print("Available Actors: ", list(ACTORS.keys()))
elif show_actors == 'n':
    print("You chose not to see the list of actors.")
else:
    print("Please provide a correct answer (y/n).")

# Initialize an empty list to store found movies
found_movies = list()

# Ask user to pick an actor
pick_actor = input("Enter actor: ").strip()

# Check if the entered actor is in ACTORS
if pick_actor in ACTORS:
    for movie in ACTORS[pick_actor]:
        found_movies.append(movie)
    print("Movies available for the actor '{}': {}".format(pick_actor, found_movies))
else:
    print("Actor not found in the database.")

# Ask user to pick a movie from the found movies
if found_movies:
    picked_movie = input("Enter movie: ").strip()
    if picked_movie in found_movies:
        # Find the genre of the picked movie
        movie_genre = None
        for genre, movies in GENRES.items():
            if picked_movie in movies:
                movie_genre = genre
                break
        print("Movie to watch: '{}'. Starring '{}'".format(picked_movie, pick_actor))
    else:
        print("The movie is not in the list of movies for the actor.")
else:
    print("No movies found for the actor.")
