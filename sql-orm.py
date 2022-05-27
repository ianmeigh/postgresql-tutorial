from sqlalchemy import (
    create_engine,
    Column,
    Float,
    ForeignKey,
    Integer,
    String,
    select,
    or_,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import generic_repr


# Executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook", echo=True)

""" 
postgresql: - Database Type
///         - Localhost
chinook     - Database Name
"""

base = declarative_base()

# Create class based model for the "Artist" table
class Artist(base):
    __tablename__ = "Artist"
    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)

    def __str__(self):
        return f"{self.ArtistId} | {self.Name}"


# Create class based model for the "Album" table
class Album(base):
    __tablename__ = "Album"
    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeignKey("Artist.ArtistId"))


# Create class based model for the "Track" table
@generic_repr  # SQLAlchemy-Utils replaces manually created '__repr__'
class Track(base):
    __tablename__ = "Track"
    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey("Album.AlbumId"))
    MediaTypeId = Column(Integer, primary_key=False)
    GenreId = Column(Integer, primary_key=False)
    Composer = Column(String)
    Milliseconds = Column(Integer)
    Bytes = Column(Integer)
    UnitPrice = Column(Float)

    # def __repr__(self):
    #     return f"Track(TrackId={self.TrackId!r}), (Name={self.Name!r}), (AlbumId={self.AlbumId!r})"  # , MediaTypeId={self.MediaTypeId!r}, GenreId={self.GenreId!r}, Composer={self.Composer!r}, Milliseconds={self.Milliseconds!r}, Bytes={self.Bytes!r}, UnitPrice={self.UnitPrice!r}"


# Instead of connecting to the database directly, we will ask for a session.
# Create a new instance of sessionmaker, then point to our engine (db)
Session = sessionmaker(db)

# Opens an actual session by calling the Session() subclass defined above
session = Session()

# Create the database using declarative_base subclass
base.metadata.create_all(db)

# ---------------------------- Query 1 -----------------------------------
# ------------- Select all records from the "Artist" table ---------------

# -- CI Example using query API

# artists = session.query(Artist)
# for artist in artists:
#     print(artist)  # Makes use of __str__ dunder method defined in the class
#     print(artist.ArtistId, artist.Name, sep=" || ")

# -- Example using execute

# As 'query' construct is now legacy(1), try with 'execute'(2)
# 1 - https://docs.sqlalchemy.org/en/20/orm/query.html
# 2 - https://docs.sqlalchemy.org/en/20/orm/queryguide.html

# ---- The code below would return a Row object

# stmt = select(Artist)
# results = session.execute(stmt)
# for result in results:
#     print(result[0].ArtistId, result[0].Name, sep=" || ")

# ---- When selecting a list of single-element rows containing ORM entities, it
# is typical to skip the generation of Row objects and instead receive ORM
# entities directly, which is achieved using the Result.scalars() method

# stmt = select(Artist)
# results = session.execute(stmt)
# for result in results.scalars():
#     print(result)  # Makes use of __str__ dunder method defined in the class

# ---- As show in the SQLAlchemy documentation
# (https://docs.sqlalchemy.org/en/20/orm/query.html):

# ---------------------------- Query 2 -----------------------------------
# ------- select only the "Name" colum from the "Artist" table -----------

# QUERY
# artists = session.query(Artist)
# for artist in artists:
#     print(artist.Name)

# EXECUTE
# results = session.execute(select(Artist.Name))
# print(results.all())

# ---------------------------- Query 3 -----------------------------------
# ---------- select only "Queen" from the "Artist" table -----------------

# QUERY
# results = session.query(Artist).filter_by(Name="Queen").first()
# print(results)  # Makes use of __str__ dunder method defined in the class

# EXECUTE
# results = session.execute(
#     select(Artist.ArtistId, Artist.Name).filter_by(Name="Queen")
# )
# print(results.all())

# ---------------------------- Query 3.1 ----------------------------------
# - select matching artists ("Queen" and "AC/DC") from the "Artist" table -

# QUERY EX.1
# results = session.query(Artist).where(Artist.Name.in_(["Queen", "AC/DC"]))
# for result in results:
#     print(result)

# QUERY EX.2
# results = session.query(Artist).where(
#     or_(Artist.Name == "Queen", Artist.Name == "AC/DC")
# )
# for result in results:
#     print(result)

# EXECUTE EX.1
# results = session.execute(
#     select(Artist.ArtistId, Artist.Name).where(
#         or_(Artist.Name == "Queen", Artist.Name == "AC/DC")
#     )
# )
# print(results.all())

# EXECUTE EX.2
# results = session.execute(
#     select(Artist.ArtistId, Artist.Name).where(
#         Artist.Name.in_(["Queen", "AC/DC"])
#     )
# )
# print(results.all())

# ---------------------------- Query 4 -----------------------------------
# ------- select only by "ArtistId" #51 from the "Artist" table ----------

# QUERY
# results = session.query(Artist).filter_by(ArtistId=51).first()
# print(results)

# EXECUTE
# results = session.execute(
#     select(Artist.ArtistId, Artist.Name).filter_by(ArtistId=51)
# )
# print(results.first())

# ---------------------------- Query 5 -----------------------------------
# --- select only the albums with "ArtistId" #51 on the "Album" table ----

# QUERY
# results = session.query(Album).filter_by(ArtistId=51)
# for result in results:
#     print(
#         result.AlbumId, result.Title, result.ArtistId, sep=" | "
#     )  # No __str__ dunder method :(

# EXECUTE
# results = session.execute(
#     select(Album.AlbumId, Album.Title, Album.ArtistId).filter_by(ArtistId=51)
# )
# print(results.all())

# ---------------------------- Query 6 -----------------------------------
# -select all tracks where the composer is "Queen" from the "Track" table-

# QUERY
# results = session.query(Track).filter_by(Composer="Queen")
# for result in results:
#     print(
#         result.TrackId,
#         result.Name,
#         result.AlbumId,
#         result.MediaTypeId,
#         result.GenreId,
#         result.Composer,
#         result.Milliseconds,
#         result.Bytes,
#         result.UnitPrice,
#         sep=" | ",
#     )

# EXECUTE
# results = session.execute(select(Track).filter_by(Composer="Queen"))
# print(results.all())
