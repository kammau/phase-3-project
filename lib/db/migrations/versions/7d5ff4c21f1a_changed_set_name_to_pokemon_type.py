"""changed set name to pokemon type

Revision ID: 7d5ff4c21f1a
Revises: bcc69cf82404
Create Date: 2023-07-17 17:01:52.756482

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7d5ff4c21f1a'
down_revision = 'bcc69cf82404'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cards', sa.Column('pokemon_type', sa.String(), nullable=True))
    op.drop_column('cards', 'set_name')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cards', sa.Column('set_name', sa.VARCHAR(), nullable=True))
    op.drop_column('cards', 'pokemon_type')
    # ### end Alembic commands ###
