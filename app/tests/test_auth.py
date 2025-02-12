import os

from fastapi.testclient import TestClient

from ..config import settings
from ..main import app

client = TestClient(app)


def test_create_user():
    print("Current ENVIRONMENT:", os.getenv("ENVIRONMENT"))  # Debugging line
    payload = {
        "email": "test1@test.com",
        "password": "testpassword",
        "full_name": "test test",
    }
    response = client.post("/users/signup", json=payload)
    assert response.status_code == 200
    user_data = response.json()
    assert "id" in user_data
    assert user_data["is_active"] is True
    assert user_data["email"] == payload["email"]
    assert user_data["full_name"] == payload["full_name"]
    assert "password" not in user_data


def test_login_access_token():
    response = client.post(
        "/login/access-token",
        data={
            "grant_type": "password",
            "username": "test@test.com",
            "password": "testpassword",
        },
    )
    assert response.status_code == 200
    token_data = response.json()
    assert "access_token" in token_data
    assert token_data["token_type"] == "bearer"
    assert len(token_data["access_token"]) > 0

    check = client.post(
        "/login/test-token",
        headers={"Authorization": f"Bearer {token_data['access_token']}"},
    )

    assert check.status_code == 200


#

# @router.post("/signup", response_model=UserPublic)
# def register_user(session: SessionDep, user_in: UserRegister):
#     """
#     Create new user without the need to be logged in.
#     """
#     user = get_user_by_email(session=session, email=user_in.email)
#     if user:
#         raise HTTPException(
#             status_code=400,
#             detail="The user with this email already exists in the system",
#         )
#     user_create = UserCreate.model_validate(user_in)
#     user = create_user(session=session, user_create=user_create)
#     return user

# @router.post("/login/access-token")
# def login_access_token(
#     session: SessionDep,
#     form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
# ) -> Token:
#     """
#     OAuth2 compatible token login, get an access token for future requests
#     """
#     user = authenticate(
#         session=session, email=form_data.username, password=form_data.password
#     )
#     if not user:
#         raise HTTPException(status_code=400, detail="Incorrect email or password")
#     elif not user.is_active:
#         raise HTTPException(status_code=400, detail="Inactive user")
#     access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
#     return Token(
#         access_token=create_access_token(user.id, expires_delta=access_token_expires)
#     )
#

#
# @router.post("/login/test-token", response_model=UserPublic)
# def test_token(current_user: CurrentUser) -> Any:
#     """
#     Test access token
#     """
#     return current_user

