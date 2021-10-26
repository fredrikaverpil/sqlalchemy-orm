"""Base."""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Whenever we want to interact with a db, we need to create an engine
# More info on engines here:
# http://docs.sqlalchemy.org/en/rel_1_1/core/engines.html
#
# Pool settings can be set here:
# https://docs.sqlalchemy.org/en/14/core/pooling.html
engine = create_engine("postgresql://postgres:changeme@localhost:5432/postgres")

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()
