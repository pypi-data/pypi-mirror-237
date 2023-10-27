import os, sys

from fluent import handler as fl_handler

import logging
log = logging.getLogger()

class TaskExecUtils:
    def __init__(self) -> None:
        pass


    def set_env_variables(self, event, list_task_params:list = None) -> None:
        # env variables used in the task
        env_variables = [

            # system env variables
            'fluentd_host',
            'NG_API_ENDPOINT',
            'NG_API_AUTHTOKEN',
            'TASK_NAME',
            'NG_COMPONENT_NAME',
            'NG_STATUS_GROUP_NAME',
            'EID',
            'JOBID',
            'PIPELINE_ID'
        ]

        env_variables.extend(list_task_params)

        # setting env varibales
        for var in env_variables:
            value = self.get_event_value(var, event)
            os.environ[var] = value
            log.debug(f'Value for "{var}" was passed to environment variables')

        log.info(f'All values: {env_variables} were saved as environment variables')




    def get_event_value(self, name:str, event):
        """Helper function to read the parameters values from the lambda event"""
        value = ''
        for param in event['Input']:
            if name == param['Name']:
                value = param['Value']
        return value


    def configure_logger(self, logging_lvl:str = 'DEBUG') -> fl_handler.FluentHandler:
        """Set up logger for the task
        
        Params:
            -logging_lvl: maximum logging level to trace within task execution
        Returns:
            - Fluent handler object"""
        
        available_logging_lvls = ['DEBUG', 'INFO', 'WARNING', 'ERROR']
        assert logging_lvl in available_logging_lvls, f'Logging level {logging_lvl} not recognized, use one of: {available_logging_lvls}'

        custom_format = {
            'task': 'true',
            'component': os.environ.get('TASK_NAME'),
            'e_id': os.environ.get('EID'),
            'job_id': os.environ.get('JOBID'),
            'pipeline_id': os.environ.get('PIPELINE_ID'),
            'level': '%(levelname)s',
            'time': '%(asctime)s'
        }

        formatter = fl_handler.FluentRecordFormatter(fmt=custom_format, datefmt='%Y-%m-%d %H:%M:%S,%L')
        
        flhandler = fl_handler.FluentHandler('ng.task.lambda.python38', 
                                            host=os.environ.get('fluentd_host'),
                                            port=24224, 
                                            nanosecond_precision=True)
        flhandler.setFormatter(formatter)

        logging_values_map = {'DEBUG': logging.DEBUG,
                            'INFO': logging.INFO,
                            'WARNING': logging.WARNING,
                            'ERROR': logging.ERROR}
        lvl = logging_values_map.get(logging_lvl)

        logging.basicConfig(level=lvl, force=True, handlers=[flhandler])

        return flhandler
