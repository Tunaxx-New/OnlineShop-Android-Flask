"""unit nullable is false

Revision ID: 03ea23b3e865
Revises: 874fc46afa53
Create Date: 2022-11-27 21:39:31.106347

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '03ea23b3e865'
down_revision = '874fc46afa53'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('products', 'unit',
               existing_type=sa.VARCHAR(length=32),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('products', 'unit',
               existing_type=sa.VARCHAR(length=32),
               nullable=True)
    # ### end Alembic commands ###
