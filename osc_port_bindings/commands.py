# Copyright 2024 SAP SE
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from osc_lib.command import command
from osc_lib import utils
from osc_lib.utils import columns as column_util

from openstackclient.i18n import _
from openstackclient.network.v2.port import JSONKeyValueAction
from neutronclient.osc import plugin

_attr_map = (
    ('host', 'HOST', column_util.LIST_BOTH),
    ('vif_type', 'VIF TYPE', column_util.LIST_BOTH),
    ('vnic_type', 'VNIC TYPE', column_util.LIST_BOTH),
    ('status', 'STATUS', column_util.LIST_BOTH),
    ('profile', 'PROFILE', column_util.LIST_BOTH),
    ('vif_details', 'VIF DETAILS', column_util.LIST_BOTH),
)


def _add_args(parser):
    parser.add_argument(
        'port',
        metavar="<port>",
        help=_("Port binding port (name or ID)")
    )

    return parser


class ListPortBinding(command.Lister):
    _description = _("Display port bindings")

    def get_parser(self, prog_name):
        parser = super().get_parser(prog_name)
        return _add_args(parser)

    def take_action(self, parsed_args):
        client = plugin.make_client(self.app.client_manager)
        data = client.list('bindings', client.port_bindings_path % parsed_args.port)['bindings']
        headers, columns = column_util.get_column_definitions(_attr_map, False)
        return (headers,
                (utils.get_dict_properties(
                    s, columns,
                ) for s in data))


class CreatePortBinding(command.ShowOne):
    _description = _("Create port binding")

    def get_parser(self, prog_name):
        parser = super().get_parser(prog_name)
        parser.add_argument(
            '--host',
            metavar="<host>",
            help=_("Port binding host")
        )
        parser.add_argument(
            '--vif-type',
            metavar="<vif-type>",
            help=_("Port binding VIF type")
        )
        parser.add_argument(
            '--vnic-type',
            metavar="<vnic-type>",
            help=_("Port binding VNIC type")
        )
        parser.add_argument(
            '--profile',
            metavar="<profile>",
            action=JSONKeyValueAction,
            help=_(
                "Custom data to be passed as binding:profile. Data may "
                "be passed as <key>=<value> or JSON. "
                "(repeat option to set multiple binding:profile data)"
            ),
        )
        return _add_args(parser)

    def take_action(self, parsed_args):
        client = plugin.make_client(self.app.client_manager)
        body = {}
        if parsed_args.host:
            body['host'] = parsed_args.host
        if parsed_args.vif_type:
            body['vif_type'] = parsed_args.vif_type
        if parsed_args.vnic_type:
            body['vnic_type'] = parsed_args.vnic_type
        if parsed_args.profile:
            body['profile'] = parsed_args.profile
        obj = client.post(client.port_bindings_path % parsed_args.port, body={'binding': body})['binding']
        headers, columns = column_util.get_column_definitions(_attr_map, False)
        return headers, utils.get_dict_properties(obj, columns)


class DeletePortBinding(command.Command):
    _description = _("Delete port binding")

    def get_parser(self, prog_name):
        parser = super().get_parser(prog_name)
        parser.add_argument(
            '--host',
            required=True,
            metavar="<host>",
            help=_("Host binding to delete")
        )
        return _add_args(parser)

    def take_action(self, parsed_args):
        client = plugin.make_client(self.app.client_manager)
        client.delete(client.port_binding_path % (parsed_args.port, parsed_args.host))


class ActivatePortBinding(command.ShowOne):
    _description = _("Activate port binding")

    def get_parser(self, prog_name):
        parser = super().get_parser(prog_name)
        parser.add_argument(
            '--host',
            required=True,
            metavar="<host>",
            help=_("Host binding to activate")
        )
        return _add_args(parser)

    def take_action(self, parsed_args):
        client = plugin.make_client(self.app.client_manager)
        obj = client.put(client.port_binding_path_activate % (parsed_args.port, parsed_args.host))
        headers, columns = column_util.get_column_definitions(_attr_map, False)
        return headers, utils.get_dict_properties(obj, columns)
