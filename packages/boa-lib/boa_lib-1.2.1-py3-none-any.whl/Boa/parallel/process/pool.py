"""
This module implements Pools of Worker processes.
"""

from os import cpu_count
from typing import ParamSpec, TypeVar

from ..abc import Pool as AbstractPool
from .primitives.workers import Worker

__all__ = ["Pool", "default_pool"]





P = ParamSpec("P")
R = TypeVar("R")

CPU_COUNT = cpu_count()
if CPU_COUNT is None:
    CPU_COUNT = 2

class Pool(AbstractPool[Worker]):

    """
    Deploys a pool of Worker processes to execute tasks.
    """

    def __init__(self, maxsize: int = CPU_COUNT, max_tasks_per_child : int | float = float("inf")) -> None:
        super().__init__(maxsize, max_tasks_per_child=max_tasks_per_child)

    @classmethod
    def _spawn(cls) -> Worker:
        from .primitives.workers import Worker
        return Worker()

default_pool = Pool()





del CPU_COUNT, cpu_count, ParamSpec, TypeVar, AbstractPool, Worker