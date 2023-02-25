"""empty message

Revision ID: fda8f2f41785
Revises: c26523da51c3
Create Date: 2023-02-25 23:28:05.027577

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fda8f2f41785'
down_revision = 'c26523da51c3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('shifts', sa.Column('date', sa.Date(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('shifts', 'date')
    # ### end Alembic commands ###
