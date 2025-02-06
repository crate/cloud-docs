(networking)=

# Networking & Connectivity  

## CrateDB Cloud IP Addresses  

This page provides the outbound IP addresses used by CrateDB Cloud across
different regions and cloud providers. These IPs should be allowlisted if you
use external services that require network access from CrateDB Cloud, 
such as:  

- **Import Jobs** (when pulling data from external sources)  
- **Managed Integrations** (e.g., MongoDB CDC)  
- **COPY FROM/TO** (e.g., AWS S3, Azure Blob Storage, Google Cloud Storage)  
- **Snapshot Repositories** (for backups to object storage)  
- **Foreign Data Wrappers** (when connecting to external databases via FDW)  

### **Outbound IP Addresses**  

:::{caution}
CrateDB Cloud **may update outbound IPs periodically** as infrastructure evolves.   
:::

| **Cloud Provider** | **Region**         | **Outbound IP(s)**                         |
|-------------------|------------------|-----------------------------------------|
| **Azure**        | West Europe (aks1.westeurope)  | `51.105.153.175/32`, `108.142.34.5/32`  |
| **Azure**        | East US 2 (aks1.eastus2)     | `52.184.241.228/32`, `52.254.31.90/32`  |
| **AWS**          | EU West 1 (eu-west-1)       | `34.255.75.224`                         |
| **AWS**          | US East 1 (us-east-1)       | `54.197.229.58`                         |
| **AWS**          | US West 2 (us-west-2)       | `54.189.16.20`                          |
| **GCP**          | US Central 1 (us-central1)  | `34.69.134.49`                          |


