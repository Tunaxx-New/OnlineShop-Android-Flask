"""Changed role table

Revision ID: 61a4bb7f47a0
Revises: 47a7d4a2b959
Create Date: 2022-11-10 11:33:38.734706

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '61a4bb7f47a0'
down_revision = '47a7d4a2b959'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('roles', 'user_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('roles', sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
