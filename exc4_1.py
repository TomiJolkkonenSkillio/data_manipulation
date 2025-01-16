import requests

# fetch info from api
response = requests.get("https://api.github.com/search/repositories?q=language:python")

if response.status_code == 200: # if status is "OK", continue
    data = response.json()
    python_repos = data.get("items", [])

    # Sort by Forks
    sorted_python_repos = sorted(python_repos, key=lambda repo: repo["forks"], reverse=True)
    # Print the data line by line in the specified format
    print("Python Repos:")
    for repo in sorted_python_repos:
        forks = repo.get("forks")
        name = repo.get("name")
        description = repo.get("description")
        print(f"Forks: {forks}. Name: {name}. Description: {description}")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}") # fetch not ok, print out error msg