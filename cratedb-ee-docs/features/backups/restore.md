# Restore

You can restore a snapshot that succeeded or partially succeeded. From a partial
snapshot, the incomplete parts are left out.

- **Tables**: restore the tables you select. For a table that already exists,
  you can skip it or restore it as a copy, under a new name. Existing tables are
  never overwritten.
- **Whole cluster**: restore everything the snapshot contains. Only available
  for snapshots of the whole cluster.

:::{caution}
Restoring the whole cluster:
- fails if any table of the snapshot already exists. Drop those tables first,
  or restore them one by one as copies;
- replaces users, privileges, views, user-defined functions and cluster
  settings with the ones in the snapshot. Users created after the snapshot are
  deleted. Make sure the user you log in with exists in the snapshot.
:::

Backup schedules skip their runs while a restore is in progress.
