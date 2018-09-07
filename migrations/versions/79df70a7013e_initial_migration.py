"""Initial Migration

Revision ID: 79df70a7013e
Revises: 481186a46202
Create Date: 2018-09-07 23:39:34.557498

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '79df70a7013e'
down_revision = '481186a46202'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('bio', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('profile_pic_path', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'profile_pic_path')
    op.drop_column('users', 'bio')
    # ### end Alembic commands ###
