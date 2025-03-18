"""Create content management tables

Revision ID: content_management_tables
Revises: 
Create Date: 2025-03-17 15:30:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'content_management_tables'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Create the content_type enum
    content_type_enum = postgresql.ENUM('text', 'html', 'markdown', 'file', name='contenttype')
    content_type_enum.create(op.get_bind())
    
    # Create the content_status enum
    content_status_enum = postgresql.ENUM('draft', 'published', 'archived', name='contentstatus')
    content_status_enum.create(op.get_bind())
    
    # Create content table
    op.create_table(
        'content',
        sa.Column('id', sa.Integer(), primary_key=True, index=True),
        sa.Column('title', sa.String(length=255), nullable=False, index=True),
        sa.Column('description', sa.String(length=1000), nullable=True),
        sa.Column('body', sa.Text(), nullable=True),
        sa.Column('content_type', content_type_enum, nullable=False),
        sa.Column('status', content_status_enum, nullable=False, server_default='draft'),
        sa.Column('created_by', sa.Integer(), sa.ForeignKey('user.id'), nullable=False),
        sa.Column('updated_by', sa.Integer(), sa.ForeignKey('user.id'), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), onupdate=sa.text('now()'), nullable=False),
    )
    
    # Create content_file table
    op.create_table(
        'content_file',
        sa.Column('id', sa.Integer(), primary_key=True, index=True),
        sa.Column('content_id', sa.Integer(), sa.ForeignKey('content.id', ondelete='CASCADE'), nullable=False),
        sa.Column('filename', sa.String(length=255), nullable=False),
        sa.Column('file_path', sa.String(length=1000), nullable=False),
        sa.Column('file_size', sa.BigInteger(), nullable=False),
        sa.Column('mime_type', sa.String(length=127), nullable=False),
        sa.Column('uploaded_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.Column('uploaded_by', sa.Integer(), sa.ForeignKey('user.id'), nullable=False),
    )
    
    # Create content_permission table
    op.create_table(
        'content_permission',
        sa.Column('id', sa.Integer(), primary_key=True, index=True),
        sa.Column('content_id', sa.Integer(), sa.ForeignKey('content.id', ondelete='CASCADE'), nullable=False),
        # Using string for role to avoid enum dependency issues
        sa.Column('role', sa.String(length=50), nullable=False),
        sa.Column('can_view', sa.Boolean(), default=False, nullable=False),
        sa.Column('can_edit', sa.Boolean(), default=False, nullable=False),
        sa.Column('can_delete', sa.Boolean(), default=False, nullable=False),
        sa.UniqueConstraint('content_id', 'role', name='uq_content_role'),
    )
    
    # Create indexes
    op.create_index(op.f('ix_content_title'), 'content', ['title'], unique=False)
    op.create_index(op.f('ix_content_file_content_id'), 'content_file', ['content_id'], unique=False)
    op.create_index(op.f('ix_content_permission_content_id'), 'content_permission', ['content_id'], unique=False)
    op.create_index(op.f('ix_content_permission_role'), 'content_permission', ['role'], unique=False)


def downgrade() -> None:
    # Drop tables
    op.drop_table('content_permission')
    op.drop_table('content_file')
    op.drop_table('content')
    
    # Drop enums
    op.execute("DROP TYPE contentstatus")
    op.execute("DROP TYPE contenttype")
