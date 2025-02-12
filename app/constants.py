from enum import Enum


class Environment(str, Enum):
    DEVELOPMENT = "DEVELOPMENT"
    PRODUCTION = "PRODUCTION"

    @property
    def is_debug(self):
        return self in (self.DEVELOPMENT)

    @property
    def is_deployed(self) -> bool:
        return self in (self.PRODUCTION)
