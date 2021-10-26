"""Many To Many.

...is used when instances of a particular class can have zero or more
associations to instances of another class. For example, let's say that
we are mapping the relationship of instances of `Student` and instances
of `Class` in a system that manages a school. As many students can
participate in many classes, we would map the relationship as shown
in this file.

In this case, we had to create a helper table to persist the association
between instances of `Student` and instances of `Class`, as this
wouldn't be possible without an extra table. Note that, to make
SQLAlchemy aware of the helper table, we passed it in the secondary
parameter of the relationship function.
"""

students_classes_association = Table('students_classes', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id')),
    Column('class_id', Integer, ForeignKey('classes.id'))
)

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    classes = relationship("Class", secondary=students_classes_association)

class Class(Base):
    __tablename__ = 'classes'
    id = Column(Integer, primary_key=True)
