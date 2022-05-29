# SQLAlchemy 1.4 Documentation
# https://docs.sqlalchemy.org/en/14/index.html

from platform import release
from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Date,
    Float,
    select,
)
import datetime

# Changed in version 1.4: The declarative_base() function is now a
# specialization of the more generic registry class. The function also moves to
# the sqlalchemy.orm package from the declarative.ext package.
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy_utils import generic_repr


# The Engine is a factory that can create new database connections for us,
# which also holds onto connections inside of a Connection Pool for fast reuse.
engine = create_engine("postgresql:///chinook")

Base = declarative_base()


@generic_repr
class Game(Base):
    __tablename__ = "Games"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    genre = Column(String)
    release = Column(Date)
    publisher = Column(String)
    metacritic_score = Column(Float)


# https://docs.sqlalchemy.org/en/14/orm/session_api.html?highlight=session%20maker#sqlalchemy.orm.sessionmaker

Session = sessionmaker(engine)

Base.metadata.create_all(engine)

# EXAMPLES

# with Session() as session:
#     session.add(some_object)
#     session.add(some_other_object)
#     session.commit()

# Context manager use is optional; otherwise, the returned Session object may
# be closed explicitly via the Session.close() method. Using a try:/finally:
# block is optional, however will ensure that the close takes place even if
# there are database errors:

# session = Session()
# try:
#     session.add(some_object)
#     session.add(some_other_object)
#     session.commit()
# finally:
#     session.close()

# sessionmaker acts as a factory for Session objects in the same way as an
# Engine acts as a factory for Connection objects. In this way it also includes
# a sessionmaker.begin() method, that provides a context manager which both
# begins and commits a transaction, as well as closes out the Session when
# complete, rolling back the transaction if any errors occur:

# with Session.begin() as session:
#     session.add(some_object)
#     session.add(some_other_object)
# commits transaction, closes session

# ----------------------------------- CREATE ----------------------------------

metal_gear_solid = Game(
    name="Metal Gear Solid",
    genre="Action Adventure",
    release=datetime.datetime(1998, 10, 21),
    publisher="Konami",
    metacritic_score="9.4",
)

final_fantasy_8 = Game(
    name="Final Fantasy 8",
    genre="RPG",
    release=datetime.datetime(1999, 9, 7),
    publisher="SquareSoft",
    metacritic_score="9.0",
)

with Session.begin() as session:
    session.add_all([metal_gear_solid, final_fantasy_8])

# ------------------------- UPDATING A SINGLE RECORD --------------------------

# session = Session()

# stmt = select(Game).filter_by(name="Final Fantasy 8")

# result = session.execute(stmt).scalars().first()
# result.publisher = "SquareEnix"

# session.commit()


# ------------------------- UPDATING MULTIPLE RECORDS -------------------------

# session = Session()

# stmt = select(Game)

# results = session.scalars(stmt)
# for result in results:
#     result.metacritic_score = 10
#     session.commit()

# ------------------------- DELETING A SINGLE RECORD --------------------------

# session = Session()

# stmt = select(Game).where(Game.id == 1)
# result = session.scalars(stmt).one()
# session.delete(result)
# session.commit()

# ------------------------ ALT DELETING A SINGLE RECORD -----------------------

# session = Session()

# ff8 = session.get(Game, 2)
# session.delete(ff8)
# session.commit()

# ------------------------------------ READ -----------------------------------

results = session.execute(select(Game)).all()
print(results)
