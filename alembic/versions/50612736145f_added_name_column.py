"""added name column

Revision ID: 50612736145f
Revises: 68a95593bd0a
Create Date: 2020-03-29 16:49:42.129050

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '50612736145f'
down_revision = '68a95593bd0a'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('stockprices', sa.Column('name', sa.String(length=5)))


def downgrade():
    pass
