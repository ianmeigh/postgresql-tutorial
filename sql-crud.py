from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    select,
)
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import generic_repr

# Executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")  # , echo=True)
""" 
postgresql: - Database Type
///         - Localhost
chinook     - Database Name
"""
base = declarative_base()

# Create a class-based model for the "Programmer" table
@generic_repr  # SQLAlchemy-Utils replaces manually created '__repr__'
class Programmer(base):
    __tablename__ = "Programmer"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)

    @property
    def fullname(self):
        return self.first_name + " " + self.last_name


# Instead of connecting to the database directly, we will ask for a session.
# Create a new instance of sessionmaker, then point to our engine (db)
Session = sessionmaker(db)

# Opens an actual session by calling the Session() subclass defined above
session = Session()

# Create the database using declarative_base subclass
base.metadata.create_all(db)

# ----------------------------------- CREATE ----------------------------------

# Creating records on our Programmer table
ada_lovelace = Programmer(
    first_name="Ada",
    last_name="Lovelace",
    gender="F",
    nationality="British",
    famous_for="First Programmer",
)

alan_turning = Programmer(
    first_name="Alan",
    last_name="Turing",
    gender="M",
    nationality="British",
    famous_for="Modern Computing",
)

grace_hopper = Programmer(
    first_name="Grace",
    last_name="Hopper",
    gender="F",
    nationality="American",
    famous_for="COBOL Language",
)

margaret_hamilton = Programmer(
    first_name="Margaret",
    last_name="Hamilton",
    gender="F",
    nationality="American",
    famous_for="Apollo 11",
)

bill_gates = Programmer(
    first_name="Bill",
    last_name="Gates",
    gender="M",
    nationality="American",
    famous_for="Microsoft",
)

tim_berners_lee = Programmer(
    first_name="Tim",
    last_name="Burners-Lee",
    gender="M",
    nationality="British",
    famous_for="World Wide Web",
)

alice_sample = Programmer(
    first_name="Alice",
    last_name="Sample",
    gender="F",
    nationality="British",
    famous_for="Sample Entry",
)

# Add each instance of our programmers to our session
# session.add(ada_lovelace)
# session.add(alan_turning)
# session.add(grace_hopper)
# session.add(margaret_hamilton)
# session.add(bill_gates)
# session.add(tim_berners_lee)
# session.add(alice_sample)

# commit out session to the database
# session.commit()

# ------------------------- UPDATING A SINGLE RECORD --------------------------

# programmer = session.query(Programmer).filter_by(id=7).first()
# programmer.famous_for = "UPDATE: Helping Others"

# commit out session to the database
# session.commit()

# ------------------------- UPDATING MULTIPLE RECORDS -------------------------

# people = session.query(Programmer)
# for person in people:
#     if person.gender == "F":
#         person.gender = "Female"
#     elif person.gender == "M":
#         person.gender = "Male"
#     else:
#         print("Gender not defined")
#     session.commit()

# ------------------------- DELETING A SINGLE RECORD --------------------------

# fname = input("Enter a first name: ").strip(" \t")
# lname = input("Enter a last name: ").strip(" \t")

# programmer = (
#     session.query(Programmer)
#     .filter_by(first_name=fname, last_name=lname)
#     .first()
# )

# if programmer is not None:
#     print(f"Programmer found: {programmer.first_name} {programmer.last_name}")
#     confirmation = input(
#         "Are you sure you wish to delete this record? (y/n)\n>> : "
#     )
#     if confirmation.lower() == "y":
#         session.delete(programmer)
#         session.commit()
#         print("Programmer has been deleted")
#     else:
#         print("Programmer not deleted")
# else:
#     print("No records found")

# ------------------------------------ READ -----------------------------------

# QUERY
programmers = session.query(Programmer)
for programmer in programmers:
    print(
        programmer.id,
        programmer.fullname,
        programmer.gender,
        programmer.nationality,
        programmer.famous_for,
        sep=" | ",
    )

# EXECUTE
# programmers = session.execute(select(Programmer))
# print(programmers.all())
