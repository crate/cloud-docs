(integrations-mongo-cdc)=
# MongoDB CDC

CrateDB Cloud enables continuous data ingestion from MongoDB using Change Data
Capture (CDC), providing real-time synchronization of your data.

## Key Concepts

The MongoDB CDC integration in CrateDB Cloud allows you to keep your data
synchronized between your MongoDB Atlas cluster and your CrateDB Cloud cluster
in real-time.

### How It Works

The integration functions in two main stages:

1. **Initial Sync:**
   The integration performs a complete scan of your MongoDB collections,
   importing all existing data into your CrateDB Cloud cluster.

2. **Continuous Sync:**
   The integration uses MongoDB Change Streams to monitor changes in your
   MongoDB collections and syncs these updates to your CrateDB Cloud cluster
   in real-time, ensuring that your data remains current.

### Data Consistency and Mode

For continuous sync, CrateDB Cloud uses MongoDB's **full document mode** to
ensure data consistency. This mode guarantees that MongoDB returns the latest
majority-committed version of the updated document.

While receiving partial deltas is more efficient, full document mode provides
robust functionality. Support for partial deltas may be added in the future to
enhance performance and flexibility.

---

## Create a new Integration
A MongoDB integration allows you to sync a single collection from a MongoDB
Atlas cluster. You can reuse an existing connection across multiple integrations
to continuously sync data from multiple MongoDB Atlas collections.

Supported authentication methods:
- MongoDB SCRAM Authentication
- MongoDB X.509 Authentication


### Set Up MongoDB Atlas Authentication

The following steps should be performed in the MongoDB Atlas UI.

:::::{stepper}
#### Create a Custom Role
1. **Navigate to Database Access**
   Go to **Database Access** in the MongoDB Atlas UI for the cluster you want to
   connect to CrateDB Cloud.

2. **Add a Custom Role**
   Under **Custom Roles**, click **Add New Custom Role**. A form will appear.

3. Fill in the Custom Role Name - For example, use CrateDB CDC integration.

4. **Set Up Read-Only Access**
   Assign the following actions or roles to the custom role:
   - `find`, to be found under Collection Actions/Query and Write Actions
   - `changeStream`, to be found under Collection Actions/Change Stream Actions
   - `collStats`, to be found under Collection Actions/Diagnostic Actions

   Specify the databases and collections for these actions. You can update
   access permissions in the MongoDB Atlas UI later if needed.


#### Create a User

Depending on whether you plan to use SCRAM or X.509 authentication, create a
database user with one of the following methods:

:::{tab} SCRAM Auhentication

1. **Navigate to Database Access**
   In the MongoDB Atlas UI, go to **Database Access** and click **Add New
   Database User**.

2. **Set Authentication Method**
   Choose **Password** as the authentication method and enter a username and
   password for the database user.

3. **Assign the Role**
   Under **Database User Privileges**, select the custom role created in Step 1.

4. **Copy User Credentials**
   Click **Add User**, and make sure to record the username and password. These
   credentials will be used later in the CrateDB Cloud Console.
:::

:::{tab} x.509 Authentication

1. **Navigate to Database Access**
   In the MongoDB Atlas UI, go to **Database Access** and click **Add New
   Database User**.

2. **Set Authentication Method**
   Choose **Certificate** as the authentication method.

3. **Assign the Role**
   Under **Database User Privileges**, select the custom role created in Step 1.

4. **Save the Certificate**
   Click **Add User**, and store the certificate securely. This will be required
   later in the CrateDB Cloud Console.
:::


#### Configure IP Access

To allow CrateDB Cloud to access your MongoDB Atlas cluster, you must add the
CrateDB Cloud IP addresses to the IP Access List in MongoDB Atlas.

1. **Navigate to Network Access**
   In the MongoDB Atlas UI, go to **Network Access** from the left navigation.

2. **Add IP Address**
   Click **Add IP Address** and choose an IP address or range to allow access.
   For testing purposes, you can select **Allow Access from Anywhere**, but for
   production, it is recommended to specify only the required IPs. The form will show you the specific IP addresses you need to allow.

