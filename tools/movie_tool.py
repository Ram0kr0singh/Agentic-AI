from __future__ import annotations

import difflib
import re
from typing import Any

_MOVIES = [
    {
        "title": "Inception",
        "year": "2010",
        "genre": "Action, Adventure, Sci-Fi",
        "director": "Christopher Nolan",
        "cast": "Leonardo DiCaprio, Joseph Gordon-Levitt, Ellen Page",
        "plot": "A skilled thief uses dream-sharing technology to perform corporate espionage and must plant an idea into a target's subconscious.",
        "rating": "8.8/10",
    },
    {
        "title": "The Dark Knight",
        "year": "2008",
        "genre": "Action, Crime, Drama",
        "director": "Christopher Nolan",
        "cast": "Christian Bale, Heath Ledger, Aaron Eckhart",
        "plot": "Batman faces the psychopathic Joker while trying to protect Gotham City from chaos.",
        "rating": "9.0/10",
    },
    {
        "title": "Interstellar",
        "year": "2014",
        "genre": "Adventure, Drama, Sci-Fi",
        "director": "Christopher Nolan",
        "cast": "Matthew McConaughey, Anne Hathaway, Jessica Chastain",
        "plot": "A team of explorers travels through a wormhole in space to ensure humanity's survival.",
        "rating": "8.6/10",
    },
    {
        "title": "The Matrix",
        "year": "1999",
        "genre": "Action, Sci-Fi",
        "director": "Lana Wachowski, Lilly Wachowski",
        "cast": "Keanu Reeves, Laurence Fishburne, Carrie-Anne Moss",
        "plot": "A hacker discovers reality is a simulated world and joins a rebellion against the machines.",
        "rating": "8.7/10",
    },
    {
        "title": "The Shawshank Redemption",
        "year": "1994",
        "genre": "Drama",
        "director": "Frank Darabont",
        "cast": "Tim Robbins, Morgan Freeman, Bob Gunton",
        "plot": "Two imprisoned men form a friendship and find hope while navigating life in prison.",
        "rating": "9.3/10",
    },
    {
        "title": "Pulp Fiction",
        "year": "1994",
        "genre": "Crime, Drama",
        "director": "Quentin Tarantino",
        "cast": "John Travolta, Uma Thurman, Samuel L. Jackson",
        "plot": "The lives of several criminals intertwine in a series of violent and darkly comedic events.",
        "rating": "8.9/10",
    },
    {
        "title": "Titanic",
        "year": "1997",
        "genre": "Drama, Romance",
        "director": "James Cameron",
        "cast": "Leonardo DiCaprio, Kate Winslet, Billy Zane",
        "plot": "A young couple falls in love aboard the ill-fated RMS Titanic.",
        "rating": "7.8/10",
    },
    {
        "title": "Fight Club",
        "year": "1999",
        "genre": "Drama",
        "director": "David Fincher",
        "cast": "Brad Pitt, Edward Norton, Helena Bonham Carter",
        "plot": "An office worker and a soap maker start an underground fight club that becomes something much more dangerous.",
        "rating": "8.8/10",
    },
    {
        "title": "Forrest Gump",
        "year": "1994",
        "genre": "Drama, Romance",
        "director": "Robert Zemeckis",
        "cast": "Tom Hanks, Robin Wright, Gary Sinise",
        "plot": "The life of Forrest Gump unfolds through historic events as he pursues love and personal destiny.",
        "rating": "8.8/10",
    },
    {
        "title": "The Godfather",
        "year": "1972",
        "genre": "Crime, Drama",
        "director": "Francis Ford Coppola",
        "cast": "Marlon Brando, Al Pacino, James Caan",
        "plot": "The powerful Corleone crime family struggles with leadership, betrayal, and loyalty.",
        "rating": "9.2/10",
    },
]


def _normalize(text: str) -> str:
    return re.sub(r"[^a-z0-9 ]+", "", text.strip().lower())


def _movie_score(movie: dict[str, str], query: str) -> int:
    query = _normalize(query)
    score = 0

    if query in _normalize(movie["title"]):
        score += 10

    if any(token in _normalize(movie["genre"]) for token in query.split()):
        score += 3

    if any(token in _normalize(movie["plot"]) for token in query.split()):
        score += 2

    if any(token in _normalize(movie["director"]) for token in query.split()):
        score += 2

    if any(token in _normalize(movie["cast"]) for token in query.split()):
        score += 2

    return score


def search_movies(query: str, limit: int = 5) -> list[dict[str, str]]:
    if not query or not query.strip():
        raise ValueError("Missing query for movie search.")

    query_norm = _normalize(query)
    matches = []

    for movie in _MOVIES:
        score = _movie_score(movie, query_norm)
        if score > 0:
            matches.append((score, movie))

    if not matches:
        title_matches = difflib.get_close_matches(query.strip(), [movie["title"] for movie in _MOVIES], n=limit, cutoff=0.4)
        if title_matches:
            matches = [(10, movie) for movie in _MOVIES if movie["title"] in title_matches]

    sorted_matches = [movie for _, movie in sorted(matches, key=lambda item: item[0], reverse=True)]
    return sorted_matches[:max(1, min(limit, len(sorted_matches)))]


def format_movie_result(movie: dict[str, str]) -> str:
    return (
        f"Title: {movie['title']}\n"
        f"Year: {movie['year']}\n"
        f"Genre: {movie['genre']}\n"
        f"Director: {movie['director']}\n"
        f"Cast: {movie['cast']}\n"
        f"Rating: {movie['rating']}\n"
        f"Plot: {movie['plot']}"
    )


def execute(arguments: dict[str, Any]) -> str:
    query = (arguments.get("query") or "").strip()
    limit = arguments.get("limit")

    try:
        limit = int(limit)
    except (TypeError, ValueError):
        limit = 5

    movies = search_movies(query, limit=limit)

    if not movies:
        return f"No matching movies found for query: {query}"

    header = f"Movie search results for: {query}\n\n"
    results = "\n\n".join(format_movie_result(movie) for movie in movies)
    return header + results
