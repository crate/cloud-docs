# Snapshots

The Snapshots screen lists your cluster's snapshots, with their state, start time,
duration and failures.

A snapshot can be:

- **In progress**: the snapshot is still running.
- **Success**: every table was saved.
- **Partial**: some parts couldn't be saved. The failures show which ones. The
  snapshot can still be restored, without those parts.
- **Failed**: nothing usable was saved. The snapshot can't be restored.
