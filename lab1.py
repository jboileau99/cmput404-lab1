import requests

# Print requests version
print(requests.__version__)

# Make GET request to google
response = requests.get("https://google.com")
print(response.text)

# Make GET request to our own script and print its source code
myScript = requests.get("https://raw.githubusercontent.com/jboileau99/cmput404-lab1/c94ac82be1d79afb0c2a153b50750558f837067e/lab1.py?token=GHSAT0AAAAAAB5FBQVQCUP4Y7YVKJGDHW6GY57M4TQ")
print(myScript.text)