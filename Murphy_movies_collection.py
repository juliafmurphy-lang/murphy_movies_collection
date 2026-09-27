""""""""""""""""
Julie Murphy- Base level
#Test run: display pre-loaded collection
Your Movie Collection
---------------------
Thor Ragnorak             2017 Action / Adventure   7.90
The Count of Monte Cristo 2002 Drama / Adventure    7.70
Gladiator                 2000 Action / Drama       8.50
Legally Blonde            2001 Comedy / Romance     6.50
The Hobbit                2012 Fantasy / Adventure  7.80

Add 2 new movies to your collection:

#Test run: add movie with two genres entered as "Action, Comedy"
#Test run: sort and display by year
#Test run: find_top_rated
#Test run: get_average_rating

Add 2 new movies to your collection:

~~~~~ Movie 1 ~~~~~
Enter the title of movie: Spiderman
Enter the release year of movie: 2026
Enter the genres of movie (comma-separated): Action, Comedy
Enter the rating of movie (0-10): 9

~~~~~ Movie 2 ~~~~~
Enter the title of movie: Love Hypothesis
Enter the release year of movie: 2026
Enter the genres of movie (comma-separated): Romance, Comedy
Enter the rating of movie (0-10): 10

Updated Movie Collection (Sorted by Year)
-----------------------------------------
Gladiator                 2000 Action / Drama       8.50
Legally Blonde            2001 Comedy / Romance     6.50
The Count of Monte Cristo 2002 Drama / Adventure    7.70
The Hobbit                2012 Fantasy / Adventure  7.80
Thor Ragnorak             2017 Action / Adventure   7.90
Spiderman                 2026 Action / Comedy      9.00
Love Hypothesis           2026 Romance / Comedy     10.00

Top 3 Rated Movies
------------------
Love Hypothesis           2026 Romance / Comedy     10.00
Spiderman                 2026 Action / Comedy      9.00
Gladiator                 2000 Action / Drama       8.50

Average Rating of All Movies: 8.2

"""""""""""""""
#Define starter data for the movie collection
movies = [
    {"title": "Thor Ragnorak", "year": 2017, "genres": ["Action", "Adventure"], "rating": 7.9},
    {"title": "The Count of Monte Cristo", "year": 2002, "genres": ["Drama", "Adventure"], "rating": 7.7},
    {"title": "Gladiator", "year": 2000, "genres": ["Action", "Drama"], "rating": 8.5},
    {"title": "Legally Blonde", "year": 2001, "genres": ["Comedy", "Romance"], "rating": 6.5},
    {"title": "The Hobbit", "year": 2012, "genres": ["Fantasy", "Adventure"], "rating": 7.8}
]

#Fuction 1 create_movie
def create_movie(title, year, genres, rating):
    movie = {
        "title": title,
        "year": year,
        "genres": genres,
        "rating": rating
    }
    return movie

#Fuction 2 display_movie
def display_movies(movies_list, heading):
    print(f"\n{heading}")
    print("-" * len(heading))
    if not movies_list:
            print("No movies in this collection.")
            return
    for movie in movies_list:
        joined_genres = ' / '.join(movie['genres'])
        print(f"{movie['title']:<25} {movie['year']:<4} {joined_genres:<20} {movie['rating']:.2f}")
    
#Find top rated movie
def find_top_rated(movies_list, n):
    sorted_movies = sorted(movies_list, key=lambda x: x['rating'], reverse=True)
    return sorted_movies[:n]    

#Get average movie rating
def get_average_rating(movies_list):
    if not movies_list:
        return 0
    total_rating = 0
    for movie in movies_list:
        total_rating += movie['rating']
    average_rating = total_rating / len(movies_list)
    return round(average_rating, 2)

#Ask user to add 2 new movies, update collection accordingly 
def main():
    display_movies(movies, "Your Movie Collection")

    print("\nAdd 2 new movies to your collection:")
    for i in range(1, 3):
        print(f"\n~~~~~ Movie {i} ~~~~~")
        title = input(f"Enter the title of movie: ")
        year = int(input(f"Enter the release year of movie: "))
        genres = input(f"Enter the genres of movie (comma-separated): ").split(',')
        genres = [genre.strip() for genre in genres]
        rating = float(input(f"Enter the rating of movie (0-10): "))
        new_movie = create_movie(title, year, genres, rating)
        movies.append(new_movie)

    movies.sort(key=lambda m: m['year'])
    display_movies(movies, "Updated Movie Collection (Sorted by Year)")

    top_rated_movies = find_top_rated(movies, 3)
    display_movies(top_rated_movies, "Top 3 Rated Movies")  

    average_rating = get_average_rating(movies)
    print(f"\nAverage Rating of All Movies: {average_rating}")

if __name__ == "__main__":
    main()
