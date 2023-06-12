from django.shortcuts import render
from django.contrib.auth.decorators import login_required



# Create your views here.
def login(request):
    return render(request, 'login.html')

@login_required
def home(request):
    return render(request, 'home.html')


# Scrape data from linkedIn profile
import requests
from bs4 import BeautifulSoup
from django.shortcuts import redirect
from django.http import JsonResponse

# Set your LinkedIn application credentials
CLIENT_ID = '78al3a9zifmgwi'
CLIENT_SECRET = 'pCpdSH4SiItWOmw2'
#REDIRECT_URI = 'http://localhost:8000/linkedin-auth/'
REDIRECT_URI = 'http://127.0.0.1:8000/social-auth/complete/linkedin-oauth2/'



def linkedin_login(request):
    # Redirect the user to the LinkedIn authorization page
    auth_url = f'https://www.linkedin.com/oauth/v2/authorization?response_type=code&client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&state=random_state_string&scope=r_liteprofile'
    return redirect(auth_url)

def linkedin_auth(request):
    # Extract the authorization code from the request
    authorization_code = request.GET.get('code')

    # Exchange the authorization code for an access token
    token_url = 'https://www.linkedin.com/oauth/v2/accessToken'
    payload = {
        'grant_type': 'authorization_code',
        'code': authorization_code,
        'redirect_uri': REDIRECT_URI,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
    }
    response = requests.post(token_url, data=payload)

    if response.status_code == 200:
        access_token = response.json()['access_token']

        # Use the access token to fetch the user's profile data
        profile_url = 'https://api.linkedin.com/v2/me?projection=(id,firstName,lastName,profilePicture(displayImage~:playableStreams))'
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Connection': 'Keep-Alive',
            'Accept-Encoding': 'gzip, deflate, br',
            'Host': 'api.linkedin.com',
        }
        response = requests.get(profile_url, headers=headers)

        if response.status_code == 200:
            profile_data = response.json()
            # Extract the desired profile information
            first_name = profile_data['firstName']['localized']['en_US']
            last_name = profile_data['lastName']['localized']['en_US']
            picture_url = profile_data['profilePicture']['displayImage~']['elements'][0]['identifiers'][0]['identifier']
            educations = profile_data['educations']['elements']

            # Extract the education details
            education_list = []
            for education in educations:
                school_name = education.get('schoolName', '')
                degree_name = education.get('degreeName', '')
                field_of_study = education.get('fieldOfStudy', '')
                start_date = education.get('timePeriod', {}).get('startDate', {}).get('year', '')
                end_date = education.get('timePeriod', {}).get('endDate', {}).get('year', '')

                education_info = {
                    'school_name': school_name,
                    'degree_name': degree_name,
                    'field_of_study': field_of_study,
                    'start_date': start_date,
                    'end_date': end_date,
                }
                education_list.append(education_info)

            # Create a dictionary with the extracted data
            profile_data = {
                'first_name': first_name,
                'last_name': last_name,
                'picture_url': picture_url,
                'educations': education_list,
            }

            return JsonResponse(profile_data)
        else:
            return JsonResponse({'error': 'Failed to fetch LinkedIn profile data.'})
    else:
        return JsonResponse({'error': 'Failed to authenticate with LinkedIn.'})

########################


