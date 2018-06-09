"""empty message

Revision ID: fd1c0edd4d0c
Revises: d90ada55083e
Create Date: 2018-06-09 12:39:46.798227

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fd1c0edd4d0c'
down_revision = 'd90ada55083e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('event',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('coreid', sa.String(), nullable=True),
    sa.Column('data', sa.String(), nullable=True),
    sa.Column('productID', sa.String(), nullable=True),
    sa.Column('public', sa.Boolean(), nullable=True),
    sa.Column('published_at', sa.DateTime(), nullable=True),
    sa.Column('ttl', sa.Integer(), nullable=True),
    sa.Column('userid', sa.String(), nullable=True),
    sa.Column('version', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('event')
    # ### end Alembic commands ###
