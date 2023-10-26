import datetime
from dataclasses import dataclass
from typing import Any


@dataclass
class DefaultConfig:
    # Task execution settings
    task_ignore_result: bool = False
    task_soft_time_limit: int | None = None

    # Task result backend settings
    result_backend: str | None = None
    result_expires: datetime.timedelta = datetime.timedelta(days=1)

    # Message Routing
    task_default_priority: int = 5
    task_default_queue: str = "celery"
    task_queue_max_priority: int = 5

    # Broker Settings
    broker_url: str = "pyamqp://guest:guest@localhost:5672//"

    # Specific
    redis_pool_size: int = 50

    def update(self, **options: Any) -> None:
        for k, v in options.items():
            setattr(self, k, v)
