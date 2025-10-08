(glossary)=
# Glossary

This glossary describes the concepts in the CrateDB Cloud Console
and its documentation, the Croud CLI, and other resources related
to CrateDB Cloud. The items are presented in alphabetical order.

:::{note}
While learning about CrateDB Cloud, please also visit the {ref}`CrateDB
glossary <crate-reference:appendix-glossary>`. It describes
all terms related to the CrateDB database in general.
:::

**Table of contents**

-   [Audit log](#gloss-audit-log)
-   [Azure AD](#gloss-azure-ad)
-   [Cluster](#gloss-cluster)
-   [Console](#gloss-console)
-   [Consumer](#gloss-consumer)
-   [Croud](#gloss-croud)
-   [Cloud on Kubernetes](#gloss-cloud-on-kubernetes)
-   [Endpoint](#gloss-endpoint)
-   [Offer](#gloss-offer)
-   [Organization](#gloss-org)
-   [Product](#gloss-product)
-   [Profile](#gloss-profile)
-   [Region](#gloss-region)
-   [SaaS](#gloss-saas)
-   [Scale unit](#gloss-scale-unit)
-   [Subscription](#gloss-subscription)
-   [Subscription plan](#gloss-subscription-plan)
-   [System user](#gloss-system-user)
-   [Tier](#gloss-tier)
-   [User](#gloss-user)
-   [Versions](#gloss-version)

(gloss-audit-log)=
## Audit log

The Audit Log registers and displays all operations associated with a
particular {ref}`organization <gloss-org>`. This includes operations
on {ref}`users <gloss-user>`, on {ref}`clusters <gloss-cluster>`, and
on {ref}`consumers <gloss-consumer>`. The Audit Log can be found
in the rightmost tab of the Organization overview page in the CrateDB
Cloud {ref}`Console <gloss-console>`. Only an *organization admin* has
access to the Audit Log.

(gloss-azure-ad)=
## Azure AD

Azure AD (Active Directory) is Microsoft's authentication and sign-in
service for accessing Microsoft hosted services. CrateDB Cloud uses
AzureAD as one of the means of sign-up and authentication for its
service. For documentation on Azure AD, refer to the [Microsoft
documentation on
Azure](https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/active-directory-whatis).

(gloss-cluster)=
## Cluster

Within each {ref}`organization <gloss-org>`, an administrator can
deploy any number of {ref}`products <gloss-product>`. The main
service is the deployment of clusters, which can be done through the
CrateDB Cloud Console. A cluster is a set of at least one instance
(referred to as node) which forms a database. It is also possible (and
recommended) to deploy multi-node clusters. Then the the database is
truly distributed. Depending on the user's {ref}`subscription
plan <gloss-subscription-plan>` and scaling, each cluster will have a
certain storage capacity and can process a certain amount of ingests
and queries per second. Only actual cluster usage is billed.

A cluster has a name, a unique ID, as well as a storage and processing
capacity and a number of nodes. Note that clusters are also versioned.
For information on how to deploy a cluster, please see the [tutorial for
deploying a CrateDB Cloud cluster from
scratch](https://cratedb.com/docs/cloud/en/latest/tutorials/quick-start.html).

(gloss-console)=
## Console

The CrateDB Cloud Console is the hosted user interface for CrateDB
Cloud. It is a fully supported, easy-to-use UI which allows customers to
interact with every aspect of the CrateDB Cloud service (subject to
{ref}`user role permissions <user-roles>`.) While CrateDB
Cloud also supports a CLI for interacting with the service, we assume
use of the Console by default. Only the Console allows deployment of a
{ref}`cluster <gloss-cluster>`.

(gloss-consumer)=
## Consumer

A consumer in the sense used for CrateDB Cloud architecture and
documentation is an entity that reads event data from an IoT hub. It is
possible to use a consumer, such as Azure IoT Hub, with CrateDB Cloud:
you can store the data processed by the consumer on the Cloud
{ref}`cluster <gloss-cluster>`. For a tutorial
on how to do this, see [documentation examples](https://cratedb.com/docs/crate/howtos/en/latest/reference-architectures/cratedb-azure-iot.html).
Operations on consumers are registered in the
{ref}`Audit Log <gloss-audit-log>`.


(gloss-croud)=
## Croud

Croud is the name of the CrateDB Cloud Command-Line Interface (CLI). You
can use Croud to interact with the {ref}`organization <gloss-org>` and
{ref}`products <gloss-product>` you have access to.

Croud is intended for customers who prefer a CLI to the use of a hosted
web interface such as the CrateDB Cloud
{ref}`Console <gloss-console>`. Note however that the Console
is the default way to interact with CrateDB Cloud, and currently
clusters can only be deployed within the Console.

:::{note}
See also: Croud CLI {ref}`documentation <cluster-deployment-croud>`.
:::

(gloss-cloud-on-kubernetes)=
## CrateDB Cloud on Kubernetes

CrateDB Cloud on Kubernetes is a hybrid cloud database solution presented
by [CrateDB](https://cratedb.com/). It allows customers to deploy a Kubernetes cluster either on
their own cloud provider or their own local servers, using the database
software and maintenance support that CrateDB Cloud offers. It can be
accessed through the {ref}`CrateDB Cloud Console <gloss-console>`.

(gloss-endpoint)=
## Endpoint

An endpoint is the end or goal of a communication channel. A user or
client communicates with an endpoint via a defined method, which returns
a defined set of data. In CrateDB Cloud, different
{ref}`profiles <gloss-profile>` can be used to configure their own
associated endpoints, which a user connects to via the
{ref}`Croud <gloss-croud>` CLI. For information on how
to do this, see the {ref}`Croud configuration <cluster-deployment-croud>`.

(gloss-offer)=
## Offer

An offer or subscription offer is a Software-as-a-Service
{ref}`(SaaS) <gloss-saas>` product prepared for
consumer purchase on a subscription basis. CrateDB Cloud has an offer on
the [Microsoft Azure
Marketplace](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/crate.cratedbcloud?tab=Overview)
and on the [AWS
Marketplace](https://aws.amazon.com/marketplace/pp/B089M4B1ND).

(gloss-org)=
## Organization

Organizations represent the larger structure - for example a company -
within which CrateDB Cloud {ref}`products <gloss-product>` are deployed.
At the organization level there is always at least one organization
administrator, who can in turn add organization
members. Such organization admins and members have access to the
clusters run by the organization. One account can be a member or admin
of multiple organizations.

:::{note}
For more on user roles in CrateDB Cloud and how to manage them, see the
{ref}`reference for user roles <user-roles>`.
:::

Each organization has a name, a unique ID, and optionally an associated
email address. For information on how to create an organization, please
refer to the guide about {ref}`creating organization <create-org>`.

(gloss-product)=
## Product

A product in the sense used in CrateDB Cloud is something that uses the
Cloud service for the storage of data. It consists of either a
{ref}`consumer <gloss-consumer>` or a {ref}`cluster <gloss-cluster>` and
is run within an {ref}`organization <gloss-org>`.

(gloss-profile)=
## Profile

In CrateDB Cloud's CLI, {ref}`Croud <gloss-croud>`, profiles are sets
of configuration options. They define API {ref}`endpoints <gloss-endpoint>`
and the desired output format of interaction with those endpoints. A Croud user
can create multiple profiles and switch between them as desired.

(gloss-region)=
## Region

A region in the sense used for CrateDB Cloud is a set of data centers
(servers) grouped together on a geographic basis so as to not exceed a
certain latency. CrateDB Cloud on Kubernetes also permits the creation of
custom regions. These regions are designed to correspond to servers used
by CrateDB Cloud on Kubernetes customers locally, on which they can deploy
CrateDB Cloud clusters for use in plants and other production facilities.

(gloss-saas)=
## SaaS

SaaS stands for "Software-as-a-Service". It refers to a model where
software is provided to customers on a
{ref}`subscription <gloss-subscription>` basis,
rather than a one-off payment, and is centrally hosted. Besides the
default option of subscribing directly, CrateDB Cloud can be used as a
service through its SaaS {ref}`offer <gloss-offer>` on [Microsoft Azure
Marketplace](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/crate.cratedbcloud?tab=Overview)
and the [AWS Marketplace](https://aws.amazon.com/marketplace/pp/B089M4B1ND).

(gloss-scale-unit)=
## Scale unit

The CrateDB Cloud
{ref}`subscription plans <gloss-subscription-plan>` each come with a number
of different scale units. Each scale unit represents an (additional)
unit multiplying the specific combination of hardware capacity
that applies to that plan.

:::{note}
See also [Scale your
cluster guide](https://crate.io/docs/cloud/howtos/en/latest/reconfigure-cluster.html)
:::

(gloss-subscription)=
## Subscription

A subscription is - for the purposes of CrateDB Cloud - a container in
which the CrateDB Cloud service is created and managed. You can purchase
a CrateDB Cloud subscription by signing up at [CrateDB Cloud].
In the case of using a {ref}`SaaS <gloss-saas>` {ref}`offers <gloss-offer>` on the cloud
provider marketplaces, customers subscribe to CrateDB Cloud through that
particular cloud provider.

The billing for a particular instance of the CrateDB Cloud service is
managed per subscription. On Microsoft Azure, a given customer can have
multiple subscriptions. This can be practical in case that customer
wants to separate different instances of using the CrateDB Cloud service
into different billing accounts.

:::{note}
[Subscribe to CrateDB Cloud](https://console.cratedb.cloud)

[Subscribe via AWS
Marketplace](https://crate.io/docs/cloud/tutorials/en/latest/cluster-deployment/deploy-to-cluster-marketplace/deploy-to-cluster-aws/subscribe-aws.html)

[Subscribe via Azure
Marketplace](https://crate.io/docs/cloud/tutorials/en/latest/cluster-deployment/deploy-to-cluster-marketplace/deploy-to-cluster-azure/subscribe-azure.html)

{ref}`Services <services>`
:::

(gloss-subscription-plan)=
## Subscription plan

CrateDB Cloud's service comes with several possible subscription plans.
These plans are combinations of hardware specifications that are geared
towards particular customer use cases: from trial and development plans
to high-end production clusters. They can also be further adjusted for
different {ref}`scale units <gloss-scale-unit>` per plan.

There are multiple subscription plans available for direct
deployment, and also multiple plans and a separate contract option
through the Marketplace {ref}`offers <gloss-offer>`. For more information,
refer to the documentation on {ref}`services we offer <services>`.

:::{note}
See also:

[Subscribe to CrateDB Cloud](https://console.cratedb.cloud)

[Subscribe via AWS
Marketplace](https://crate.io/docs/cloud/tutorials/en/latest/cluster-deployment/deploy-to-cluster-marketplace/deploy-to-cluster-aws/subscribe-aws.html)

[Subscribe via Azure
Marketplace](https://crate.io/docs/cloud/tutorials/en/latest/cluster-deployment/deploy-to-cluster-marketplace/deploy-to-cluster-azure/subscribe-azure.html)

:::

(gloss-system-user)=
## System user

In CrateDB Cloud, there are two distinct system
{ref}`users <gloss-user>`:

-   One is the "SYSTEM" user in the
    {ref}`Audit Log <gloss-audit-log>`. This is
    an internal user that logs the results of (attempted) {ref}`scaling
    <gloss-scale-unit>` operations.
-   The other is the "system" user in the CrateDB backend. For more
    information on this second user, refer to the
    {ref}`explanation <system-user>` in the
    CrateDB Cloud reference.

(gloss-tier)=
## Tier

In the CrateDB Cloud
{ref}`services <services>` for SaaS Marketplace
subscriptions, tiers offer different magnitudes of the hardware
composition of a given plan. For a given ratio of storage capacity,
memory, and CPUs, going up in tier allows youto multiply
the hardware values for your cluster deployment without
changing the hardware ratio.

(gloss-user)=
## User

A user in CrateDB Cloud is any individual account authorized to interact
with some part of an {ref}`organization's <gloss-org>` assets. Each user has
a defined role within the organization (see documentation on {ref}`user roles
<user-roles>`) and is associated with a
specific email address.

:::{note}
See also: {ref}`User roles <user-roles>`
:::

(gloss-version)=
## Versions

CrateDB uses a semantic versioning system called
[Semver](https://semver.org/) with three levels of versioning: major
versions, minor versions, and patch versions. (Versions can also be
referred to as releases.) CrateDB clusters run on the CrateDB Cloud
service also refer to this CrateDB versioning system.

A major version of CrateDB is a release that includes significant
changes in features, performance, and/or supported operations that are
not backwards compatible with any previous version. It is indicated by
the first numeral in the versioning sequence, i.e. the 5 in 'version
5.3.4'.

A minor version of CrateDB is a release that includes substantial
changes in features, performance, and/or supported operations compared
to the previous such version. It is indicated by the second numeral in
the versioning sequence, e.g. the 3 in 'version 5.3.4'.

A patch version of CrateDB is a release that includes bug fixes and
smaller quality of life improvements compared to the previous such
version. It is indicated by the third numeral in the versioning
sequence, e.g. the 4 in 'version 5.3.4'.

:::{note}
See also: {ref}`CrateDB Release Notes <crate-reference:release_notes>`
:::
