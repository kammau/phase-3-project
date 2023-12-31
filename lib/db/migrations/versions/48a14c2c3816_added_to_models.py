"""added to models

Revision ID: 48a14c2c3816
Revises: 7d5ff4c21f1a
Create Date: 2023-07-18 15:40:16.892647

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '48a14c2c3816'
down_revision = '7d5ff4c21f1a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('decks', sa.Column('set_name', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('decks', 'set_name')
    # ### end Alembic commands ###
