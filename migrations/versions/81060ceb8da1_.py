"""empty message

Revision ID: 81060ceb8da1
Revises: 313db0676132
Create Date: 2024-11-12 12:57:31.346523

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '81060ceb8da1'
down_revision = '313db0676132'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('custom_fields1',
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('value', sa.String(length=500), nullable=True),
    sa.PrimaryKeyConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('custom_fields1')
    # ### end Alembic commands ###
