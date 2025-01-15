# OpenStack CLI Extension for Neutron port bindings

This plugin adds the commands ``openstack port bindings`` to the OpenStack CLI
client. It allows to list, create, delete and activate (multiple) port bindings of a Neutron port.

## Installation

Use the following command to install this extension in the same Python
virtualenv where ``python-openstackclient`` is installed.

```bash
pip install git+https://github.com/sapcc/osc-ccloud-server-group-member-changes
```

The extension should be found automatically. You can check by running
``openstack server group add members --help``.

## Usage example

For adding/removing one or multiple servers to a server-group, you need a
server-group UUID and the UUIDs of the servers. ``openstack server group list``
and ``openstack server list`` can help you finding those, if you only have
names.

To add a server with UUID '722afc72-2451-450e-9868-2d69935054e3' to a
server-group with UUID 'a15e7b44-311c-435e-b89c-c061b82fecd7' that already
contains another server with UUID '9d7c289a-3736-4cc3-b278-27b5caba594d', you
run the following command and get the following output:
```
$ openstack server group add members a15e7b44-311c-435e-b89c-c061b82fecd7 722afc72-2451-450e-9868-2d69935054e3
+------------+----------------------------------------------------------------------------+
| Field      | Value                                                                      |
+------------+----------------------------------------------------------------------------+
| id         | a15e7b44-311c-435e-b89c-c061b82fecd7                                       |
| members    | 9d7c289a-3736-4cc3-b278-27b5caba594d, 722afc72-2451-450e-9868-2d69935054e3 |
| name       | my-server-group                                                            |
| policy     | soft-anti-affinity                                                         |
| project_id | 1234ed96bbff4a9e9bf55b52952682d9                                           |
| rules      |                                                                            |
| user_id    | a457aef43a7faa233a98b801a5117e2f539572514967754c7665bfb7328717bb           |
+------------+----------------------------------------------------------------------------+
```

It's possible to add multiple servers to the same server-group at the same time
by supplying more server UUIDs to the command.

Removing a server from a server-group works similar, e.g.
```
$ openstack server group remove members a15e7b44-311c-435e-b89c-c061b82fecd7 9d7c289a-3736-4cc3-b278-27b5caba594d
+------------+------------------------------------------------------------------+
| Field      | Value                                                            |
+------------+------------------------------------------------------------------+
| id         | a15e7b44-311c-435e-b89c-c061b82fecd7                             |
| members    | 722afc72-2451-450e-9868-2d69935054e3                             |
| name       | my-server-group                                                  |
| policy     | soft-anti-affinity                                               |
| project_id | 1234ed96bbff4a9e9bf55b52952682d9                                 |
| rules      |                                                                  |
| user_id    | a457aef43a7faa233a98b801a5117e2f539572514967754c7665bfb7328717bb |
+------------+------------------------------------------------------------------+
```