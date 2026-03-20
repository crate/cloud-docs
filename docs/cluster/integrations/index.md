(cluster-integrations)=
# Integrations

CrateDB Cloud simplifies data ingestion with fully managed integrations from
external data sources. Unlike traditional import jobs, integrations run
continuously, automatically importing new data into your CrateDB Cloud cluster
as it becomes available. This makes them ideal for real-time data
synchronization and keeping your database up to date with external systems.
Fully managed by CrateDB Cloud, integrations eliminate the need for manual
setup or maintenance of separate ETL pipelines.


```{figure} ../../_assets/img/integrations-example.png
:width: 600px
:align: center
:alt: Integration in CrateDB Cloud
```

:::{toctree}
:titlesonly:
:hidden:

MongoDB CDC <mongo-cdc>
DynamoDB CDC <dynamo-cdc>

:::

---

:::
## Key Concepts
:::

:::
### Integration
:::

An integration in CrateDB Cloud automatically imports data from an external data
source into a table within your CrateDB Cloud cluster. It uses a secure
connection to ensure data privacy and can run continuously to handle updates
in real time. You can create multiple integrations for the same data source to
support different tables or configurations.

Currently, CrateDB Cloud supports ingestion from the following data source:
- {ref}`MongoDB CDC <integrations-mongo-cdc>`
- {ref}`DynamoDB CDC <integrations-dynamo-cdc>`

More integrations are planned for future releases to expand the range of
supported data sources and use cases.

The integration automatically make field names compatible with CrateDB naming 
restrictions.

When a new data field is discovered, the integration will infer its data type.
To cast data to specific types, simply create the column in CrateDB with the target type
and. The integration will always try to cast the data to the type defined in the 
CrateDB destination table. 

:::
### Connection
:::

A "Connection" in CrateDB Cloud associates authentication credentials with a
specific data source. This allows secure access to the external system and is
reusable across multiple integrations. By setting up a connection once, you can
streamline the process of creating and managing integrations without having to
re-enter credentials for each one.

:::
### Integration types
:::

There are 3 different integration types:
- **Full load only**: Imports all your data and immediately ends after.
- **CDC only**: It indefinitely listens to CDC (Change Data Capture) events on the 
  source and applies them into your CrateDB table. Once it reaches the last CDC event 
  it waits for new events to come.
- **Full load and CDC**
  It imports all the data like the type **full load only**, but once that phase finishes
  it starts processing CDC events. If the source supports it, it will try to read CDC
  events starting from right when the import phase started. This way any data alteration
  during the import phase will be picked up and processed.
