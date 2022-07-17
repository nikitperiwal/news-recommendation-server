import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from news_recommender import recommender, api_utils, constants

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


@app.get('/user/')
def get_user_recommendation(username: str):
    user_details = api_utils.get_user_details(username)
    return user_details


class User(BaseModel):
    username: str
    categories: list = constants.NEWS_CATEGORIES


@app.post('/user/')
def post_user_recommendation(user: User):
    api_utils.post_user_details(user)


@app.put('/user/')
def put_user_recommendation(user: User):
    api_utils.put_user_details(user)


@app.get('/news/user/')
def get_user_recommendation(username: str, num_articles: int = 15):
    articles = recommender.user_recommendations(username, num_articles)
    return {'news': articles}


@app.get('/news/category/')
def get_category_news(category: str, num_articles: int = 15):
    articles = recommender.category_news(category, num_articles)
    return {'news': articles}


@app.get('/news/search/')
def get_searched_news(search_str: str, num_articles: int = 15):
    articles = recommender.search_news(search_str, num_articles)
    return {'news': articles}


class LikeDislike(BaseModel):
    username: str
    news_id: str
    value: int


@app.post('/usage/like_dislike/')
def post_like_dislike(data: LikeDislike):
    api_utils.post_usage_data(
        user_id=data.username,
        news_id=data.news_id,
        value=data.value,
    )


if __name__ == "__main__":
    print("Starting the recommender API")
    # Run app with uvicorn with port and host specified. Host needed for docker port mapping.
    uvicorn.run(app, port=8000, host="127.0.0.1")
