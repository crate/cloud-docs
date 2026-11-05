=======================================
Installation on Red Hat and derivatives
=======================================

.. include:: prerequisites.rst

Supported platforms
--------------------

The following distributions are supported:

- Fedora
- Red Hat
- Rocky Linux

Please note only the ``amd64`` architecture is currently supported.

Installation guide
-------------------

The installation is performed via an RPM package that must be manually downloaded from a
generic repository.


.. stepper::

Download the CrateDB Enterprise Edition package
--------------------------------------------------

The installation is performed via an RPM package served from a private repository.

The first step is to fetch the repository's and package signing keys and store it in the machine:

.. code-block:: bash

   sudo curl -fsSL -u '{username}:{token}' \
   https://cratedb-ee.git.onstackit.cloud/api/packages/cratedb/rpm/repository.key \
   -o /etc/pki/rpm-gpg/RPM-GPG-KEY-cratedb-ee

   sudo curl -fsSL -u '{username}:{token}' \
   https://cratedb-ee.git.onstackit.cloud/api/packages/cratedb/generic/cloud-enterprise/0.0.10/cratedb-ee-console-0.0.10-1.x86_64.rpm.key.asc \
   -o /etc/pki/rpm-gpg/RPM-GPG-KEY-cratedb-ee-console


Next, import the downloaded keys:

.. code-block:: bash

   sudo rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-cratedb-ee
   sudo rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-cratedb-ee-console


Then, create a file named ``/etc/yum.repos.d/cratedb-ee.repo`` and add the following content:

.. code-block:: text

    [cratedb-ee]
    name=CrateDB Enterprise Edition RPM repository
    baseurl=https://cratedb-ee.git.onstackit.cloud/api/packages/cratedb/rpm
    enabled=1
    gpgcheck=1
    gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-cratedb-ee
    username={username}
    password={token}

Replace ``{username}`` and ``{token}`` with the credentials provided to you.


.. stepper::

Install CrateDB Enterprise Edition
------------------------------------

To install the downloaded package, run the following command:

.. code-block:: bash

   # on RedHat based distributions
   sudo dnf install cratedb-ee-console

   # on SUSE based distributions
   sudo zypper install cratedb-ee-console

Installing the package will also install its required dependencies, including ``podman``.

Once the installation is complete, CrateDB EE console needs to be configured before it
can be used.
During the configuration step, user input will be required.


.. include:: setup.rst
