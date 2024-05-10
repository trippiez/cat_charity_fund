"""Add user relationship to donation

Revision ID: dd55d98df24a
Revises: 910affcdd6e8
Create Date: 2024-05-09 10:55:58.142719

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = 'dd55d98df24a'
down_revision = '910affcdd6e8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('donation', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(batch_op.f('fk_donation_user_id_user'), 'user', ['user_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('donation', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_donation_user_id_user'), type_='foreignkey')
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###
