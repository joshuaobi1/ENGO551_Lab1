import csv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import text


# Assuming you've set your DATABASE_URL environment variable externally, or you can set it here again
os.environ["DATABASE_URL"] = 'postgresql://postgres:tGreyjoy789?@localhost/ENGO551Lab1'

# Ensure the environment variable for your database URL is set
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Set up database connection using the same approach as in application.py
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

def import_books():
    # Open and read the books.csv file
    with open("books.csv", "r") as f:
        reader = csv.reader(f)
        next(reader)  # Skip the header row to avoid importing it

        for isbn, title, author, year in reader:
            # Insert book data into the database
            db.execute(text("INSERT INTO books (isbn, title, author, year) VALUES (:isbn, :title, :author, :year)"),
           {"isbn": isbn, "title": title, "author": author, "year": year})
            print(f"Added book {title} with ISBN {isbn} to database.")
        db.commit()

if __name__ == "__main__":
    import_books()
