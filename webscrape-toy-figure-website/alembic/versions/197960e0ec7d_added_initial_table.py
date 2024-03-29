"""Added initial table

Revision ID: 197960e0ec7d
Revises: 
Create Date: 2022-08-07 13:36:09.888115

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '197960e0ec7d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=256), nullable=True),
    sa.Column('shop_product_code', sa.String(length=256), nullable=True),
    sa.Column('order_time_start', sa.DateTime(), nullable=True),
    sa.Column('order_time_end', sa.DateTime(), nullable=True),
    sa.Column('delivery_date', sa.DateTime(), nullable=True),
    sa.Column('company', sa.String(length=256), nullable=True),
    sa.Column('original_website', sa.String(length=256), nullable=True),
    sa.Column('img_url', sa.String(length=256), nullable=True),
    sa.Column('order_status', sa.String(length=256), nullable=True),
    sa.Column('is_favourite', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('create_by', sa.String(length=256), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('update_by', sa.String(length=256), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_product_shop_product_code'), 'product', ['shop_product_code'], unique=False)
    op.create_table('order',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('order_at', sa.DateTime(), nullable=True),
    sa.Column('pay_at', sa.DateTime(), nullable=True),
    sa.Column('qty', sa.Integer(), nullable=True),
    sa.Column('total_price', sa.Integer(), nullable=True),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('create_by', sa.String(length=256), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('update_by', sa.String(length=256), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('order')
    op.drop_index(op.f('ix_product_shop_product_code'), table_name='product')
    op.drop_table('product')
    # ### end Alembic commands ###
