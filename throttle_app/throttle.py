from rest_framework.throttling import SimpleRateThrottle

class CustomAnonRateThrottle(SimpleRateThrottle):
    scope = 'anon'

    def throttle_failure(self):
        return {
            "error": "Too many requests. Please try again in a few seconds."
        }

class CustomUserRateThrottle(SimpleRateThrottle):
    scope = 'user'

    def throttle_failure(self):
        return {
            "error": "You have exceeded your request limit. Please wait before trying again."
        }
