"""empty message

Revision ID: fc8d3e1e1867
Revises: ccf9f75cf8eb
Create Date: 2023-10-26 18:18:14.908838

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fc8d3e1e1867'
down_revision = 'ccf9f75cf8eb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.add_column(sa.Column('first_name', sa.String(), nullable=False))
        batch_op.add_column(sa.Column('last_name', sa.String(), nullable=False))
        batch_op.add_column(sa.Column('phone', sa.String(), nullable=False))
        batch_op.add_column(sa.Column('address', sa.String(), nullable=False))
        batch_op.create_unique_constraint(None, ['phone'])
        batch_op.create_unique_constraint(None, ['address'])
        batch_op.drop_column('body')
        batch_op.drop_column('date_created')
        batch_op.drop_column('title')

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('date_created')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('date_created', sa.DATETIME(), nullable=False))

    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.add_column(sa.Column('title', sa.VARCHAR(), nullable=False))
        batch_op.add_column(sa.Column('date_created', sa.DATETIME(), nullable=False))
        batch_op.add_column(sa.Column('body', sa.VARCHAR(), nullable=False))
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('address')
        batch_op.drop_column('phone')
        batch_op.drop_column('last_name')
        batch_op.drop_column('first_name')

    # ### end Alembic commands ###
