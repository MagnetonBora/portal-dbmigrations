"""add nickname field to User model

Revision ID: eb382e4a1b82
Revises: ffbce0fc0a38
Create Date: 2020-03-01 16:48:36.826239

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eb382e4a1b82'
down_revision = 'ffbce0fc0a38'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('nickname', sa.String(length=50), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'nickname')
    # ### end Alembic commands ###
