"""empty message

Revision ID: ac55902fcc3d
Revises: 7d55a089b5bc
Create Date: 2018-02-25 17:42:29.388863

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ac55902fcc3d'
down_revision = '7d55a089b5bc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('validation_message', sa.Boolean(), nullable=False, server_default=sa.true()))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'validation_message')
    # ### end Alembic commands ###