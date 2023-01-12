import requests

# Print requests version
print(requests.__version__)

# Make GET request to google
response = requests.get("https://google.com")
print(response.text)

# Make GET request to our own script
myScript = requests.get()