=======================================
Installation on Debian and derivatives
=======================================

.. include:: prerequisites.rst

Supported platforms
--------------------

The following distributions are supported:

- Debian 13 Trixie
- Ubuntu 24.04 LTS and newer

Please note only the ``amd64`` architecture is currently supported.

Installation guide
-------------------

The installation is performed via a DEB package served from a private APT repository.


.. stepper::

Configure the private package repository
--------------------------------------------

The DEB package is installed from a private APT repository. Make sure ``curl`` is
available on the target machine, then configure the repository credentials and
signing key.

.. code-block:: bash

    sudo apt update
    sudo apt install curl


First, store the credentials provided to you by creating an auth file so that APT can
authenticate against the private repository:

.. code-block:: bash

   sudo install -d -m 0755 /etc/apt/auth.conf.d

Create ``/etc/apt/auth.conf.d/cratedb-ee.conf`` with the following content, replacing
``{username}`` and ``{token}`` with the credentials provided to you:

.. code-block:: text

   machine cratedb-ee.git.onstackit.cloud
   login    {username}
   password {token}

Next, fetch the repository's signing key and add the repository itself using the following
commands:

.. code-block:: bash

   sudo install -d -m 0755 /etc/apt/keyrings

   curl -fsSL --netrc-file /etc/apt/auth.conf.d/cratedb-ee.conf \
     https://cratedb-ee.git.onstackit.cloud/api/packages/cratedb/debian/repository.key \
     | sudo tee /etc/apt/keyrings/cratedb-ee.asc >/dev/null

   echo "deb [signed-by=/etc/apt/keyrings/cratedb-ee.asc] \
   https://cratedb-ee.git.onstackit.cloud/api/packages/cratedb/debian stable main" \
     | sudo tee /etc/apt/sources.list.d/cratedb-ee.list

   sudo apt update

.. stepper::

Install CrateDB Enterprise Edition
--------------------------------------

To install the package, run the following command:

.. code-block:: bash

   sudo apt install cratedb-ee-console

Installing the package will also install its required dependencies, including ``podman``.

Once the installation is complete, CrateDB EE console needs to be configured before it
can be used.
During the configuration step, user input will be required.

.. include:: setup.rst


