"""Dropped versions table

Revision ID: 68a95593bd0a
Revises: 
Create Date: 2020-03-29 16:20:16.083663

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '68a95593bd0a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('StockPrices',
    sa.Column('Ticker', sa.String(length=5), nullable=False),
    sa.Column('Price', sa.Integer(), nullable=True),
    sa.Column('Volume', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('Ticker')
    )
    op.drop_table('stockprices')
    op.drop_table('sample_data')
    op.drop_index('Name', table_name='companies')
    op.drop_table('companies')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('companies',
    sa.Column('Number', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('Name', mysql.VARCHAR(length=5), nullable=True),
    sa.PrimaryKeyConstraint('Number'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('Name', 'companies', ['Name'], unique=True)
    op.create_table('sample_data',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('firstnames', mysql.VARCHAR(length=45), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('stockprices',
    sa.Column('Ticker', mysql.VARCHAR(length=5), nullable=False),
    sa.Column('Price', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('Volume', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('Ticker'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_table('StockPrices')
    # ### end Alembic commands ###
