from typing import Optional


class NumberRange:
    def __init__(self, min_value: Optional[float] = None, max_value: Optional[float] = None):
        if min_value is not None and not isinstance(min_value, (int, float)):
            raise ValueError("min_value must be a float or integer")
        if max_value is not None and not isinstance(max_value, (int, float)):
            raise ValueError("max_value must be a float or integer")
        if min_value is not None and max_value is not None and min_value > max_value:
            raise ValueError("min_value cannot be greater than max_value")

        self.min_value = min_value
        self.max_value = max_value

    def is_in_range(self, number: float) -> bool:
        if self.min_value is not None and number < self.min_value:
            return False
        if self.max_value is not None and number > self.max_value:
            return False
        return True

    def constrain(self, number: float) -> float:
        if self.min_value is not None:
            number = max(number, self.min_value)
        if self.max_value is not None:
            number = min(number, self.max_value)

        return number

    def __repr__(self):
        return f"NumberRange({self.min_value}, {self.max_value})"
