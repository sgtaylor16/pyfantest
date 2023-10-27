# Check out this link
# https://stackoverflow.com/questions/67066619/python-requests-post-a-query-to-graphql-with-variables

import requests

query = """{instros{masterNumber,type}}"""

response = requests.post('http://localhost:8000',json={"query":query})

if response.status_code == 200:
    print("response : ", response.content)