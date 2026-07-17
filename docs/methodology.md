# Methodology

## Principle

The project does not equate unusual with wrong. Records are classified as:

- **valid**: passes hard rules; may still carry soft flags.
- **suspicious**: logically possible but unusual.
- **invalid**: violates a hard structural or business rule.

## Hard invalid rules

- pickup or drop-off timestamp missing
- drop-off before or equal to pickup
- pickup outside the selected analysis month
- trip distance below zero
- passenger count below zero
- pickup or drop-off zone outside the official TLC zone-ID range 1-265
- non-finite core monetary values

## Soft anomaly flags

- zero distance
- duration above 4 hours
- average speed above 80 mph
- fare amount below zero
- total amount below zero
- tip amount below zero
- passenger count above 6
- fare-component difference greater than $1, where comparable columns exist

## Why negative fares are flagged rather than deleted

Negative monetary records can represent reversals or corrections. They require domain review and should not be silently discarded.
