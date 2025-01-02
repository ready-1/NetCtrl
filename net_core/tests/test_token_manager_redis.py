from django.test import TestCase
from django.core.cache import cache
from net_core.api_helpers.token_manager import TokenManager

class RedisTokenManagerTests(TestCase):
    
    def setUp(self):
        self.switch_ip = "192.168.1.1"
        self.token = "test_token"

    def test_token_caching_with_ttl(self):
        """Test that a token is cached with a TTL."""
        cache_key = f"switch_token_{self.switch_ip}"
        cache.set(cache_key, self.token, timeout=30)  # Cache with 30 seconds TTL
        cached_token = cache.get(cache_key)
        self.assertEqual(cached_token, self.token)

        ttl = cache.ttl(cache_key)  # Check the TTL
        self.assertGreater(ttl, 0)

    def test_token_expiry_check(self):
        """Test checking the token expiry."""
        cache_key = f"switch_token_{self.switch_ip}"
        cache.set(cache_key, self.token, timeout=30)  # Cache with 30 seconds TTL

        ttl = TokenManager.get_token_expiry(self.switch_ip)
        self.assertGreater(ttl, 0)