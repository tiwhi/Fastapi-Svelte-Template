"""init

Revision ID: c127b690703e
Revises: 
Create Date: 2021-08-17 16:44:58.420073

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c127b690703e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'user',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('full_name', sa.String, index=True),
        sa.Column('email', sa.String, unique=True, index=True, nullable=False),
        sa.Column('hashed_password', sa.String, nullable=False),
        sa.Column('is_active', sa.Boolean(), default=True),
        sa.Column('is_superuser', sa.Boolean(), default=False)
    )


def downgrade():
    op.drop_table('user')