#
# router = APIRouter(prefix="/users", tags=["users"])
#
#
# @router.get(
#     "/",
#     dependencies=[Depends(current_superuser)],
#     response_model=UsersPublic,
# )
# def read_users(
#     session: SessionDep,
#     skip: int = 0,
#     limit: int = 100,
# ):
#     """
#     Retrieve users.
#     """
#
#     count_statement = select(func.count()).select_from(User)
#     count = session.exec(count_statement).one()
#
#     statement = select(User).offset(skip).limit(limit)
#     users = session.exec(statement).all()
#
#     return UsersPublic(data=users, count=count)  # type: ignore
#
#
# @router.post("/", dependencies=[Depends(current_superuser)], response_model=UserPublic)
# def user_create(session: SessionDep, user_in: UserCreate):
#     """
#     Create new user.
#     """
#     user = get_user_by_email(session=session, email=user_in.email)
#     if user:
#         raise HTTPException(
#             status_code=400,
#             detail="The user with this email already exists in the system.",
#         )
#
#     user = create_user(session=session, user_create=user_in)
#     return user
#
#
# @router.patch("/me", response_model=UserPublic)
# def update_user_me(
#     session: SessionDep, user_in: UserUpdateMe, current_user: CurrentUser
# ):
#     """
#     Update own user.
#     """
#
#     if user_in.email:
#         existing_user = get_user_by_email(session=session, email=user_in.email)
#         if existing_user and existing_user.id != current_user.id:
#             raise HTTPException(
#                 status_code=409, detail="User with this email already exists"
#             )
#     user_data = user_in.model_dump(exclude_unset=True)
#     current_user.sqlmodel_update(user_data)
#     session.add(current_user)
#     session.commit()
#     session.refresh(current_user)
#     return current_user
#
#
# @router.get("/me", response_model=UserPublic)
# def read_user_me(current_user: CurrentUser):
#     """
#     Get current user.
#     """
#     return current_user
#
#
# @router.delete("/me", response_model=Message)
# def delete_user_me(session: SessionDep, current_user: CurrentUser):
#     """
#     Delete own user.
#     """
#     if current_user.is_superuser:
#         raise HTTPException(
#             status_code=403, detail="Super users are not allowed to delete themselves"
#         )
#     session.delete(current_user)
#     session.commit()
#     return Message(message="User deleted successfully")
#
#
# @router.post("/signup", response_model=UserPublic)
# def register_user(session: SessionDep, user_in: UserRegister):
#     """
#     Create new user without the need to be logged in.
#     """
#     user = get_user_by_email(session=session, email=user_in.email)
#     if user:
#         raise HTTPException(
#             status_code=400,
#             detail="The user with this email already exists in the system",
#         )
#     user_create = UserCreate.model_validate(user_in)
#     user = create_user(session=session, user_create=user_create)
#     return user
#
#
# @router.patch("/me/password", response_model=Message)
# def update_password_me(
#     session: SessionDep, body: UpdatePassword, current_user: CurrentUser
# ):
#     """
#     Update own password.
#     """
#     if not verify_password(body.current_password, current_user.hashed_password):
#         raise HTTPException(status_code=400, detail="Incorrect password")
#     if body.current_password == body.new_password:
#         raise HTTPException(
#             status_code=400, detail="New password cannot be the same as the current one"
#         )
#     hashed_password = get_password_hash(body.new_password)
#     current_user.hashed_password = hashed_password
#     session.add(current_user)
#     session.commit()
#     return Message(message="Password updated successfully")
#
#
# @router.get("/{user_id}", response_model=UserPublic)
# def read_user_by_id(user_id: UUID, session: SessionDep, current_user: CurrentUser):
#     """
#     Get a specific user by id.
#     """
#     user = session.get(User, user_id)
#     if user == current_user:
#         return user
#     if not current_user.is_superuser:
#         raise HTTPException(
#             status_code=403,
#             detail="The user doesn't have enough privileges",
#         )
#     return user
#
#
# @router.patch(
#     "/{user_id}",
#     dependencies=[Depends(current_superuser)],
#     response_model=UserPublic,
# )
# def user_update(
#     session: SessionDep,
#     user_id: UUID,
#     user_in: UserUpdate,
# ):
#     """
#     Update a user.
#     """
#
#     db_user = session.get(User, user_id)
#     if not db_user:
#         raise HTTPException(
#             status_code=404,
#             detail="The user with this id does not exist in the system",
#         )
#     if user_in.email:
#         existing_user = get_user_by_email(session=session, email=user_in.email)
#         if existing_user and existing_user.id != user_id:
#             raise HTTPException(
#                 status_code=409, detail="User with this email already exists"
#             )
#
#     db_user = update_user(session=session, db_user=db_user, user_in=user_in)
#     return db_user
#
#
# @router.delete("/{user_id}", dependencies=[Depends(current_superuser)])
# def delete_user(
#     session: SessionDep, current_user: CurrentUser, user_id: UUID
# ) -> Message:
#     """
#     Delete a user.
#     """
#     user = session.get(User, user_id)
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")
#     if user == current_user:
#         raise HTTPException(
#             status_code=403, detail="Super users are not allowed to delete themselves"
#         )
#     session.delete(user)
#     session.commit()
#     return Message(message="User deleted successfully")
