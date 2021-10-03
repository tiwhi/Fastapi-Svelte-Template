"""items table and user to item relationship

Revision ID: d9ff6fa760c4
Revises: c127b690703e
Create Date: 2021-08-19 10:34:56.758521

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd9ff6fa760c4'
down_revision = 'c127b690703e'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'item',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('title', sa.String, index=True),
        sa.Column('description', sa.String, index=True),
        sa.Column('owner_id', sa.Integer, sa.ForeignKey("user.id"))
    )


def downgrade():
    op.drop_table('item')
