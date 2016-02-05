"""empty message

Revision ID: 5534aaacefa2
Revises: None
Create Date: 2015-05-27 01:35:27.823583

"""

# revision identifiers, used by Alembic.
revision = '5534aaacefa2'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('studies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('title', sa.Unicode(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('stormpath_id', sa.Unicode(), nullable=True),
    sa.Column('email', sa.Unicode(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('datasets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('title', sa.Unicode(), nullable=True),
    sa.Column('labelled', sa.Boolean(), nullable=True),
    sa.Column('study_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['study_id'], ['studies.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_datasets_study_id'), 'datasets', ['study_id'], unique=False)
    op.create_table('study_uploads',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('filename', sa.Unicode(), nullable=True),
    sa.Column('data', sa.LargeBinary(), nullable=True),
    sa.Column('study_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['study_id'], ['studies.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_study_uploads_study_id'), 'study_uploads', ['study_id'], unique=False)
    op.create_table('study_users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('study_id', sa.Integer(), nullable=True),
    sa.Column('role', sa.Enum('labeller', 'owner', name='user_role'), nullable=True),
    sa.ForeignKeyConstraint(['study_id'], ['studies.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_study_users_study_id'), 'study_users', ['study_id'], unique=False)
    op.create_index(op.f('ix_study_users_user_id'), 'study_users', ['user_id'], unique=False)
    op.create_table('datapoints',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('unit', sa.String(length=16), nullable=True),
    sa.Column('value', sa.Float(), nullable=True),
    sa.Column('training', sa.Boolean(), nullable=True),
    sa.Column('dataset_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['dataset_id'], ['datasets.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_datapoints_dataset_id'), 'datapoints', ['dataset_id'], unique=False)
    op.create_index(op.f('ix_datapoints_timestamp'), 'datapoints', ['timestamp'], unique=False)
    op.create_table('notes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('text', sa.Unicode(), nullable=True),
    sa.Column('dataset_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['dataset_id'], ['datasets.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_notes_dataset_id'), 'notes', ['dataset_id'], unique=False)
    op.create_table('user_labels',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('datapoint_id', sa.Integer(), nullable=True),
    sa.Column('dataset_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('label', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['datapoint_id'], ['datapoints.id'], ),
    sa.ForeignKeyConstraint(['dataset_id'], ['datasets.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_labels_datapoint_id'), 'user_labels', ['datapoint_id'], unique=False)
    op.create_index(op.f('ix_user_labels_dataset_id'), 'user_labels', ['dataset_id'], unique=False)
    op.create_index(op.f('ix_user_labels_user_id'), 'user_labels', ['user_id'], unique=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_labels_user_id'), table_name='user_labels')
    op.drop_index(op.f('ix_user_labels_dataset_id'), table_name='user_labels')
    op.drop_index(op.f('ix_user_labels_datapoint_id'), table_name='user_labels')
    op.drop_table('user_labels')
    op.drop_index(op.f('ix_notes_dataset_id'), table_name='notes')
    op.drop_table('notes')
    op.drop_index(op.f('ix_datapoints_timestamp'), table_name='datapoints')
    op.drop_index(op.f('ix_datapoints_dataset_id'), table_name='datapoints')
    op.drop_table('datapoints')
    op.drop_index(op.f('ix_study_users_user_id'), table_name='study_users')
    op.drop_index(op.f('ix_study_users_study_id'), table_name='study_users')
    op.drop_table('study_users')
    op.drop_index(op.f('ix_study_uploads_study_id'), table_name='study_uploads')
    op.drop_table('study_uploads')
    op.drop_index(op.f('ix_datasets_study_id'), table_name='datasets')
    op.drop_table('datasets')
    op.drop_table('users')
    op.drop_table('studies')
    ### end Alembic commands ###
