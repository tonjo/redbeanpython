"""empty message

Revision ID: d2f91eafc4554288ac0a31bda9412534
Revises: 54e77f7666a24e67bb4f8ba56d9e73dd
Create Date: 2024-01-28 21:15:38.483812

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd2f91eafc4554288ac0a31bda9412534'
down_revision: Union[str, None] = '54e77f7666a24e67bb4f8ba56d9e73dd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('test',
    sa.Column('id', sa.String(length=255), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('second_name', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('test')
    # ### end Alembic commands ###