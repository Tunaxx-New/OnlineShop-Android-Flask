"""Add Map model

Revision ID: 745d612eb7fb
Revises: 166ca87ba6cb
Create Date: 2022-12-09 20:00:19.182394

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '745d612eb7fb'
down_revision = '166ca87ba6cb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('shop_position',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('shop_id', sa.Integer(), nullable=True),
    sa.Column('meridian', sa.REAL(), nullable=True),
    sa.Column('longitude', sa.REAL(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('shop_position')
    # ### end Alembic commands ###
