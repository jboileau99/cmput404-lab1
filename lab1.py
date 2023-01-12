import requests

# Print requests version
print(requests.__version__)

# Make GET request to google
response = requests.get("https://google.com")
print(response.text)

# Make GET request to our own script
myScript = requests.get("https://github.com/jboileau99/cmput404-lab1/blob/main/lab1.py")
print(myScript.text)