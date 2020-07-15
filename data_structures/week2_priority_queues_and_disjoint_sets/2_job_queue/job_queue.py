# python3

from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


def build_job_heap(n_workers):
    worker_heap = []
    for i in range(n_workers):
        worker_heap.append(AssignedJob(i, 0))
    return worker_heap


def get_next_worker(job_queue):
    return job_queue[0]


def left_child(i):
    return 2*i+1


def right_child(i):
    return 2*i+2


def sift_down(job_queue, i):
    min = i
    left_child_idx = left_child(i)

    if left_child_idx < len(job_queue):
        left_job = job_queue[left_child_idx]
        if left_job.started_at < job_queue[min].started_at or \
                (left_job.started_at == job_queue[min].started_at and left_job.worker < job_queue[min].worker):
            min = left_child_idx

    right_child_idx = right_child(i)
    if right_child_idx < len(job_queue):
        right_job = job_queue[right_child_idx]
        if right_job.started_at < job_queue[min].started_at or \
                (right_job.started_at == job_queue[min].started_at and right_job.worker < job_queue[min].worker):
            min = right_child_idx
    if min != i:
        job_queue[i], job_queue[min] = job_queue[min], job_queue[i]
        sift_down(job_queue, min)


def sift_down_root(job_queue):
    sift_down(job_queue, 0)


def assign_worker_time(job_queue, job):
    next_job = get_next_worker(job_queue)
    job_queue[0] = AssignedJob(next_job.worker, next_job.started_at + job)


def assign_to_work(job_queue, job):
    assign_worker_time(job_queue, job)
    sift_down_root(job_queue)


def assign_jobs(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    result = []
    job_queue = build_job_heap(n_workers)
    for job in jobs:
        result.append(get_next_worker(job_queue))
        assign_to_work(job_queue, job)
    return result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
