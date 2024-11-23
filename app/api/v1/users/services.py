"""Services for users."""

from datetime import datetime
from typing import Optional

from sqlalchemy.orm import Session

from app.api.v1.users.models import User, Member


def get_user_by_pk(session: Session, name: str, email: str):
    return session.query(User).filter(User.pk == f"{name}_{email}").first()

def get_member_by_name_and_email(session: Session, first_name: str, email: str):
    return session.query(Member).filter(Member.first_name == first_name, Member.email == email).first()

def create_user(
    session: Session,
    email: str,
    name: str,
    address: str,
    phone: str,
    first_joined: Optional[datetime] = None,
    date_expired: Optional[datetime] = None,
    emergency_contact: Optional[str] = None,
    emergency_contact_phone: Optional[str] = None,
    is_member: Optional[bool] = False,
    date_renewed: Optional[datetime] = None,
):
    new_user = User(
        pk=f"{name}_{email}",
        email=email,
        name=name,
        address=address,
        phone=phone,
        emergency_contact=emergency_contact,
        emergency_contact_phone=emergency_contact_phone,
        is_member=is_member,
        first_joined=first_joined,
        date_expired=date_expired,
        date_renewed=date_renewed,
    )
    return new_user


def upsert_user(
    session: Session,
    email: str,
    name: str,
    address: str,
    phone: str,
    date_renewed: Optional[datetime] = None,
    date_expired: Optional[datetime] = None,
    emergency_contact: Optional[str] = None,
    emergency_contact_phone: Optional[str] = None,
    is_member: Optional[bool] = False,
):
    user = get_user_by_pk(session, name, email)
    if user:
        # since already exists, update date_renewed not first_joined
        if name:
            user.name = name
        if address:
            user.address = address
        if phone:
            user.phone = phone
        if email:
            user.email = email
        if is_member:
            user.is_member = is_member
        if date_renewed:
            user.date_renewed = date_renewed
        if date_expired:
            user.date_expired = date_expired
        if emergency_contact:
            user.emergency_contact = emergency_contact
        if emergency_contact_phone:
            user.emergency_contact_phone = emergency_contact_phone
    else:
        # notice passing in date_renewed to first_joined because since this user doesn't exist, date_renewed is the actual join date
        user = create_user(
            session,
            email=email,
            name=name,
            address=address,
            phone=phone,
            emergency_contact=emergency_contact,
            emergency_contact_phone=emergency_contact_phone,
            is_member=is_member,
            first_joined=date_renewed,
            date_expired=date_expired,
            date_renewed=date_renewed,
        )
    session.add(user)
    session.flush()
    session.refresh(user)
    return user

"""
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

"""

def create_member(
    session: Session,
    email: str,
    first_name: str,
    last_name: str,
    street_address: str,
    city: str,
    state: str,
    zip: str,
    phone: str,
    first_joined: Optional[datetime] = None,
    date_expired: Optional[datetime] = None,
    emergency_contact: Optional[str] = None,
    emergency_contact_phone: Optional[str] = None,
    is_member: Optional[bool] = False,
    date_renewed: Optional[datetime] = None,
):
    return Member(
        first_name=first_name,
        last_name=last_name,
        street_address=street_address,
        city=city,
        state=state,
        zip=zip,
        phone=phone,
        email=email,
        emergency_contact=emergency_contact,
        emergency_contact_phone=emergency_contact_phone,
        member_status="YrE" if is_member else None,
        expiration_date=date_expired,
        partner="",
        public=True,
        orientation_date=first_joined,
        date_joined=first_joined,
    )

def upsert_member(
    session: Session,
    email: str,
    first_name: str,
    last_name: str,
    street_address: str,
    city: str,
    state: str,
    zip: str,
    phone: str,
    date_renewed: Optional[datetime] = None,
    date_expired: Optional[datetime] = None,
    emergency_contact: Optional[str] = None,
    emergency_contact_phone: Optional[str] = None,
    is_member: Optional[bool] = None,
):
    member = get_member_by_name_and_email(session, first_name, email)
    if member:
        if first_name:
            member.first_name = first_name
        if last_name:
            member.last_name = last_name
        if street_address:
            member.street_address = street_address
        if city:
            member.city = city
        if state:
            member.state = state
        if zip:
            member.zip = zip
        if phone:
            member.phone = phone
        if email:
            member.email = email
        if is_member:
            member.member_status = "YrE"
        if date_renewed:
            member.orientation_date = date_renewed
        if date_expired:
            member.expiration_date = date_expired
        if emergency_contact:
            member.emergency_contact = emergency_contact
        if emergency_contact_phone:
            member.emergency_contact_phone = emergency_contact_phone
    else:
        member = create_member(
            session,
            email=email,
            first_name=first_name,
            last_name=last_name,
            street_address=street_address,
            city=city,
            state=state,
            zip=zip,
            phone=phone,
            emergency_contact=emergency_contact,
            emergency_contact_phone=emergency_contact_phone,
            is_member=is_member,
            first_joined=date_renewed,
            date_expired=date_expired,
        )
    session.add(member)
    session.flush()
    session.refresh(member)
    return member
