from fastapi import FastAPI, Body, HTTPException # Import core FastAPI classes and HTTP exception handling
from fastapi.responses import HTMLResponse

# Create FastAPI app instance
app = FastAPI()

# Sample movie data
movies = [
    {
        "id": 1,
        "title": "Inception",
        "overview": "A thief who steals corporate secrets through dream-sharing technology is given the inverse task of planting an idea.",
        "year": "2010",
        "rating": 8.8,
        "category": "Science Fiction"
    },
    {
        "id": 2,
        "title": "Coco",
        "overview": "A young boy who dreams of becoming a musician enters the Land of the Dead to find answers about his family history.",
        "year": "2017",
        "rating": 8.4,
        "category": "Animation"
    },
    {
        "id": 3,
        "title": "Parasite",
        "overview": "A poor family schemes to become employed by a wealthy family and infiltrate their household with unexpected consequences.",
        "year": "2019",
        "rating": 8.6,
        "category": "Drama"
    },
    {
        "id": 4,
        "title": "The Dark Knight",
        "overview": "Batman faces his most dangerous enemy yet, the Joker, while protecting Gotham from chaos and destruction.",
        "year": "2008",
        "rating": 9.0,
        "category": "Action"
    }
]

# Set the title of the FastAPI app 
app.title = "Getting started with FastAPI"

# Home route
@app.get('/', tags=['Home'])
def home(): 
    return "Hello, World!"

# Get all movies or filter by category
@app.get('/movies', tags=['Movies']) 
def get_movies(category: str = None):
    if category:
        return [movie for movie in movies if movie['category'].lower() == category.lower()]
    return movies

# Create a new movie
@app.post('/movies', tags=['Movies'])
def create_movie(
    id : int = Body(),
    title: str  = Body(), 
    overview: str  = Body(), 
    year: str  = Body(), 
    rating: float = Body(), 
    category: str = Body()
    ): 
    for movie in movies:
        if movie['id'] == id:
            raise HTTPException(status_code=400, detail="Movie with this ID already exists.")
        
    new_movie = {
        'id': id, 
        'title': title, 
        'overview': overview, 
        'year': year, 
        'rating': rating, 
        'category': category
    }
    movies.append(new_movie)
    return new_movie

# Update an existing movie by ID
@app.put('/movies/{id}', tags=['Movies'])
def update_movies(
    id: int,
    title: str = Body(), 
    overview: str = Body(), 
    year: str  = Body(), 
    rating: float = Body(), 
    category: str = Body()
    ):
    for movie in movies:
        if movie['id'] == id: 
            movie['title'] = title
            movie['overview'] = overview
            movie['year'] = year
            movie['rating'] = rating
            movie['category'] = category
            return movies
        
    raise HTTPException(status_code=404, detail="Movie not found")

# Delete a movie by ID
@app.delete('/movies/{id}', tags=['Movies'])
def delete_movie(id: int):
    for movie in movies:
        if movie['id'] == id: 
            movies.remove(movie)
            return movie
        
    raise HTTPException(status_code=404, detail="Movie not found")
