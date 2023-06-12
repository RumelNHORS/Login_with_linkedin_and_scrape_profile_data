# from django.db import models
# import json

# def generate_model_class_from_json(json_file_path, model_name):
#     with open(json_file_path) as f:
#         json_data = json.load(f)

#     fields = {}
#     for key, value in json_data.items():
#         field_type = models.CharField(max_length=255)  # Default field type
#         if isinstance(value, str):
#             field_type = models.CharField(max_length=255)
#         elif isinstance(value, int):
#             field_type = models.IntegerField()
#         elif isinstance(value, bool):
#             field_type = models.BooleanField()
#         # Add more checks for other field types as needed

#         fields[key] = field_type

#     model_class = type(model_name, (models.Model,), fields)
#     return model_class

# # Usage example
# json_file_path = 'rumel.json'
# model_name = 'DynamicModel'
# DynamicModel = generate_model_class_from_json(json_file_path, model_name)

from django.db import models

class MyModel(models.Model):
    name = models.TextField()
    field2 = models.IntegerField()
    # Add more fields as needed
