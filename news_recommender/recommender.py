import re
from datetime import datetime
from bson.objectid import ObjectId
from news_recommender import mongo_utils, constants, api_utils


def fix_articles(news_articles: list):
    from_format = "%Y-%m-%dT%H:%M:%SZ"
    to_format = "%H:%M %p on %d %b %Y"

    for article in news_articles:
        article["_id"] = str(article["_id"])
        article["datetime"] = datetime.strptime(article["datetime"], from_format).strftime(to_format)
        del article["content"]
    return news_articles


def record_recommendations(username: str, news_articles: list):
    data = list()
    for article in news_articles:
        data.append({
            "username": username,
            "news_id": article["_id"],
        })
    mongo_utils.persist_to_mongo(data, collection_name="recommendations", db_name="usage_db")


def user_recommendations(username: str, num_articles: int):
    category = api_utils.get_user_details(username)["category"]
    prev_news_ids = api_utils.get_prev_recommendations(username)

    query = {"$and": [{"category": {"$in": category}}, {"_id": {"$nin": prev_news_ids}}]}
    news_articles = mongo_utils.read_from_mongo(
        collection_name=constants.PROCESSED_TABLE,
        query=query
    )
    news_articles.sort("datetime", -1).limit(num_articles)
    news_articles = list(news_articles)

    if len(news_articles) > 0 and constants.TEST_MODE != "true":
        record_recommendations(username, news_articles)

    return fix_articles(news_articles)


def search_news(search_str: str, num_articles: int):
    regx = re.compile(f"{search_str}", re.IGNORECASE)
    query = {"$or": [{"title": regx}, {"abstract": regx}]}

    news_articles = mongo_utils.read_from_mongo(
        collection_name=constants.PROCESSED_TABLE,
        query=query
    )
    news_articles.sort("datetime", -1).limit(num_articles)
    news_articles = fix_articles(list(news_articles))
    return news_articles


def category_news(category: str, num_articles: int):
    query = {"category": category}
    news_articles = mongo_utils.read_from_mongo(
        collection_name=constants.PROCESSED_TABLE,
        query=query
    )
    news_articles.sort("datetime", -1).limit(num_articles)
    news_articles = fix_articles(list(news_articles))
    return news_articles
