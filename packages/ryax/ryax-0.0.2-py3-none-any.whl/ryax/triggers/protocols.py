# Copyright 2022 Ryax Technologies
# Use of this trigger code is governed by a BSD-style
# license that can be found in the LICENSE file.
import abc
from enum import Enum
from typing import Any, Dict

class RyaxRunStatus(Enum):
    DONE = 1
    ERROR = 2

class RyaxTriggerProtocol(metaclass=abc.ABCMeta):
    async def create_run_error(self) -> None:
        await self.create_run({}, status=RyaxRunStatus.ERROR)

    @abc.abstractmethod
    async def create_run(
        self,
        data: dict,
        running_time: float = 0.001,
        status: RyaxRunStatus = RyaxRunStatus.DONE,
    ) -> None:
        ...

    @abc.abstractmethod
    def get_output_definitions(self) -> Dict[str, Any]:
        ...
