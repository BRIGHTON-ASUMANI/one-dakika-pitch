"""making a few migrations

Revision ID: 003973612c46
Revises: 0b3b8eaf6204
Create Date: 2018-09-12 15:18:19.890155

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '003973612c46'
down_revision = '0b3b8eaf6204'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('techcom', sa.Column('tech_id', sa.Integer(), nullable=True))
    op.drop_constraint('techcom_technology_id_fkey', 'techcom', type_='foreignkey')
    op.create_foreign_key(None, 'techcom', 'technology', ['tech_id'], ['id'])
    op.drop_column('techcom', 'technology_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('techcom', sa.Column('technology_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'techcom', type_='foreignkey')
    op.create_foreign_key('techcom_technology_id_fkey', 'techcom', 'technology', ['technology_id'], ['id'])
    op.drop_column('techcom', 'tech_id')
    # ### end Alembic commands ###
