"""control

Revision ID: 35c56f867bfa
Revises: 
Create Date: 2023-06-05 13:21:00.557461

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '35c56f867bfa'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('kogs')
    with op.batch_alter_table('detection_routes', schema=None) as batch_op:
        batch_op.alter_column('latitude',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=5),
               existing_nullable=False)
        batch_op.alter_column('longitude',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=5),
               existing_nullable=False)

    with op.batch_alter_table('detections', schema=None) as batch_op:
        batch_op.alter_column('latitude',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=5),
               existing_nullable=False)
        batch_op.alter_column('longitude',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=5),
               existing_nullable=False)

    with op.batch_alter_table('layer_coordinates', schema=None) as batch_op:
        batch_op.alter_column('latitude',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=5),
               existing_nullable=False)
        batch_op.alter_column('longitude',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=5),
               existing_nullable=False)

    with op.batch_alter_table('markers', schema=None) as batch_op:
        batch_op.alter_column('latitude',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=5),
               existing_nullable=False)
        batch_op.alter_column('longitude',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=5),
               existing_nullable=False)

    with op.batch_alter_table('media', schema=None) as batch_op:
        batch_op.alter_column('latitude',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=5),
               existing_nullable=False)
        batch_op.alter_column('longitude',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=5),
               existing_nullable=False)

    with op.batch_alter_table('media_sources', schema=None) as batch_op:
        batch_op.alter_column('latitude',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=5),
               existing_nullable=False)
        batch_op.alter_column('longitude',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=5),
               existing_nullable=False)

    with op.batch_alter_table('screen_shots', schema=None) as batch_op:
        batch_op.alter_column('latitude',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=5),
               existing_nullable=False)
        batch_op.alter_column('longitude',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=5),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('screen_shots', schema=None) as batch_op:
        batch_op.alter_column('longitude',
               existing_type=sa.Float(precision=5),
               type_=sa.REAL(),
               existing_nullable=False)
        batch_op.alter_column('latitude',
               existing_type=sa.Float(precision=5),
               type_=sa.REAL(),
               existing_nullable=False)

    with op.batch_alter_table('media_sources', schema=None) as batch_op:
        batch_op.alter_column('longitude',
               existing_type=sa.Float(precision=5),
               type_=sa.REAL(),
               existing_nullable=False)
        batch_op.alter_column('latitude',
               existing_type=sa.Float(precision=5),
               type_=sa.REAL(),
               existing_nullable=False)

    with op.batch_alter_table('media', schema=None) as batch_op:
        batch_op.alter_column('longitude',
               existing_type=sa.Float(precision=5),
               type_=sa.REAL(),
               existing_nullable=False)
        batch_op.alter_column('latitude',
               existing_type=sa.Float(precision=5),
               type_=sa.REAL(),
               existing_nullable=False)

    with op.batch_alter_table('markers', schema=None) as batch_op:
        batch_op.alter_column('longitude',
               existing_type=sa.Float(precision=5),
               type_=sa.REAL(),
               existing_nullable=False)
        batch_op.alter_column('latitude',
               existing_type=sa.Float(precision=5),
               type_=sa.REAL(),
               existing_nullable=False)

    with op.batch_alter_table('layer_coordinates', schema=None) as batch_op:
        batch_op.alter_column('longitude',
               existing_type=sa.Float(precision=5),
               type_=sa.REAL(),
               existing_nullable=False)
        batch_op.alter_column('latitude',
               existing_type=sa.Float(precision=5),
               type_=sa.REAL(),
               existing_nullable=False)

    with op.batch_alter_table('detections', schema=None) as batch_op:
        batch_op.alter_column('longitude',
               existing_type=sa.Float(precision=5),
               type_=sa.REAL(),
               existing_nullable=False)
        batch_op.alter_column('latitude',
               existing_type=sa.Float(precision=5),
               type_=sa.REAL(),
               existing_nullable=False)

    with op.batch_alter_table('detection_routes', schema=None) as batch_op:
        batch_op.alter_column('longitude',
               existing_type=sa.Float(precision=5),
               type_=sa.REAL(),
               existing_nullable=False)
        batch_op.alter_column('latitude',
               existing_type=sa.Float(precision=5),
               type_=sa.REAL(),
               existing_nullable=False)

    op.create_table('kogs',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('event_type', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('event_at', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('user_ip', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('unity_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['unity_id'], ['unities.id'], name='kogs_unity_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='kogs_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='kogs_pkey')
    )
    # ### end Alembic commands ###