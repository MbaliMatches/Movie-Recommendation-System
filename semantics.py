import spacy 

nlp = spacy.load("en_core_web_md")
planet_hulk = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator."

def movie_prediction(planet_hulk):
    with open ("movies.txt", "r") as file:  
        movies = file.readlines()
        
        # Tokenize the planet_hulk description
        planet_hulk_tokens = nlp(planet_hulk)
        
        max_similarity = -1  # Initialize the maximum similarity value
        most_similar_movie = None
        
        for movie in movies:
            movie = nlp(movie)
            similarity = planet_hulk_tokens.similarity(movie)
            
            if similarity > max_similarity:
                max_similarity = similarity
                most_similar_movie = movie
            
        return most_similar_movie.text  # Return the most similar movie description

most_similar_movie = movie_prediction(planet_hulk)
print("Most similar movie:", most_similar_movie)              