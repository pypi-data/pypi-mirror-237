"""Add skipped state to collection_job_state_summary_view

Revision ID: c39f1de47a04
Revises: 3100452fa030
Create Date: 2023-01-16 11:53:59.783836

"""
from alembic import op

from galaxy.model.migrations.util import transaction

# revision identifiers, used by Alembic.
revision = "c39f1de47a04"
down_revision = "3100452fa030"
branch_labels = None
depends_on = None

view_name = "collection_job_state_summary_view"
previous_aggregate_query = """
SELECT
    hdca_id,
    SUM(CASE WHEN state = 'new' THEN 1 ELSE 0 END) AS new,
    SUM(CASE WHEN state = 'resubmitted' THEN 1 ELSE 0 END) AS resubmitted,
    SUM(CASE WHEN state = 'waiting' THEN 1 ELSE 0 END) AS waiting,
    SUM(CASE WHEN state = 'queued' THEN 1 ELSE 0 END) AS queued,
    SUM(CASE WHEN state = 'running' THEN 1 ELSE 0 END) AS running,
    SUM(CASE WHEN state = 'ok' THEN 1 ELSE 0 END) AS ok,
    SUM(CASE WHEN state = 'error' THEN 1 ELSE 0 END) AS error,
    SUM(CASE WHEN state = 'failed' THEN 1 ELSE 0 END) AS failed,
    SUM(CASE WHEN state = 'paused' THEN 1 ELSE 0 END) AS paused,
    SUM(CASE WHEN state = 'deleted' THEN 1 ELSE 0 END) AS deleted,
    SUM(CASE WHEN state = 'deleted_new' THEN 1 ELSE 0 END) AS deleted_new,
    SUM(CASE WHEN state = 'upload' THEN 1 ELSE 0 END) AS upload,
    SUM(CASE WHEN job_id IS NOT NULL THEN 1 ELSE 0 END) AS all_jobs
FROM (
    SELECT hdca.id AS hdca_id, job.id AS job_id, job.state as state
    FROM history_dataset_collection_association hdca
    LEFT JOIN implicit_collection_jobs icj
        ON icj.id = hdca.implicit_collection_jobs_id
    LEFT JOIN implicit_collection_jobs_job_association icjja
        ON icj.id = icjja.implicit_collection_jobs_id
    LEFT JOIN job
        ON icjja.job_id = job.id

    UNION

    SELECT hdca.id AS hdca_id, job.id AS job_id, job.state AS state
    FROM history_dataset_collection_association hdca
    LEFT JOIN job
        ON hdca.job_id = job.id
) jobstates
GROUP BY jobstates.hdca_id
"""
new_aggregate_query = """
SELECT
    hdca_id,
    SUM(CASE WHEN state = 'new' THEN 1 ELSE 0 END) AS new,
    SUM(CASE WHEN state = 'resubmitted' THEN 1 ELSE 0 END) AS resubmitted,
    SUM(CASE WHEN state = 'waiting' THEN 1 ELSE 0 END) AS waiting,
    SUM(CASE WHEN state = 'queued' THEN 1 ELSE 0 END) AS queued,
    SUM(CASE WHEN state = 'running' THEN 1 ELSE 0 END) AS running,
    SUM(CASE WHEN state = 'ok' THEN 1 ELSE 0 END) AS ok,
    SUM(CASE WHEN state = 'error' THEN 1 ELSE 0 END) AS error,
    SUM(CASE WHEN state = 'failed' THEN 1 ELSE 0 END) AS failed,
    SUM(CASE WHEN state = 'paused' THEN 1 ELSE 0 END) AS paused,
    SUM(CASE WHEN state = 'skipped' THEN 1 ELSE 0 END) AS skipped,
    SUM(CASE WHEN state = 'deleted' THEN 1 ELSE 0 END) AS deleted,
    SUM(CASE WHEN state = 'deleted_new' THEN 1 ELSE 0 END) AS deleted_new,
    SUM(CASE WHEN state = 'upload' THEN 1 ELSE 0 END) AS upload,
    SUM(CASE WHEN job_id IS NOT NULL THEN 1 ELSE 0 END) AS all_jobs
FROM (
    SELECT hdca.id AS hdca_id, job.id AS job_id, job.state as state
    FROM history_dataset_collection_association hdca
    LEFT JOIN implicit_collection_jobs icj
        ON icj.id = hdca.implicit_collection_jobs_id
    LEFT JOIN implicit_collection_jobs_job_association icjja
        ON icj.id = icjja.implicit_collection_jobs_id
    LEFT JOIN job
        ON icjja.job_id = job.id

    UNION

    SELECT hdca.id AS hdca_id, job.id AS job_id, job.state AS state
    FROM history_dataset_collection_association hdca
    LEFT JOIN job
        ON hdca.job_id = job.id
) jobstates
GROUP BY jobstates.hdca_id
"""


def upgrade():
    with transaction():
        op.execute(f"DROP VIEW IF EXISTS {view_name}")
        op.execute(f"CREATE VIEW {view_name} AS {new_aggregate_query}")


def downgrade():
    with transaction():
        op.execute(f"DROP VIEW IF EXISTS {view_name}")
        op.execute(f"CREATE VIEW {view_name} AS {previous_aggregate_query}")
