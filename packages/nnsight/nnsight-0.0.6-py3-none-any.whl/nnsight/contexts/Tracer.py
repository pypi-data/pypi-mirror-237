from __future__ import annotations

from abc import abstractmethod
from contextlib import AbstractContextManager
from typing import TYPE_CHECKING, List, Any
from ..intervention import InterventionProxy

from ..tracing.Graph import Graph

if TYPE_CHECKING:
    from ..models.AbstractModel import AbstractModel


class Tracer(AbstractContextManager):
    def __init__(
        self,
        model: "AbstractModel",
        *args,
        **kwargs,
    ) -> None:
        self.model = model

        self.args = args
        self.kwargs = kwargs

        self.graph = Graph(self.model.meta_model, proxy_class=InterventionProxy)

        self.batch_size: int = 0
        self.batched_input: List[Any] = []
        self.output = None

        self.generation_idx:int = 0

        # Modules need to know about the current Tracer to create the correct proxies.
        for name, module in self.model.meta_model.named_modules():
            module.tracer = self

    @abstractmethod
    def __enter__(self) -> Tracer:
        raise NotImplementedError()

    @abstractmethod
    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        raise NotImplementedError()
