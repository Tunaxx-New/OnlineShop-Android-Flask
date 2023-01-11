"""Added Message table

Revision ID: c4dfa4061332
Revises: a4d12d4f172c
Create Date: 2022-11-10 11:28:34.753472

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c4dfa4061332'
down_revision = 'a4d12d4f172c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('messages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created', sa.TIMESTAMP(), nullable=False),
    sa.Column('from_id', sa.Integer(), nullable=False),
    sa.Column('to_id', sa.Integer(), nullable=False),
    sa.Column('data', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('messages')
    # ### end Alembic commands ###