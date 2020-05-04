"""Initial Tables

Revision ID: db4a696fc11b
Revises: 
Create Date: 2020-05-04 20:47:09.449610

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'db4a696fc11b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # Add uuid-ossp extension if it doesn't currently exist
    op.execute("CREATE EXTENSION IF NOT EXISTS \"uuid-ossp\"")

    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('image',
    sa.Column('id', postgresql.UUID(as_uuid=True), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('image')
    # ### end Alembic commands ###
