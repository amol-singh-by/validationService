import yaml
import sys, os
import json
import logging

logging.basicConfig(filename="../logs/log.txt",
                    filemode='a',
                    format='%(asctime)s %(levelname)s-%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.DEBUG)


def load_internal_yaml_property(yaml_property: str):
    dirname = os.path.join(os.path.dirname(__file__), '../configurations/filepath.yaml')
    dirname = os.path.abspath(os.path.realpath(dirname))
    # print(dirname)

    with open(dirname, 'r') as yamlFile:
        try:
            data = yaml.load(yamlFile, Loader=yaml.FullLoader)
            dict_inbound = data
            # logging.info(dict_inbound[property])
            return dict_inbound[yaml_property]
        except yaml.YAMLError as error:
            print(error)
            logging.error(error)

def get_schema(schema_entity: str):
    """
    Gets the schema of file to be validated
    :return:
    """
    try:
        if schema_entity == "WORKFLOW":
            file_path = WORKFLOW_SCHEMA
        elif schema_entity == "TRANSFORM":
            file_path = TRANSFORM_SCHEMA
        logging.info(file_path)
        with open(file_path, 'r') as file:
            schema = json.load(file)
        return schema
    except (OSError, IOError) as error:
        print(error)

def load_json_data(file_path: str):
    try:
        if file_path == "":
            file_path = WORKFLOW_CFG_PATH

        wrkflow_file_data = open(file_path)

        data = json.load(wrkflow_file_data)
        return data
    except (OSError, IOError) as error:
        print(error)


SERVICE_DEF_PATH = load_internal_yaml_property("LPAConfigRepoPath") + \
                   load_internal_yaml_property("LPAServiceDefinitionPath")

WORKFLOW_CFG_PATH = load_internal_yaml_property("LPAConfigRepoPath") + \
                    load_internal_yaml_property("workflowconfigPath")

TRANSFORM_CFG_PATH = load_internal_yaml_property("LPAConfigRepoPath") + \
                     load_internal_yaml_property("transformconfigPath")

WORKFLOW_SCHEMA = os.path.join(os.path.dirname(__file__), '../schemaToValidate/workflowconfig_schema.json')

TRANSFORM_SCHEMA = os.path.join(os.path.dirname(__file__), '../schemaToValidate/transformconfig_schema.json')


print(get_schema("WORKFLOW"))