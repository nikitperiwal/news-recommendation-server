import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from news_recommender import recommender

# Initiate app instance
app = FastAPI(title='Recommender',
              version='1.0',
              description='News Recommender for Users of Short.ly')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)


# TODO
# 1. Endpoint to clear rec data
# 2. Figure out POST for list data
# 3. POST user category

@app.get('/user/category/')
def get_user_recommendation(user_id: str):
    category = recommender.get_user_categories(user_id)
    return {'category': category}


@app.get('/news/user/')
def get_user_recommendation(user_id: str, last_request_id: str = "", num_articles: int = 15):
    articles = recommender.user_recommendations(user_id, last_request_id, num_articles)
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
