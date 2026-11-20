(backups)=
# Backups

```{include} intro.md
```

## Repositories

Snapshots are stored in a snapshot repository, such as an Amazon S3 bucket, an Azure
Blob Storage container or a local file system. Add a repository in the "Repositories"
tab of the Backups page, with the settings your storage requires. The settings
of each repository type are described in
{ref}`CREATE REPOSITORY <crate-reference:sql-create-repo-types>`. The
credentials are stored by CrateDB only, not by the Console.

Removing a repository from the Console doesn't delete the snapshots stored in
it.

## Backup schedules

To add a schedule, fill in:

- **Name**: a name to recognize the schedule.
- **Repository**: the snapshot repository to store the snapshots in.
- **Schedule**: when to take a snapshot, as a
  [cron pattern](https://www.ibm.com/docs/en/db2-as-a-service?topic=task-unix-cron-format)
  in UTC. For example, `0 * * * *` takes a snapshot every hour.
- **Scope**: the whole cluster, or a list of tables.
- **Retention**: how many snapshots to keep. See Retention below.

You can pause, edit and delete a schedule at any time. Deleting a schedule
doesn't delete its snapshots.

Snapshots taken by a schedule are named after the schedule's ID and the time
the run started, in UTC.

```{include} snapshots.md
:heading-offset: 1
```

To restore a snapshot, select it in the list. See Restore below.

```{include} retention.md
:heading-offset: 1
```

```{include} restore.md
:heading-offset: 1
```

## Good to know

- Each schedule runs one snapshot at a time. If a snapshot is still running
  when the schedule is due again, that run is skipped.
- A snapshot keeps running in CrateDB even if the Console restarts. Its run
  is picked up again at the schedule's next run.
- Several schedules can take snapshots at the same time, even in the same
  repository.
- Up to 3 snapshots can run at the same time. When 3 are already running, the
  next scheduled snapshot waits and starts as soon as one of them finishes.
- Pause your schedules before upgrading CrateDB, and resume them afterwards.
