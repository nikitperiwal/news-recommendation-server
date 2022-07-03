import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import recommender

# Initiate app instance
app = FastAPI(title='Recommender',
              version='1.0',
              description='News Recommender for Users of Short.ly')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/news/user/')
def get_user_recommendation(user_id: str, last_request_id: str = "", num_articles: int = 15):
    articles = [user_id, last_request_id, num_articles]
    return {'news': articles}


@app.get('/news/category/')
def get_category_news(category: str, num_articles: int = 15):
    articles = recommender.category_news(category, num_articles)
    return {'news': articles}


@app.get('/news/search/')
def get_searched_news(search_str: str, num_articles: int = 15):
    articles = recommender.search_news(search_str, num_articles)
    return {'news': articles}


@app.post('/usage/like_dislike/')
def post_like_dislike():
    pass


if __name__ == "__main__":
    print("Starting the recommender API")
    # Run app with uvicorn with port and host specified. Host needed for docker port mapping.
    uvicorn.run(app, port=8000, host="127.0.0.1")
