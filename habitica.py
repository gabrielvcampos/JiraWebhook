""" Print habitica tasks that are not on HARD deficulty.
API details from https://habitica.com/#/options/settings/api
API docs: https://habitica.com/apidoc/
"""

import os
import requests

HARD_PRIORITY = 2

# auth = os.environ['HABITICA_USER'], os.environ['HABITICA_TOKEN']
auth_headers = {'x-api-user': '817f9bc8-014b-40c4-a02f-f0e5621b0009', 'x-api-key': 'd88e9840-bf17-454b-bfa9-fe813b56e500'}

r = requests.get(
  'https://habitica.com/api/v3/user',
  headers=auth_headers)
assert r.status_code == 200
tags = {tag['name']: tag['id'] for tag in r.json()['data']}
tag = tags['TodoCleanup']


r = requests.get(
  'https://habitica.com/api/v3/tasks/user?type=todos',
  headers=auth_headers)
assert r.status_code == 200

# Enforce priority
for todo in r.json()['data']:
  if todo['priority'] != HARD_PRIORITY:
    print("{priority} {text}".format(**todo))

# Enforce tag
for todo in r.json()['data']:
  if tag not in todo['tags']:
    print("{text}".format(**todo))

# Set the tag on habits
tag = tags['Focus']
r = requests.get(
  'https://habitica.com/api/v3/tasks/user?type=habits',
  headers=auth_headers)
assert r.status_code == 200

for task in list(r.json()['data']):
  if tag not in task['tags']:
    print("Updating {text}".format(**task))
    r = requests.post(
      'https://habitica.com/api/v3/tasks/%s/tags/%s' % (task['id'], tag),
      headers=auth_headers)
    assert r.status_code == 200, r.json()