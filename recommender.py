"""
1. Table that contains user_id, news_id, like/dislike data.
2. Table containing request data for users.
3. Table with user_data, category etc.
"""
import mongo_utils
import constants
import re


def get_recommendations(
        user_id: str,
        last_request_id: str,
        num_articles: int,
        categories: str,
        search_query: str):
    pass


def search_news(search_str: str, num_articles: int):
    regx = re.compile(f"{search_str}", re.IGNORECASE)
    query = {"$or": [{"title": regx}, {"abstract": regx}]}

    news_articles = mongo_utils.read_from_mongo(
        collection_name=constants.PROCESSED_TABLE,
        query=query
    )
    news_articles.sort("datetime", -1).limit(num_articles)
    return list(news_articles)


def category_news(category: str, num_articles: int):
    query = {"category": category}
    news_articles = mongo_utils.read_from_mongo(
        collection_name=constants.PROCESSED_TABLE,
        query=query
    )
    news_articles.sort("datetime", -1).limit(num_articles)
    return list(news_articles)

