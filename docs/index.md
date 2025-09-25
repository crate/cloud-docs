(index)=
(cloud-docs-index)=

# CrateDB Cloud

CrateDB Cloud is a fully managed, terabyte-scale, and cost-effective
analytics database that lets you run analytics over vast amounts of
data in near real time, even with complex queries.

It is an SQL database service for enterprise data warehouse workloads,
that works across clouds and scales with your data.


:::::{grid}
:padding: 0

::::{grid-item}
:class: rubric-slimmer
:columns: 6

:::{rubric} Database Features
:::
CrateDB Cloud helps you manage and analyze your data with procedures
like machine learning, geospatial analysis, and business intelligence.

CrateDB Cloud's scalable, distributed analysis engine lets you query
terabytes worth of data efficiently.

CrateDB provides a rich data model including container-, geospatial-, and
vector-data types, and capabilities for full-text search.
::::

::::{grid-item}
:class: rubric-slimmer
:columns: 6

:::{rubric} Operational Benefits
:::
CrateDB Cloud is a fully managed enterprise service, allowing you to deploy,
monitor, back up, and scale your CrateDB clusters in the cloud without the
need to do database management yourself.

With CrateDB Cloud, there's no infrastructure to set up or manage, letting you
focus on finding meaningful insights using plain SQL, and taking advantage of
flexible pricing models across on-demand and flat-rate options.
::::

:::::


:::{toctree}
:titlesonly:
:hidden:

Services <reference/services>
Import <cluster/import>
Console <cluster/console>
Automation <cluster/automation>
Integrations <cluster/integrations/index>
Export <cluster/export>
Backups <cluster/backups>
Manage Cluster <cluster/manage>
Billing <organization/billing>
Access Management <organization/access-management>
Networking & Connectivity <reference/networking>
API <organization/api>
API CLI <tutorials/deploy/croud>
How-tos <howtos/index>
Reference <reference/index>
:::


(feature)=
(features)=
(all-features)=
:::{rubric} All Features
:::

All features of CrateDB Cloud at a glance.

:::::{grid} 1 3 3 3
:margin: 4 4 0 0
:padding: 0
:gutter: 2
:class-container: compact

::::{grid-item-card} {material-outlined}`power_settings_new;2em` Functional
:class-footer: text-smaller

- [SQL Database][Database Features]
- {ref}`SQL Console <cluster-console>`
- {ref}`cluster-automation`
- {ref}`cluster-import`
- {ref}`cluster-export`
- {ref}`API <organization-api>`
- {ref}`API CLI <cluster-deployment-croud>`

+++
CrateDB Cloud includes enhanced automation and productivity features,
and a wide range of integrations with data ingestion and
visualization tools.
::::

::::{grid-item-card} {material-outlined}`assured_workload;2em` Operational
:class-footer: text-smaller

- {ref}`Management Console <cluster-manage>`
- {ref}`Automatic Backups <cluster-backups>`

- Monitoring
- [Support Plans]


- Effortless Scaling
- Zero Downtime Upgrades
- Flexible deployment: Fully managed vs. hybrid
- Cost-effectiveness
+++
CrateDB Cloud provides reliable scaling of your workloads
and deployments on your preferred infrastructure provider.
::::

::::{grid-item-card} {material-outlined}`security;2em` Security & Compliance
:class-footer: text-smaller

- [Auditing]
- [Secure, certified, and compliant]:

  [Encryption], [RBAC],
  [CCPA], [GDPR], [HIPAA], [ISO 27001], [SOC 2 Type 2]
- Marketplace Coverage:

  [AWS][AWS Marketplace], [Azure][Azure Marketplace], [GCP][GCP Marketplace]
+++
CrateDB Cloud ensures secure data management with its encryption and
authentication mechanisms, and its operational certifications.
::::

:::::



:::{rubric} Learn
:::
If you are getting started with CrateDB Cloud—or want to get more from your
subscription—we provide resources and tutorials to help.


::::{grid} 1 2 2 3
:margin: 4 4 0 0
:padding: 0
:gutter: 2

:::{grid-item-card} {octicon}`tools` Manage
:link: cloud-howtos-index
:link-type: ref
Learn how to manage your cluster.
:::

:::{grid-item-card} {octicon}`codespaces` API
:link: organization-api
:link-type: ref
Programmatic access to services.
:::

:::{grid-item-card} {octicon}`terminal` API CLI (croud)
:link: cluster-deployment-croud
:link-type: ref
Use services from the command-line.
:::

:::{grid-item-card} {octicon}`table` SQL Console
:link: cluster-console
:link-type: ref
Explore data and execute SQL queries.
:::

:::{grid-item-card} {octicon}`file-code` Import
:link: cluster-import
:link-type: ref
Import data into your CrateDB Cloud cluster.
:::

:::{grid-item-card} {octicon}`file-code` Export
:link: cluster-export
:link-type: ref
Export data from your CrateDB Cloud cluster.
:::

:::::


Learn about key database drivers and client applications for CrateDB,
such as the Admin UI, crash, psql, DataGrip, and DBeaver.
Discover how to configure these tools and explore CrateDB's compatibility
with analytics, ETL, BI, and monitoring solutions.


::::{grid} 1 2 2 3
:margin: 4 4 0 0
:gutter: 2


:::{grid-item-card} {material-outlined}`link` Connect
:link: guide:connect
:link-type: ref

How to configure your favorite client library to connect to a CrateDB cluster.
:::

:::{grid-item-card} {material-outlined}`download` Ingest
:link: guide:ingest
:link-type: ref

Learn how to get data into CrateDB in various ways.
:::

:::{grid-item-card} {material-outlined}`sync` Integrate
:link: guide:integrate
:link-type: ref

Learn about all compatible client applications, frameworks, and tools.
:::

::::


[Auditing]: https://cratedb.com/product/features/auditing
[AWS Marketplace]: https://aws.amazon.com/marketplace/pp/prodview-l7rqf2xpeaubk
[Azure Marketplace]: https://azuremarketplace.microsoft.com/en-us/marketplace/apps/crate.cratedbcloud?tab=overview
[CCPA]: https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1798.140.
[Database Features]: https://cratedb.com/docs/guide/feature/
[Encryption]: https://cratedb.com/product/features/data-encryption
[GCP Marketplace]: https://console.cloud.google.com/marketplace/product/cratedb-public/cratedb-gcp
[GDPR]: https://gdpr-info.eu/
[HIPAA]: https://en.wikipedia.org/wiki/Health_Insurance_Portability_and_Accountability_Act
[ISO 27001]: https://cratedb.com/blog/cratedb-elevates-its-security-standards-and-achieves-iso-27001-certification
[RBAC]: https://cratedb.com/product/features/authorization
[secure, certified, and compliant]: https://cratedb.com/contact/security
[SOC 2 Type 2]: https://cratedb.com/blog/soc-2-type-2-compliance
[Support Plans]: https://cratedb.com/support/support-plans


<!--
Custom styles.
TODO: Possibly upstream to crate-docs-theme.
-->
<style>
.compact ul {
  margin-top: 0;
  margin-bottom: 0;
}
</style>
