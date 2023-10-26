import time
from typing import Any

from eai_commons.utils.rate_limit import section_run
from eai_commons.utils.tracker import time_spend


class TestRunSection:
    @classmethod
    @section_run(2)
    def run(cls, num_iterator: Any, name=None, sex=None, age=None):
        print(name)
        print(sex)
        print(age)
        l1 = [i + 2 for i in num_iterator]
        return tuple(l1)


def test_run_section_result_type():
    @section_run(batch_size=2, time_window_sec=1, next_batch_sec=0.3)
    def run_some_list_tasks(num_iterator: Any) -> list:
        time.sleep(0.5)
        l1 = [i + 2 for i in num_iterator]
        return l1

    @section_run(batch_size=2, time_window_sec=0)
    def run_some_tuple_tasks(num_iterator: Any, i=0) -> tuple:
        l1 = [i + 2 for i in num_iterator]
        return tuple(l1)

    @section_run(batch_size=2, time_window_sec=0)
    def run_some_no_result_tasks(num_iterator: Any) -> None:
        ...

    t1 = run_some_list_tasks((4, 5, 8, 7, 6))
    assert isinstance(t1, list)
    t2 = run_some_tuple_tasks((4, 5, 8, 7, 6))
    assert isinstance(t2, tuple)
    t3 = run_some_no_result_tasks((4, 5, 8, 7, 6))
    assert t3 is None


def test_run_section_more_args():
    @section_run(batch_size=2, time_window_sec=0)
    def run_some_tuple_tasks(num_iterator: Any, name=None, sex=None, age=None) -> tuple:
        print(name)
        print(sex)
        print(age)
        l1 = [i + 2 for i in num_iterator]
        return tuple(l1)

    r = run_some_tuple_tasks((4, 5, 8, 7, 6), "david", sex="girl", age=27)
    print(r)

    r2 = TestRunSection.run((4, 5, 8, 7, 6), "jessie", "boy", 31)
    print(r2)
