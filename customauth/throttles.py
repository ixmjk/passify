from rest_framework.throttling import AnonRateThrottle as BaseAnonRateThrottle
from rest_framework.throttling import UserRateThrottle as BaseUserRateThrottle


class UserRateThrottle(BaseUserRateThrottle):
    rate = "5/minute"


class AnonRateThrottle(BaseAnonRateThrottle):
    rate = "5/minute"
