import json
from django.core.management.base import BaseCommand
from django.db import models


class Command(BaseCommand):
    help = 'Generate Django model based on a JSON file'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='Path to the JSON file')

    def handle(self, *args, **options):
        json_file = options['json_file']

        with open(json_file) as file:
            data = json.load(file)

        model_name = data.get('model_name')
        fields = data.get('fields')

        if not model_name or not fields:
            self.stderr.write('Invalid JSON file')
            return

        model_code = self.generate_model_code(model_name, fields)
        self.stdout.write(model_code)

    def generate_model_code(self, model_name, fields):
        model_code = f"class {model_name}(models.Model):\n"

        for field in fields:
            field_name = field.get('name')
            field_type = field.get('type')

            if not field_name or not field_type:
                self.stderr.write('Invalid field in JSON')
                return

            field_code = f"    {field_name} = models.{field_type}()\n"
            model_code += field_code

        return model_code
