from .engine import Base,engine
from .models import User

__all__ =[
    "Base",
    "User",
]

# Drop all tables (be careful: deletes all data)
Base.metadata.drop_all(bind=engine)

# Recreate tables according to current models
Base.metadata.create_all(bind=engine)

print("Database tables recreated successfully!")
