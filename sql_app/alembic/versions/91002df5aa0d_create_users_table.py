"""create users table

Revision ID: 91002df5aa0d
Revises: 
Create Date: 2022-05-26 18:53:25.170501

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '91002df5aa0d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True, unique=True),
        sa.Column('email', sa.String(200), nullable=False),
        sa.Column('hashed_password', sa.Unicode(200)),
        sa.Column('is_active', sa.Boolean),
    )


def downgrade():
    op.drop_table('users')
