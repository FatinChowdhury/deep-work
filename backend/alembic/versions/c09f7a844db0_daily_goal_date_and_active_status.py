"""Daily goal date and active status

Revision ID: c09f7a844db0
Revises: c73c26aaa64d
Create Date: 2023-12-12 21:34:12.142733

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel.sql.sqltypes


# revision identifiers, used by Alembic.
revision: str = "c09f7a844db0"
down_revision: Union[str, None] = "c73c26aaa64d"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("dailygoal", sa.Column("created_at", sa.DateTime(), nullable=True))
    op.add_column("dailygoal", sa.Column("is_active", sa.Boolean(), nullable=True))

    dailygoal_table = sa.table(
        "dailygoal",
        sa.column("created_at", sa.DateTime),
        sa.column("is_active", sa.Boolean),
    )

    op.execute(
        dailygoal_table.update().values(
            {"created_at": sa.func.now(), "is_active": False}
        )
    )

    op.alter_column("dailygoal", "created_at", nullable=False)
    op.alter_column("dailygoal", "is_active", nullable=False)


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("dailygoal", "is_active")
    op.drop_column("dailygoal", "created_at")
    # ### end Alembic commands ###