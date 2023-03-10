"""feat Item isFinished

Revision ID: 868d9c207017
Revises: 936ccb8f0080
Create Date: 2022-11-27 21:17:47.116447

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '868d9c207017'
down_revision = '936ccb8f0080'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('items', sa.Column('isFinished', sa.Boolean(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('items', 'isFinished')
    # ### end Alembic commands ###
