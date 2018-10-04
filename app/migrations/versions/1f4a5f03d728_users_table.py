"""users table

Revision ID: 1f4a5f03d728
Revises: 
Create Date: 2018-10-04 16:48:45.055068

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '1f4a5f03d728'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('first_name', mysql.VARCHAR(length=128), nullable=True),
    sa.Column('last_name', mysql.VARCHAR(length=128), nullable=True),
    sa.Column('email', mysql.TEXT(), nullable=True),
    sa.Column('password_hashed', mysql.VARCHAR(length=256), nullable=True),
    sa.Column('username', mysql.VARCHAR(length=32), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###
