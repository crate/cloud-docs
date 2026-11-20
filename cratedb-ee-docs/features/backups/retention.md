# Retention

After each successful run, the schedule deletes the snapshots it no longer needs
to keep:

- **Keep last**: the number of newest snapshots that are always kept. Required.
- **Keep all for (days)**: also keep every snapshot taken in the last days.
  Optional.
- **Keep one per day for (days)**: also keep the first snapshot of each day.
  Optional.

For example, keep last `14`, keep all for `1` day and keep one per day for `14`
days keeps every snapshot of the last day, one snapshot per day for two weeks,
and never fewer than 14 snapshots.

A schedule only deletes its own snapshots. Snapshots taken by hand or by other
schedules are never deleted.
