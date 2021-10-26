"""One To One.

...refers to relationships where an instance of a particular class may
only be associated with one instance of another class, and vice versa.

As an example, consider the relationship between a `Person` and a
`MobilePhone`. Usually, one person possesses one mobile phone and this
mobile phone belongs to this person only. To map this relationship on
SQLAlchemy, we would create the code in this file.

In this example, we pass two extra parameters to the relationship
function. The first one, `uselist=False`, makes SQLAlchemy understand
that `mobile_phone` will hold only a single instance and not an array
(multiple) of instances. The second one, `back_populates`, instructs
SQLAlchemy to populate the other side of the mapping. The official
Relationships API documentation provides a complete explanation of these
parameters and also covers other parameters not mentioned here.

"""


class Person(Base):
    __tablename__ = "people"
    id = Column(Integer, primary_key=True)
    mobile_phone = relationship("MobilePhone", uselist=False, back_populates="person")


class MobilePhone(Base):
    __tablename__ = "mobile_phones"
    id = Column(Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey("people.id"))
    person = relationship("Person", back_populates="mobile_phone")
