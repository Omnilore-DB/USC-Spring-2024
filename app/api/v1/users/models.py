from sqlalchemy import Boolean, Column, DateTime, String, BigInteger, Enum, Date

from app.database import Base


class User(Base):
    __tablename__ = "users (legacy)"

    pk = Column(String, nullable=False, primary_key=True, index=True, unique=True)
    email = Column(String, nullable=False, index=True, unique=False)
    name = Column(String, nullable=False)
    address = Column(String)
    phone = Column(String)
    emergency_contact = Column(String)
    emergency_contact_phone = Column(String)
    date_renewed = Column(DateTime)
    is_member = Column(Boolean, default = False)
    first_joined = Column(DateTime)
    date_expired = Column(DateTime)
    profile_pic = Column(String)

    def __repr__(self):
        return f"<User {self.pk}>"


class Member(Base):
    __tablename__ = "members"

    pid = Column(BigInteger, nullable=False, primary_key=True, index=True, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    street_address = Column(String)
    city = Column(String)
    state = Column(String)
    zip = Column(String)
    phone = Column(String)
    email = Column(String)
    emergency_contact = Column(String)
    emergency_contact_phone = Column(String)
    member_status = Column(String)
    expiration_date = Column(Date)
    partner = Column(String)
    date_of_birth = Column(Date)
    deceased_date = Column(Date)
    public = Column(Boolean, default = True)
    orientation_date = Column(Date)
    date_joined = Column(Date)
    notes = Column(String)
    photo_link = Column(String)
    gender = Column(String)
    photo_path = Column(String)
