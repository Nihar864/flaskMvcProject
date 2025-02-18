"""empty message

Revision ID: 4bf71360fe33
Revises: 09b50793de97
Create Date: 2025-02-03 13:33:57.568524

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '4bf71360fe33'
down_revision = '09b50793de97'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('category_table', schema=None) as batch_op:
        batch_op.add_column(sa.Column('Category_created_on', sa.String(length=150), nullable=False))
        batch_op.add_column(sa.Column('Category_modified_on', sa.String(length=150), nullable=False))
        batch_op.drop_column('Category_Created_on')
        batch_op.drop_column('Category_Modified_on')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('category_table', schema=None) as batch_op:
        batch_op.add_column(sa.Column('Category_Modified_on', mysql.DATETIME(), nullable=True))
        batch_op.add_column(sa.Column('Category_Created_on', mysql.DATETIME(), nullable=True))
        batch_op.drop_column('Category_modified_on')
        batch_op.drop_column('Category_created_on')

    # ### end Alembic commands ###
