import os
from dotenv import load_dotenv

load_dotenv()

import redis

redisClient = redis.Redis(host=os.environ.get("REDIS_HOST"), port=os.environ.get("REDIS_PORT"), db=0,
                     password=os.environ.get('REDIS_PASSWORD'))

