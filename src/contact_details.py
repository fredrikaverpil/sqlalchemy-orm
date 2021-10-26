"""Contact details.

nstances of this class will hold a phone_number and an address of a
particular `Actor`, and one `Actor` will be able to have many
`ContactDetails` associated. Therefore, we will need to use the Many
To One relationship pattern to map this association.
"""

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from base import Base


class ContactDetails(Base):
    __tablename__ = 'contact_details'

    id = Column(Integer, primary_key=True)
    phone_number = Column(String)
    address = Column(String)
    actor_id = Column(Integer, ForeignKey('actors.id'))
    actor = relationship("Actor", backref="contact_details")

    def __init__(self, phone_number, address, actor):
        self.phone_number = phone_number
        self.address = address
        self.actor = actor