:::{note}
To set up a PrivateLink connection for the Mongo CDC integration, please reach
out to our support team.
:::


#### Access Connection String

You'll need to provide the connection string for your MongoDB Atlas cluster so
that CrateDB Cloud can connect to it.

1. **Navigate to Your Cluster**
   In the MongoDB Atlas UI, navigate to the cluster you want to connect to CrateDB Cloud.

2. **Click "Connect"**
   From the cluster view, click on **Connect**.

3. **Select "Connect Your Application"**
   Choose **Connect your application** as the connection method.

4. **Copy the Connection String**
   Copy the connection string provided in the MongoDB Atlas UI. It will look like this:

```
mongodb+srv://:@/?retryWrites=true&w=majority
```

---

:::{note}
If you are using X.509 authentication, the connection string will look slightly
different and will not include a username and password. Instead, it will
reference the certificate file:

```
mongodb+srv:///?authMechanism=MONGODB-X509&retryWrites=true&w=majority
```

Make sure to upload the X.509 certificate file when configuring the connection
in CrateDB Cloud.
:::
:::::

### Set Up Integration in CrateDB Cloud

Follow these steps in the CrateDB Cloud Console to set up the MongoDB CDC integration:

:::::{stepper}
#### Create an Integration
1. Navigate to the **Import** section in the CrateDB Cloud Console.
2. Click **Create Integration** and select **MongoDB** as the source type.

#### Configure Connection
1. Choose **Create New Connection** or select an existing one.
2. Fill in the following details:
   :::{tab} SCRAM Authentication
   - **Connection Name**: Provide a unique name for the connection.
   - **Connection String**: Paste the connection string from MongoDB Atlas.
   - **Username**: Enter the database username (required for SCRAM).
   - **Password**: Enter the database password (required for SCRAM).
   - **Default Database**: Specify the default database to use for this connection.
   :::
   :::{tab} X.509 Auhentication
   - **Connection Name**: Provide a unique name for the connection.
   - **Connection String**: Paste the connection string from MongoDB Atlas.
   - **Certificate**: Upload the X.509 certificate file.
   - **Default Database**: Specify the default database to use for this connection.
   :::

#### Test the Connection
Click **Test Connection** to verify CrateDB Cloud can connect to your MongoDB
Atlas cluster. Resolve any issues if the test fails.

#### Select Collection
Enter the database and collection name from your MongoDB Atlas cluster, that you
want to sync with CrateDB Cloud.

#### Select Target Table
1. Specify the target table in your CrateDB Cloud cluster where the data will be synced.
2. MongoDB records will be inserted into an object column called `document`.
3. Select the object type for the column:
   - **`dynamic`**: Allows indexing and columnar storage for faster querying.
   - **`ignored`**: Prevents type conflicts in CrateDB if your source data lacks a strict schema.

   :::{note}
   If your source data doesn't follow a strict schema, select `ignored` to avoid type conflicts.
   However, selecting `dynamic` provides faster query performance by utilizing indexes and columnar storage.
   :::

#### Configure Integration Settings
1. Enter a name for the integration.
2. Select the integration mode:
   - **Full Load Only**: Imports the data once but doesn’t sync changes.
   - **Full Load and CDC**: Imports the data and syncs changes in real-time.
   - **CDC Only**: Syncs only new changes in real-time without importing existing data.

#### Create the Integration
Click **Create Integration** to finalize the setup. CrateDB Cloud will now sync
your MongoDB data based on the selected settings.
:::::
---

### Column Name Restrictions

Column or property names containing square brackets `[]` are not supported and
are replaced with `_obkt_` and `_cbkt_` respectively. Likewise, column
names containing dots `.` are not supported and are replaced with `_dot_`.

:::{warning}
This behavior may change in future releases.
:::


### Unsupported Data Types

The following MongoDB data types are not supported in the CrateDB Cloud MongoDB
CDC integration:

- **Long Strings** exceeding 32,766 characters are replaced with a placeholder
  value.
- **Binary data types** other than UUIDs, which are converted to `TEXT` and
  **vectors**, which are converted to `ARRAY`s of numbers.
- The `Decimal128` data type is not supported and is converted to a string.
