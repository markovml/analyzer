import os

class JobRunRequest:
    params: dict
    job_id: str

    @staticmethod
    def from_json(json_str):
        return JobRunRequest()

def get_available_tasks(params):
    return []

class JobRunner:
    @staticmethod
    def submit(tasklet):
        pass

def execute_run(job_run_request: JobRunRequest):
    available_tasks = get_available_tasks(job_run_request.params)

    for task in available_tasks:
        JobRunner.submit(task)


if __name__ == '__main__':
    run_request = os.getenv("JOB_RUN_REQUEST")
    job_run_request = JobRunRequest.from_json(run_request)
    execute_run(job_run_request=job_run_request)
