from typing import Tuple, cast

import pytest
from databricks.sdk.service.jobs import BaseJob, JobSettings

from databricks_jobs.utilities import list_jobs


def test_iter_jobs(job_name: str) -> None:
    assert job_name
    jobs: Tuple[BaseJob, ...] = list_jobs()
    assert jobs
    job: BaseJob = jobs[0]
    assert (
        len(
            list_jobs(
                names=(cast(JobSettings, job.settings).name,),
            )
        )
        == 1
    )


if __name__ == "__main__":
    pytest.main()
