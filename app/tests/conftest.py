import os
from unittest.mock import patch

patch.dict(
    os.environ,
    {
        "DATABASE_URL": "postgresql://test_user:test_password@localhost:5433/test_db",
        "FIRST_SUPERUSER": "test@test.com",
        "FIRST_SUPERUSER_PASSWORD": "testpassword",
    },
).start()  # Start patching immediately


import pytest
from sqlmodel import Session, SQLModel, create_engine

from ..database import init_db
from ..dependencies import get_session
from ..main import app

test_engine = create_engine(os.environ["DATABASE_URL"])


@pytest.fixture(scope="function", autouse=True)
def setup_test_db():
    """Set up and clean test database."""

    SQLModel.metadata.create_all(test_engine)
    with Session(test_engine) as session:
        init_db(
            session,
            os.environ["FIRST_SUPERUSER"],
            os.environ["FIRST_SUPERUSER_PASSWORD"],
        )
    yield
    SQLModel.metadata.drop_all(test_engine)  # Clean up after tests


def get_test_session():
    with Session(test_engine) as session:
        yield session


@pytest.fixture(scope="function")
def db_session():
    """Fixture to override session for each test."""
    with Session(test_engine) as session:
        yield session


# Override session dependency for testing
app.dependency_overrides[get_session] = get_test_session
