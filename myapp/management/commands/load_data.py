import json
from django.core.management.base import BaseCommand
from myapp.models import UserProfile, Experience, Education

class Command(BaseCommand):
    help = 'Load data into Django models'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='Path to the JSON file')

    def handle(self, *args, **options):
        json_file = options['json_file']
        with open(json_file, 'r') as file:
            data = json.load(file)

        for item in data:
            user_profile = UserProfile.objects.create(
                profile=item['profile'],
                url=item['url'],
                name=item['name'],
                description=item['description'],
                location=item['location'],
                followers=item['followers'],
                connections=item['connections'],
                about=item['about']
            )

            for exp_data in item['experience']:
                experience = Experience.objects.create(
                    organisation_profile=exp_data['organisation_profile'],
                    location=exp_data['location'],
                    description=exp_data['description'],
                    # start_time=exp_data['start_time'],
                    # end_time=exp_data['end_time'],
                    # duration=exp_data['duration']
                )
                user_profile.experience.add(experience)

            for edu_data in item['education']:
                education = Education.objects.create(
                    organisation=edu_data['organisation'],
                    organisation_profile=edu_data['organisation_profile'],
                    course_details=edu_data['course_details'],
                    description=edu_data['description'],
                    # start_time=edu_data['start_time'],
                    # end_time=edu_data['end_time']
                )
                user_profile.education.add(education)

            self.stdout.write(self.style.SUCCESS('Data loaded successfully.'))