"""aaa

Revision ID: 76bcd4475b15
Revises: 
Create Date: 2023-12-27 15:56:38.269710

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '76bcd4475b15'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tables')
    with op.batch_alter_table('category', schema=None) as batch_op:
        batch_op.add_column(sa.Column('page_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key(None, 'page', ['page_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('category', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('page_id')

    op.create_table('tables',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###