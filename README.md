# OpenStack CLI Extension for Neutron port bindings

This plugin adds the commands ``openstack port bindings`` to the OpenStack CLI
client. It allows to list, create, delete and activate (multiple) port bindings of a Neutron port.

## Installation

Use the following command to install this extension in the same Python
virtualenv where ``python-openstackclient`` is installed.

```bash
pip install git+https://github.com/sapcc/osc-port-bindings
```

The extension should be found automatically. You can check by running
``openstack port bindings list --help``.

## Usage example

List existing port bindings
```
$ openstack port binding list dfe06949-825d-4bef-8aca-f25aa239e35f
+---------------+----------+-----------+--------+-----------------------------+-----------------------------------+
| HOST          | VIF TYPE | VNIC TYPE | STATUS | PROFILE                     | VIF DETAILS                       |
+---------------+----------+-----------+--------+-----------------------------+-----------------------------------+
| node004-bb273 | ovs      | normal    | ACTIVE | {'os_vif_delegation': True} | {'connectivity': 'l2',            |
|               |          |           |        |                             | 'port_filter': True,              |
|               |          |           |        |                             | 'ovs_hybrid_plug': False,         |
|               |          |           |        |                             | 'datapath_type': 'system',        |
|               |          |           |        |                             | 'bridge_name': 'br-int'}          |
+---------------+----------+-----------+--------+-----------------------------+-----------------------------------+
```

Add a new (PASSIVE) port binding
```
$ openstack port binding create dfe06949-825d-4bef-8aca-f25aa239e35f --host node007-bb273
+-------------+---------------------------------------------------------------------------------------------------------------------------+
| Field       | Value                                                                                                                     |
+-------------+---------------------------------------------------------------------------------------------------------------------------+
| HOST        | node007-bb273                                                                                                             |
| VIF TYPE    | ovs                                                                                                                       |
| VNIC TYPE   | normal                                                                                                                    |
| STATUS      | INACTIVE                                                                                                                  |
| PROFILE     | {}                                                                                                                        |
| VIF DETAILS | {'connectivity': 'l2', 'port_filter': True, 'ovs_hybrid_plug': False, 'datapath_type': 'system', 'bridge_name': 'br-int'} |
+-------------+---------------------------------------------------------------------------------------------------------------------------+
```

Activate the new port binding
```
$ openstack port binding activate --host node007-bb273 dfe06949-825d-4bef-8aca-f25aa239e35f
+-------------+---------------------------------------------------------------------------------------------------------------------------+
| Field       | Value                                                                                                                     |
+-------------+---------------------------------------------------------------------------------------------------------------------------+
| HOST        | node007-bb273                                                                                                             |
| VIF TYPE    | ovs                                                                                                                       |
| VNIC TYPE   | normal                                                                                                                    |
| STATUS      | ACTIVE                                                                                                                  |
| PROFILE     | {}                                                                                                                        |
| VIF DETAILS | {'connectivity': 'l2', 'port_filter': True, 'ovs_hybrid_plug': False, 'datapath_type': 'system', 'bridge_name': 'br-int'} |
+-------------+---------------------------------------------------------------------------------------------------------------------------+
```

List all port bindings
```
$ openstack port binding list dfe06949-825d-4bef-8aca-f25aa239e35f
$ +---------------+----------+-----------+----------+-----------------------------+----------------------------------+
| HOST          | VIF TYPE | VNIC TYPE | STATUS   | PROFILE                     | VIF DETAILS                      |
+---------------+----------+-----------+----------+-----------------------------+----------------------------------+
| node004-bb273 | ovs      | normal    | ACTIVE   | {'os_vif_delegation': True} | {'connectivity': 'l2',           |
|               |          |           |          |                             | 'port_filter': True,             |
|               |          |           |          |                             | 'ovs_hybrid_plug': False,        |
|               |          |           |          |                             | 'datapath_type': 'system',       |
|               |          |           |          |                             | 'bridge_name': 'br-int'}         |
| node007-bb273 | ovs      | normal    | INACTIVE | {}                          | {'connectivity': 'l2',           |
|               |          |           |          |                             | 'port_filter': True,             |
|               |          |           |          |                             | 'ovs_hybrid_plug': False,        |
|               |          |           |          |                             | 'datapath_type': 'system',       |
|               |          |           |          |                             | 'bridge_name': 'br-int'}         |
+---------------+----------+-----------+----------+-----------------------------+----------------------------------+
```

Delete the old port binding
```
$ openstack port binding delete dfe06949-825d-4bef-8aca-f25aa239e35f --host node004-bb273
```