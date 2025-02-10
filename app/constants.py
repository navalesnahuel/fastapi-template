from enum import Enum


class Environment(str, Enum):
    DEVELOPMENT = "DEVELOPMENT"
    PRODUCTION = "PRODUCTION"
    TESTING = "TESTING"

    @property
    def is_debug(self):
        return self in (self.DEVELOPMENT, self.TESTING)

    @property
    def is_deployed(self) -> bool:
        return self in (self.PRODUCTION)
