from abc import ABC, abstractmethod


class CanBeShipped(ABC):
    """Interface-style ABC: a 'must-be-able-to-do' contract, not an 'is-a'."""

    @abstractmethod
    def calculate_shipping_cost(self) -> float:
        pass
