#importing requests
import requests

#the heart of the tools.py file, this will search for exploits, 
#sometimes if exploits are not there, it will show random github repos
def github_exploit_search(cve_id):

    query = f'"{cve_id}" exploit poc'
    url = f"https://api.github.com/search/repositories?q={query}"

    response = requests.get(url)
    data = response.json()

    exploits = []

    for repo in data["items"][:5]:
        exploits.append(repo["html_url"])

    return exploits

