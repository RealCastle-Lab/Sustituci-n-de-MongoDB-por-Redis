from redis_integration.config import get_redis_connection

r = get_redis_connection()

def get_db():
    return r
