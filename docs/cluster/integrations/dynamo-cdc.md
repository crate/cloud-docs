(integrations-dynamo-cdc)=
# DynamoDB CDC

CrateDB Cloud enables continuous data ingestion from DynamoDB using Change Data
Capture (CDC), providing real-time synchronization of your data.

## Key Concepts

The DynamoDB CDC integration in CrateDB Cloud allows you to keep your data
synchronized between a DynamoDB table and your CrateDB Cloud cluster
in real-time.

### How It Works

The integration functions in two main stages:

1. **Initial Sync:**
   The integration performs a complete scan of your DynamoDB table.

2. **Continuous Sync:**
   The integration uses a Kinesis Data Stream to read changes from your DynamoDB table.
   Please note the Kinesis Data Stream needs to be set up before you can use this stage.
   You can refer to the AWS documentation page 
   [Getting started with Kinesis Data Streams for Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/kds_gettingstarted.html)
   to complete your setup.

### Data Consistency and Mode

For continuous sync, CrateDB Cloud uses a Kinesis Data Stream. This provides full items
that are then written as either full inserts or full upserts to ensure data consistency.
Directly reading CDC events from DynamoDB is limited to 1 day of history. By using
a Kinesis Data Stream you can choose the retention policy that best suits your needs.

---

## Create a new Integration
A DynamoDB integration allows you to sync a single table from DynamoDB. You can reuse an existing Cloud secret across multiple integrations
to continuously sync data from multiple DynamoDB tables.

Supported authentication methods:
- AWS Access Key and Access secret pair.

### Optional setup for CDC
This setup is only required if you want to enable the Continuous Sync.
Please note that running a Kinesis data stream has additional costs that AWS will charge you directly.

#### Set up a Kinesis Data Stream for CDC in AWS
1. In the **AWS console**, go to **DynamoDB**.
2. Go to **Tables**.
3. Click on the table name you want to use.
4. Click on the **Exports and streams** tab.
5. On the **Amazon Kinesis data stream details** section, click the button **Turn On**.
6. Click the **Create new** button right to **Destination Kinesis data stream**.
7. Fill in the **Data stream name*. Please note you will need this name later when setting up the integration in CrateDB Cloud. 
8. Choose the capacity that best suits your needs.
8. Choose a **Maximum record size** that can hold more than two times your biggest DynamoDB table items.
9. Click the button **Create data stream**.
10. The Kinesis data stream has now been created. If you want to change its retention policy (recommended), click on the tab **Configuration**, then click on **Edit** under the **Data retention** section.
11. Select the data retention that suits you. At least 7 days is recommended. Please note the data retention period will have an impact on the cost of the Kinesis Data Stream.
12. Back to the **Stream to an Amazon Kinesis data stream** DynamoDB page, select the newly created Kinesis Stream from the list.
13. Click on **Turn on stream**.


### Set Up Integration in CrateDB Cloud

Follow these steps in the CrateDB Cloud Console to set up the DynamoDB CDC integration:

:::::{stepper}
#### Create an Integration
1. Navigate to the **Import** section in the CrateDB Cloud Console.
2. Click **Create Integration** and select **DynamoDB** as the source type.

#### Configure Connection
1. Choose **Create New Secret** or select an existing one.
2. Fill in the following details:
   :::{tab} AWS Secret
   - **Secret Name**: Provide a unique name for the secret.
   - **Access key**: The AWS access key ID that will be used. Please note this access key requires access to your DynamoDB table and, if CDC is enabled, also to the Kinesis data stream.
   - **Secret access key**: The AWS secret key.
   :::

#### Configure Integration Settings
1. Enter a name for the integration.
2. Select the integration mode:
   - **Full Load Only**: Imports the data once but doesn’t sync changes.
   - **Full Load and CDC**: Imports the data and syncs changes in real-time.
   - **CDC Only**: Syncs only new changes in real-time without importing existing data.

#### Select source
1. Enter the AWS region name the DynamoDB table is in.
2. Enter the DynamoDB table name.
3. If CDC is enabled, please also enter the Kinesis stream name.

#### Select Target Table
1. Specify the target table in your CrateDB Cloud cluster where the data will be synced.
2. DynamoDB items will be inserted into an object column called `document`.
3. Select the object type for the column:
   - **`dynamic`**: Allows indexing and columnar storage for faster querying.
   - **`ignored`**: Prevents type conflicts in CrateDB if your source data lacks a strict schema.

   :::{note}
   If your source data doesn't follow a strict schema, select `ignored` to avoid type conflicts.
   However, selecting `dynamic` provides faster query performance by utilizing indexes and columnar storage.
   :::


#### Create the Integration
Click **Start import** to finalize the setup. CrateDB Cloud will now sync
your DynamoDB data based on the selected settings.
:::::
---

### Column Name Restrictions

Column or property names containing square brackets `[]` are not supported and
are replaced with `_obkt_` and `_cbkt_` respectively. Likewise, column
names containing dots `.` are not supported and are replaced with `_dot_`.

:::{warning}
This behavior may change in future releases.
:::
