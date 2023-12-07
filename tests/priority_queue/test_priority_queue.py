from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    priority = PriorityQueue()
    priority.enqueue({"qtd_linhas": 7})
    priority.enqueue({"qtd_linhas": 1})
    priority.enqueue({"qtd_linhas": 6})
    priority.enqueue({"qtd_linhas": 2})
    priority.enqueue({"qtd_linhas": 5})
    priority.enqueue({"qtd_linhas": 8})
    priority.enqueue({"qtd_linhas": 3})

    assert len(priority.high_priority) == 3
    assert len(priority.regular_priority) == 4

    assert priority.high_priority.items[0]["qtd_linhas"] == 1
    assert priority.high_priority.items[1]["qtd_linhas"] == 2
    assert priority.regular_priority.items[0]["qtd_linhas"] == 7

    assert priority.dequeue() == {"qtd_linhas": 1}
    assert priority.dequeue() == {"qtd_linhas": 2}
    assert priority.dequeue() == {"qtd_linhas": 3}
    assert priority.dequeue() == {"qtd_linhas": 7}

    assert priority.search(0) == {"qtd_linhas": 6}
    assert priority.search(1) == {"qtd_linhas": 5}

    with pytest.raises(IndexError):
        priority.search(10)
