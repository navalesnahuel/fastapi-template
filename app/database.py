from sqlmodel import Session, create_engine, select

from app.auth.models import User, UserCreate
from app.auth.services import create_user
from app.config import settings

DATABASE_URL = str(settings.DATABASE_URL)

engine = create_engine(
    DATABASE_URL,
    pool_size=settings.DATABASE_POOL_SIZE,
    pool_recycle=settings.DATABASE_POOL_TTL,
    pool_pre_ping=settings.DATABASE_POOL_PRE_PING,
)


def init_db(session: Session) -> None:
    """Create the first superuser with credentials from env"""
    user = session.exec(
        select(User).where(User.email == settings.FIRST_SUPERUSER)
    ).first()
    if not user:
        user_in = UserCreate(
            email=settings.FIRST_SUPERUSER,
            password=settings.FIRST_SUPERUSER_PASSWORD,
            is_superuser=True,
        )
        user = create_user(session=session, user_create=user_in)
