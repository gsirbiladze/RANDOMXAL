
#from aws_cli_helper import AWSCliHelper
#aws = AWSCliHelper()

from awscli import clidriver
from collections import OrderedDict


class AWSCliHelper(object):

    def __init__(self):
        self._cli_driver = clidriver.create_clidriver()
        self._aws_help = self._cli_driver.create_help_command()

        self.service_table = self._aws_help.command_table
        self.arg_table     = self._aws_help.arg_table
        self.description   = self._aws_help.description
        self.synopsis      = self._aws_help.synopsis
        self.help_usage    = self._aws_help.help_usage

        self.__aws_service_help_catalog = OrderedDict()
        self.__generate_service_help_catalog()

        
    def __generate_service_help_catalog(self):
        """ Generate help for individual resource """
        for service in self.service_table.keys():
            self.__aws_service_help_catalog[service] = self.service_table[service].create_help_command()


    @property
    def list_services(self):
        """ Returns list of services """
        return list(self.service_table.keys())


    def get_service(self, service_name):
        """ Returns service """
        return self.__aws_service_help_catalog[service_name]


    def list_service_operations(self, service_name):
        """ Returns list of service operations """
        return list(self.get_service(service_name).command_table.keys())


    def get_service_operation(self, service_name, service_operation):
        """ Returns service operation """
        return self.get_service(service_name).command_table[service_operation]


    def list_service_operation_arguments(self, service_name, service_operation):
        """ Returns list of service operation arguments """
        return list(self.get_service(service_name).command_table[service_operation].arg_table.keys())


    def get_service_operation_argument(self, service_name, service_operation, argument_name):
        """ Returns service operation argument """
        return self.get_service_operation(service_name, service_operation).arg_table[argument_name]


    def get_service_operation_details(self, service_name, service_operation):
        """ Returns help object for service operation """
        return self.get_service_operation(service_name, service_operation).create_help_command()


    # def get_detail_service_command_arguments(self, service_name, service_command):
    #     """ Returns list of service operation arguments """
    #     ops_arg_details =  OrderedDict({ 'service'   : OrderedDict({}),
    #                                      'operation' : OrderedDict({}),
    #                                      'arguments' : OrderedDict({}) })
        
    #     service_help = self.get_service(service_name)
    #     if service_help:
    #         ops_arg_details['service']['name'] = service_help.name
    #         ops_arg_details['service']['description'] = service_help.obj.documentation
        
    #         operation = service_help.command_table.get(service_operation) 
    #         if operation:
    #             detail_operation = operation.create_help_command()       
    #             ops_arg_details['operation']['name'] = detail_operation.name
    #             ops_arg_details['operation']['description'] = detail_operation.obj.documentation

    #             for arg_key, argument in detail_operation.arg_table.items():
    #                 ops_arg_details['arguments'][arg_key] = {
    #                                                             'cli_name' : argument.cli_name,
    #                                                             'cli_type_name': argument.cli_type_name,
    #                                                             'group_name': argument.group_name or [],
    #                                                             'choices': argument.choices,
    #                                                             'required': argument.required,
    #                                                             'description': argument.documentation,
    #                                                             'synopsis': argument.synopsis
    #                                                         }
    #     return ops_arg_details
            

