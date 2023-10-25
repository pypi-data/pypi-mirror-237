from pg_common import SingletonBase
from pg_redis.define import *
from pg_environment import config
from redis import asyncio as aioredis


__all__ = ("RedisManager", )


class _RedisManager(SingletonBase):
    def __init__(self):
        self._pool_cfg = {}
        self._redis_client = {}
        _cfg_redis = config.get_conf(KEY_REDIS)
        for _k, _v in _cfg_redis.items():
            self._pool_cfg[_k] = aioredis.ConnectionPool(host=_v[KEY_REDIS_HOST], port=_v[KEY_REDIS_PORT],
                                                         db=_v[KEY_REDIS_DB], password=_v[KEY_REDIS_PASSWORD],
                                                         decode_responses=True, max_connections=_v[KEY_REDIS_POOL_SIZE])
            self._redis_client[_k] = aioredis.StrictRedis(connection_pool=self._pool_cfg[_k])

    def get_redis(self, svr_name="default"):
        return self._redis_client[svr_name]


RedisManager = _RedisManager()
