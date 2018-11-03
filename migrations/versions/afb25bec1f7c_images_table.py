"""images table

Revision ID: afb25bec1f7c
Revises: 998d82fd0f7b
Create Date: 2018-06-29 16:52:53.159899

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'afb25bec1f7c'
down_revision = '998d82fd0f7b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('file_contents',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=300), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('file_contents')
    # ### end Alembic commands ###
