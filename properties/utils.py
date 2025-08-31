from django.core.cache import cache
from .models import Property
from django_redis import get_redis_connection

def get_all_properties():
    properties = cache.get('all_properties')
    if not properties:
        properties = list(Property.objects.all().values())
        cache.set('all_properties', properties, 3600)  # Cache for 1 hour
    return properties


def get_redis_cache_metrics():
    conn = get_redis_connection("default")
    info = conn.info("stats")
    hits = info.get("keyspace_hits", 0)
    misses = info.get("keyspace_misses", 0)
    ratio = hits / (hits + misses) if (hits + misses) > 0 else 0
    return {
        "hits": hits,
        "misses": misses,
        "hit_ratio": ratio,
    }

import logging
from django_redis import get_redis_connection

logger = logging.getLogger(__name__)

def get_redis_cache_metrics():
    redis_conn = get_redis_connection("default")
    info = redis_conn.info("stats")
    hits = info.get("keyspace_hits", 0)
    misses = info.get("keyspace_misses", 0)
    total_requests = hits + misses
    hit_ratio = hits / total_requests if total_requests > 0 else 0

    logger.error(f"Redis Cache Metrics: hits={hits}, misses={misses}, hit_ratio={hit_ratio:.2f}")
    return {
        "hits": hits,
        "misses": misses,
        "hit_ratio": hit_ratio,
    }
