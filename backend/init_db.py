from app.models import Base # Import Base from the models package
from app.models import user, question # Import all models to ensure they are registered
from app.models import engine # Import engine from the models package

def create_tables():
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully!")

if __name__ == "__main__":
    create_tables()