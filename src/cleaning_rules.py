
from __future__ import annotations
from dataclasses import dataclass

ZONE_MIN, ZONE_MAX = 1, 265
MAX_DURATION_MINUTES = 240.0
MAX_REASONABLE_SPEED_MPH = 80.0
FARE_RECONCILIATION_TOLERANCE = 1.0

CORE_MONEY_COLUMNS = [
    "fare_amount", "extra", "mta_tax", "tip_amount", "tolls_amount",
    "improvement_surcharge", "total_amount", "congestion_surcharge",
    "Airport_fee", "cbd_congestion_fee",
]

@dataclass(frozen=True)
class AnalysisPeriod:
    year: int = 2025
    month: int = 1

PERIOD = AnalysisPeriod()
