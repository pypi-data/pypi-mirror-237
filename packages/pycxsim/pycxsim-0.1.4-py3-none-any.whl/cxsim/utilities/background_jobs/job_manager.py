import threading


class BackgroundThread:
    def __init__(self):
        pass


class JobManager:
    jobs = []
    has_background_tasks = False

    @classmethod
    def add_job(cls, job):
        cls.jobs.append(job)
        cls.has_background_tasks = True

    @classmethod
    def cleanup_jobs(cls):
        for job in cls.jobs:
            if not job.is_alive():
                cls.jobs.remove(job)
        if not cls.jobs:
            cls.has_background_tasks = False
