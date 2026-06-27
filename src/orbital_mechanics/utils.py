from pint import Quantity

def require_dimension(quantity: Quantity, dimension: str, name: str = "value") -> None:
    if not quantity.check(dimension):
        raise ValueError(f"{name} must have dimension {dimension}, got {quantity.dimensionality}")
    