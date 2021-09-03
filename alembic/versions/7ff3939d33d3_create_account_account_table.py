"""create account.account table

Revision ID: 7ff3939d33d3
Revises: 
Create Date: 2021-09-02 21:28:55.365065

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID, JSONB

# revision identifiers, used by Alembic.
revision = '7ff3939d33d3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.get_bind().execute(sa.sql.text('CREATE EXTENSION IF NOT EXISTS "uuid-ossp"'))
    op.create_table('account',
                    sa.Column('id', sa.Integer(), primary_key=True),
                    sa.Column('code', sa.String(), nullable=False, unique=True),
                    sa.Column('etl_running', sa.Boolean(), nullable=False, default=False),
                    sa.Column('last_successful_etl_runtime', sa.DateTime(timezone=True)),
                    sa.Column('last_successful_pis_runtime', sa.DateTime(timezone=True)),
                    sa.Column('last_successful_drs_runtime', sa.DateTime(timezone=True)),
                    sa.Column('timezone', sa.String(), nullable=False, default="US/Pacific"),
                    sa.Column('show_empty_stops', sa.Boolean(), nullable=False, default=False),
                    sa.Column('uuid',
                              UUID(),
                              nullable=False,
                              server_default=sa.text("uuid_generate_v4()")),
                    sa.Column('etl_running', sa.Boolean(), nullable=False, default=False),
                    sa.Column('routing_provider', sa.String(), nullable=False),
                    sa.Column('max_alert_grade', sa.Integer()),
                    sa.Column('allowable_minuts_late', sa.Integer()),
                    sa.Column('config', JSONB()),
                    )
    op.create_index('idx_account_code', 'account', ['code'], unique=True)

def downgrade():
    op.drop_table('account')

