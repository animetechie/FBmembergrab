import requests
import csv

# Replace ACCESS_TOKEN with a valid access token
ACCESS_TOKEN = 'YOUR_ACCESS_TOKEN'

# Replace GROUP_ID with the ID of the group you want to get the members of
GROUP_ID = 'YOUR_GROUP_ID'

# Set the API endpoint URL
url = f'https://graph.facebook.com/v9.0/{GROUP_ID}/members'

# Set the parameters for the API request
params = {
    'access_token': ACCESS_TOKEN,
    'limit': 1000  # Set the limit to 1000 to get the first 1000 members of the group
}

# Initialize an empty list to store the member data
members = []

# Set a flag to indicate whether there are more members to retrieve
more_members = True

# Keep making API requests until all members have been retrieved
while more_members:
    # Make the API request
    response = requests.get(url, params=params)
    data = response.json()

    # Append the member data to the list
    members.extend(data['data'])

    # Check if there is a next page of data
    if 'paging' in data and 'next' in data['paging']:
        # Update the URL and parameters for the next request
        url = data['paging']['next']
        params = {}
    else:
        # There are no more members to retrieve, so set the flag to False
        more_members = False

# Write the member data to a CSV file
with open('members.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['name', 'id']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for member in members:
        writer.writerow({'name': member['name'], 'id': member['id']})
