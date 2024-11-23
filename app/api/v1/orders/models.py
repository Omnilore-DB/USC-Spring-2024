"""DB Models for orders."""

import enum

from sqlalchemy import DateTime, Enum, Float
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import String
from sqlalchemy.sql.sqltypes import Boolean

from app.database import Base


class PaymentPlatform(str, enum.Enum):
    STRIPE = "STRIPE"
    PAYPAL = "PAYPAL"
    MAIL = "MAIL"


class Order(Base):
    __tablename__ = "orders"

    sqsp_transaction_id = Column(
        String,
        nullable=False,
        primary_key=True,
        index=True,
        unique=True,
    )
    sqsp_order_id = Column(String, index=True, nullable=True)
    user_emails = Column(
        ARRAY(String),
        nullable=False,
    )  # Assuming users table with email as primary key
    amount = Column(Float, nullable=False)
    date = Column(DateTime, nullable=False)
    skus = Column(ARRAY(String), nullable=False)
    # payment_method = Column(String)  # Enum? either STRIPE or PAYPAL
    payment_platform = Column(Enum(PaymentPlatform), nullable=False)
    fee = Column(Float, default=0.0)
    external_transaction_id = Column(String, nullable=False)
    user_names = Column(ARRAY(String), nullable=True)
    user_amounts = Column(ARRAY(Float), nullable=True)

    def __repr__(self):
        return f"<Order {self.sqsp_transaction_id}>"

    # def __init__(
    #     self,
    #     id: str,
    #     orderNumber: str,
    #     total: str,
    #     createdOn: str,
    #     modifiedOn: str,
    #     customerEmail: str,
    #     billingAddress: str,
    # ):
    #     self.id = id
    #     self.orderNumber = orderNumber
    #     self.total = total
    #     self.createdOn = createdOn
    #     self.modifiedOn = modifiedOn
    #     self.customerEmail = customerEmail
    #     self.billingsAddress = billingAddress
