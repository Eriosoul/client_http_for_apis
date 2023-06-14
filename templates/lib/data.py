from dataclasses import dataclass, asdict
from typing import Optional

@dataclass
class Item:
    name: str
    price: float
    sku: str
    attributes: Optional [list[str]] = None
