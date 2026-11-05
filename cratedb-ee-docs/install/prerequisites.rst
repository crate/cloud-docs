Prerequisites
-------------

CrateDB EE console has the following requirements:

- The CrateDB cluster must be running
- The CrateDB cluster must be reachable from the machine where CrateDB EE is to be installed.
  This can be achieved either by having direct access to at least one of the CrateDB nodes or via a load balancer.
  Access via a load balancer is preferred.
  Connectivity will be established to any port via the HTTP protocol and to port 5432 via the PG protocol, the installation process will aid in the setup if needed.
- A CrateDB user that can authenticate via password from where the CrateDB EE Console will be installed. This user will be used during the setup.
- The CrateDB EE console machine must be reachable from the CrateDB nodes. Specifically, ports 9443 and 8080.
- The machine where the CrateDB EE console is to be installed must be able to reach the Internet to download the package.
- Requires being able to modify the configuration of all CrateDB nodes.
- Requires restarting all CrateDB nodes.

Preparing the CrateDB cluster for the installation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The installation requires a CrateDB user that can authenticate from the machine where the
installation will take place.

That user needs the privilege ``AL`` because it will create new users.

For more information about privileges you can read the `CrateDB privileges documentation <https://cratedb.com/docs/crate/reference/en/latest/admin/privileges.html#administration-privileges>`_.
You will need to create a user if none is available yet.

This can be done with the following SQL statement:

.. code-block:: sql

   CREATE USER <username> WITH (password = '<password>');
   GRANT AL TO <username>;

If your CrateDB configuration already has host based authentication you may need to add a new
configuration entry to be able to authenticate with the user from the target machine.
Here is an example configuration that allows:

.. code-block:: yaml

   - -Cauth.host_based.enabled=true
   - -Cssl.http.enabled=true
   - -Cauth.host_based.config.05_setup.protocol=http
   - -Cauth.host_based.config.05_setup.method=password
   - -Cauth.host_based.config.05_setup.user=<username>
