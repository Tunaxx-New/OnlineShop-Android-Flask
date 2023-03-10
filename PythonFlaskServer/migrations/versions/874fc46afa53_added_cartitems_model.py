"""Added CartItems model

Revision ID: 874fc46afa53
Revises: 450f218d7eab
Create Date: 2022-11-27 21:37:46.199843

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '874fc46afa53'
down_revision = '450f218d7eab'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('items', 'unit')
    op.add_column('products', sa.Column('unit', sa.String(length=32), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('products', 'unit')
    op.add_column('items', sa.Column('unit', sa.VARCHAR(length=32), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
