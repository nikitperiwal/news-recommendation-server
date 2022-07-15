from bson.objectid import ObjectId
from news_recommender import mongo_utils


def get_user_details(user_id: str):
    query = {"_id": ObjectId(user_id)}
    columns = {"_id": 0, "category": 1}

    cursor = mongo_utils.read_from_mongo(
        collection_name="users",
        query=query,
        columns=columns,
        db_name="user_db"
    )
    user = cursor.next()
    return user


def post_user_details(user_details):
    mongo_utils.persist_to_mongo(
        user_details,
        collection_name="users",
        db_name="user_db"
    )


def put_user_details(user_details):
    mongo_utils.remove_from_collection(
        [user_details["user_id"]],
        collection_name="users",
        db_name="user_db"
    )

    mongo_utils.persist_to_mongo(
        user_details,
        collection_name="users",
        db_name="user_db"
    )


def get_prev_recommendations(user_id: str):
    query = {"user_id": ObjectId(user_id)}
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


def post_usage_data(usage_data: list):
    mongo_utils.persist_to_mongo(usage_data, collection_name="like_dislike", db_name="usage_db")
