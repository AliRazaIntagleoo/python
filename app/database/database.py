from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker, Session
from pathlib import Path
from typing import Generator

from app.database.base import Base

# ---- DB PATH ----
BASE_DIR = Path(__file__).resolve().parent.parent.parent
DB_PATH = BASE_DIR / "my_database.db"
DATABASE_URL = f"sqlite:///{DB_PATH}"

# ---- ENGINE ----
engine = create_engine(
    DATABASE_URL,
    connect_args={
        "check_same_thread": False,
        "timeout": 30
    }
)
@event.listens_for(engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA journal_mode=DELETE;")
    cursor.execute("PRAGMA synchronous=NORMAL;")
    cursor.close()
# ---- SESSION ----
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

# ---- INIT DB ----
def init_db() -> None:
    Base.metadata.create_all(bind=engine)

# ---- DEPENDENCY ----
def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
