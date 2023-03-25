films = ['Spider-man: No way to home',
        'Crazy Stupid Love.',
        'Die Hard',
        'Dead Poets Society',
        'Home Alone',
        'Seven',
        'Memento',
        'Harry Potter and the Prisoner of Azkaban'
        "One Flew Over the Cuckoo's Nest"
        ]
def filter_movies_by_length(movies):
    filtered_movies = []
    for movie in movies:
        if len(movie) > 8:
            filtered_movies.append(movie)
    return filtered_movies
print(filter_movies_by_length(films))