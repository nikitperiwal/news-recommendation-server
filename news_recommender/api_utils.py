from bson.objectid import ObjectId
from news_recommender import mongo_utils


def get_user_details(username: str):
    query = {"username": username}
    columns = {"_id": 0, "username": 1, "category": 1}

    cursor = mongo_utils.read_from_mongo(
        collection_name="users",
        query=query,
        columns=columns,
        db_name="user_db"
    )
    user = cursor.next()
    return user


def post_user_details(user):
    data = [{
        "username": user.username,
        "category": user.category,
    }]
    mongo_utils.persist_to_mongo(
        data,
        collection_name="users",
        db_name="user_db"
    )


def put_user_details(user):
    user = {
        "username": user.username,
        "category": user.category,
    }
    query = {"username": user["username"]}

    mongo_utils.replace_in_collection(
        data=user,
        query=query,
        collection_name="users",
        db_name="user_db"
    )


def get_prev_recommendations(username: str):
    query = {"username": username}
    columns = {"_id": 0, "news_id": 1}

    cursor = mongo_utils.read_from_mongo(
        collection_name="recommendations",
        db_name="usage_db",
        query=query,
        columns=columns
    )
    news_ids = list()
    for data in cursor:
        news_ids.append(data["news_id"])
    return news_ids


def post_usage_data(username: str, news_id: str, value: int):
    data = [{
        "username": username,
        "news_id": ObjectId(news_id),
        "value": value,
    }]
    mongo_utils.persist_to_mongo(data, collection_name="like_dislike", db_name="usage_db")
