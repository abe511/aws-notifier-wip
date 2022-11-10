
from abc import ABCMeta

class BaseController(metaclass=ABCMeta):
    pass

    # _slack_service 
    # _email_service 
    # _logger_service 
    # _env_repo 
    # _email_service_provider 
    # _messenger_service_provider 
    # _logger_service_provider
    
    
    
    # Create an APIController class which will inherit from BaseController 

    # APIController should  have a method called process_event  which will create a corresponding use_case instance and execute it.
from core.use_cases import BaseUseCase

class APIController(BaseController):
    def __init__(self, request_data, service_providers):
        self.request_data = request_data
        self.service_providers = service_providers
        
    def process_event(self, request_data, service_providers):
        use_case = BaseUseCase()
        # pass

    
    
# Initialize use cases and pass as a parameter request data, service providers

#     Method process_event should instantiate a use_case class giving the corresponding arguments and call the execute  method of the use case.

