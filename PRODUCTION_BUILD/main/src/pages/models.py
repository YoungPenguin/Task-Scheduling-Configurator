from django.db import models

# Create your models here.

class Data:
    id : list
    title : list
    predecessor : list
    utilities : str 
    general_rules : str 
    default_BOOLEAN : str 
    default_duration_best_case : str 
    default_duration_worse_case : str 
    duration_rules : str 
    resources_mandatory : str 
    resources_optional : str 
    resource_rules : str 
    user_attention_necessary : str 

