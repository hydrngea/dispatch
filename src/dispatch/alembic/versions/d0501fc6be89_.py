"""empty message

Revision ID: d0501fc6be89
Revises: e75e103693f2
Create Date: 2020-01-17 09:46:07.966965

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "d0501fc6be89"
down_revision = "e75e103693f2"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("application", sa.Column("created_at", sa.DateTime(), nullable=True))
    op.add_column("application", sa.Column("description", sa.String(), nullable=True))
    op.add_column("application", sa.Column("source", sa.String(), nullable=True))
    op.add_column("application", sa.Column("updated_at", sa.DateTime(), nullable=True))
    op.drop_column("application", "uri_source")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "application", sa.Column("uri_source", sa.VARCHAR(), autoincrement=False, nullable=True)
    )
    op.drop_column("application", "updated_at")
    op.drop_column("application", "source")
    op.drop_column("application", "description")
    op.drop_column("application", "created_at")
    # ### end Alembic commands ###
