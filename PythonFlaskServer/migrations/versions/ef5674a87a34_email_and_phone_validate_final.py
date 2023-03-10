"""Email and phone validate final

Revision ID: ef5674a87a34
Revises: 317921084ef5
Create Date: 2022-11-07 15:09:43.297967

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ef5674a87a34'
down_revision = '317921084ef5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('users_phone_key', 'users', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('users_phone_key', 'users', ['phone'])
    # ### end Alembic commands ###
