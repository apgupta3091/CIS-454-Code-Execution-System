import unittest
import json
from execrequest import ExecRequest

# Test cases - Python
PYTHON_0 = '{"lang":"py", "src": ""}'
PYTHON_1 = '{"lang":"py", "src": "print(1 + 1)"}'
PYTHON_2 = '{"lang":"py", "src":"print([x for x in range(10)])"}'

# Test cases - Racket
RACKET_0 = '{"lang":"rkt", "src":"#lang racket"}'
RACKET_1 = '{"lang":"rkt", "src":"#lang racket (+ 1 1)"}'

# Test class
class CodeResponseTests(unittest.TestCase):
    # Python example tests
    def test_py_0(self):
        py_0 = json.loads(PYTHON_0)
        py_0_req = ExecRequest(py_0)
        self.assertEqual(py_0_req.run_tmp_file(), '')

    def test_py_1(self):
        py_1 = json.loads(PYTHON_1)
        py_1_req = ExecRequest(py_1)
        self.assertEqual(py_1_req.run_tmp_file(), '2')

    def test_py_2(self):
        py_2 = json.loads(PYTHON_2)
        py_2_req = ExecRequest(py_2)
        self.assertEqual(py_2_req.run_tmp_file(), '[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]')

    # Racket example tests
    def test_rkt_0(self):
        rkt_0 = json.loads(RACKET_0)
        rkt_0_req = ExecRequest(rkt_0)
        self.assertEqual(rkt_0_req.run_tmp_file(), '')

    def test_rkt_1(self):
        rkt_1 = json.loads(RACKET_1)
        rkt_1_req = ExecRequest(rkt_1)
        self.assertEqual(rkt_1_req.run_tmp_file(), '2')

if __name__ == "__main__":
    unittest.main()
