from rest_framework.throttling import SimpleRateThrottle

class CustomAnonRateThrottle(SimpleRateThrottle):
    scope = 'anon'

    def get_cache_key(self, request, view):
        # Use the client's IP address as the cache key
        return self.cache_format % {
            'scope': self.scope,
            'ident': self.get_ident(request),
        }

    def throttle_failure(self):
        wait_time = self.wait()
        return {
            "error": f"Too many requests from this IP. Please try again in {wait_time:.0f} seconds."
        }


class CustomUserRateThrottle(SimpleRateThrottle):
    scope = 'user'

    def get_cache_key(self, request, view):
        # Use the authenticated user's ID as the cache key
        if request.user and request.user.is_authenticated:
            return self.cache_format % {
                'scope': self.scope,
                'ident': request.user.pk,
            }
        return None

    def throttle_failure(self):
        wait_time = self.wait()
        return {
            "error": f"You have exceeded your request limit. Please wait {wait_time:.0f} seconds before retrying."
        }
