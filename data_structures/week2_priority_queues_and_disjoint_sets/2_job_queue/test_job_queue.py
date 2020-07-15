import unittest
from job_queue import assign_jobs
from job_queue import AssignedJob


class MyTestCase(unittest.TestCase):

    def test_sample_1(self):
        self.assertEqual([AssignedJob(0, 0), AssignedJob(1, 0), AssignedJob(0, 1), AssignedJob(1, 2), AssignedJob(0, 4)], assign_jobs(2, [1, 2, 3, 4, 5]))

    def test_sample_2(self):
        self.assertEqual([AssignedJob(0, 0),
                          AssignedJob(1, 0),
                          AssignedJob(2, 0),
                          AssignedJob(3, 0),
                          AssignedJob(0, 1),
                          AssignedJob(1, 1),
                          AssignedJob(2, 1),
                          AssignedJob(3, 1),
                          AssignedJob(0, 2),
                          AssignedJob(1, 2),
                          AssignedJob(2, 2),
                          AssignedJob(3, 2),
                          AssignedJob(0, 3),
                          AssignedJob(1, 3),
                          AssignedJob(2, 3),
                          AssignedJob(3, 3),
                          AssignedJob(0, 4),
                          AssignedJob(1, 4),
                          AssignedJob(2, 4),
                          AssignedJob(3, 4),],
                         assign_jobs(4, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))


if __name__ == '__main__':
    unittest.main()
