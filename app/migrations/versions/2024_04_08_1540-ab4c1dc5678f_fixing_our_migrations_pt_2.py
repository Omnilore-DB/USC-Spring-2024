"""fixing our migrations pt 2

Revision ID: ab4c1dc5678f
Revises: d4d397c3f402
Create Date: 2024-04-08 15:40:53.320621

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "ab4c1dc5678f"
down_revision: Union[str, None] = "d4d397c3f402"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index("ix_orders_sqsp_order_id", table_name="orders")
    op.drop_table("orders")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "orders",
        sa.Column(
            "amount",
            sa.DOUBLE_PRECISION(precision=53),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column("date", postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
        sa.Column(
            "fee",
            sa.DOUBLE_PRECISION(precision=53),
            autoincrement=False,
            nullable=True,
        ),
        sa.Column(
            "created_at",
            postgresql.TIMESTAMP(),
            autoincrement=False,
            nullable=True,
        ),
        sa.Column(
            "updated_at",
            postgresql.TIMESTAMP(),
            autoincrement=False,
            nullable=True,
        ),
        sa.Column(
            "user_emails",
            postgresql.ARRAY(sa.VARCHAR()),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column(
            "payment_platform",
            postgresql.ENUM("STRIPE", "PAYPAL", name="paymentplatform"),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column(
            "external_transaction_id",
            sa.VARCHAR(),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column(
            "sqsp_transaction_id",
            sa.VARCHAR(),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column("sqsp_order_id", sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.Column(
            "skus",
            postgresql.ARRAY(sa.VARCHAR()),
            autoincrement=False,
            nullable=False,
        ),
    )
    op.create_index(
        "ix_orders_sqsp_order_id",
        "orders",
        ["sqsp_order_id"],
        unique=False,
    )
    # ### end Alembic commands ###