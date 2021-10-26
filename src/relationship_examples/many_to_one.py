"""Many To One

...refers to the same relationship described in "One to many" but from
the other perspective. To give a different example, let's say that we
want to map the relationship between instances of Tire to an instance
of a Car.

As many tires belong to one car and this car contains many tires,
we would map this relation as follows:
"""


class Tire(Base):
    __tablename__ = "tires"
    id = Column(Integer, primary_key=True)
    car_id = Column(Integer, ForeignKey("cars.id"))
    car = relationship("Car")


class Car(Base):
    __tablename__ = "cars"
    id = Column(Integer, primary_key=True)
