"""
`deps` = dependency

-------------------------------------------------------------------------
# What is "Dependency Injection"

==> https://fastapi.tiangolo.com/tutorial/dependencies/

"Dependency Injection" means, in programming, that there is a way for your code (in this case, your path operation functions) to declare things that it requires to work and use: "dependencies".

-------------------------------------------------------------------------
This is a first look at FastAPI’s powerful dependency injection capabilities, which for my money is one of the frameworks best features. Dependency Injection (DI) is a way for your functions and classes to declare things they need to work (in a FastAPI context, usually our endpoint functions which are called path operation functions).

We’ll be exploring dependency injection in much more detail later in the tutorial. For now, what you need to appreciate is that the FastAPI Depends class is used in our function parameters like so:

db: Session = Depends(deps.get_db)

And what we pass into Depends is a function specifying the dependency. In this part of the tutorial, we’ve added these functions in the deps.py module:
"""

# 1. We import the ORM session class `SessionLocal` from `app/db/session.py`
# 2. We instantiate the session by `db = SessionLocal()`
# 3. We `yield` the session, which returns a generator. Why do this? Well, the `yield` statement suspends the function’s execution and sends a value back to the caller, but retains enough state to enable the function to resume where it is left off. In short, it’s an efficient way to work with our database connection. Python generators primer for those unfamiliar.
# 4. We make sure we close the DB connection by using the `finally` clause of the `try` block - meaning that the DB session is always closed. This releases connection objects associated with the session and leaves the session ready to be used again.

from typing import Generator

from app.db.session import SessionLocal     #1

def get_db() -> Generator:
    db = SessionLocal()         #2
    db.current_user_id = None
    try:
        yield db                #3
    finally:
        db.close()              #4
