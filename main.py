#imports
import os
from crewai import Agent
from dotenv import load_dotenv
from crewai.llm import LLM
import requests
from crewai import Crew
from agents import CVE_explainer
from task import exlpainer_task
from tools import github_exploit_search

#optional
from colorama import Fore, Style
import itertools
import threading
import time
import sys

#load environment variables, make sure to enter you api keys in the .env file
load_dotenv()

CVE_API_KEY = os.getenv("CVE_API")


#some styling - i like these
print("""
    
=================================
        AYANO v1.0
   DEVELPOED BY FAHISXD
=================================
      
""")
print(Fore.RED +"Welcome to the CVE Explainer CLI Tool!")

#simple spinner animation while the agent is working, to enhance user experience, again optional.
def spinner(stop_event):
    for char in itertools.cycle("|/-\\"):
        if stop_event.is_set():
            break
        sys.stdout.write(Fore.YELLOW + f"\rAnalyzing... {char}" + Style.RESET_ALL)
        sys.stdout.flush()
        time.sleep(0.1)

stop_event = threading.Event()

t = threading.Thread(target=spinner, args=(stop_event,))

#user will enter the CVE code they want to analyze, for example CVE-2021-44228, you can test with that one, its the log4j vulnerability!
cve_id = input("Enter the CVE ID: ")

#getting the info from the NVD API, you can also use other sources if you want, just make sure to adjust the code accordingly, and also make sure to have a valid API key for the NVD API, you can get one for free from their website.
url = f"https://services.nvd.nist.gov/rest/json/cves/2.0?cveId={cve_id}"
headers = {
    "apiKey": CVE_API_KEY
}

#starting the spinner animation
t.start()
#making the API request to get the CVE details
response = requests.get(url, headers=headers)
data = response.json()

try:
    description = data["vulnerabilities"][0]["cve"]["descriptions"][0]["value"]
except:
    print("CVE not found.")

#defining the crew with the agent and task, you can add more agents and tasks if you want to expand the functionality of the tool,
#for example you can add an agent that looks for patches or mitigations for the CVE, or an agent that checks if the CVE is being actively exploited in the wild, 
# the possibilities are endless!!
explainer_crew = Crew(
    agents = [CVE_explainer],
    tasks = [exlpainer_task],
    cache=True,
    max_rpm=30,
    
)

#searching for exploits from github using the tools.py
exploits = github_exploit_search(cve_id)

result = explainer_crew.kickoff(
        inputs={
            "CVE_info": description,
            "CVE_exploits": exploits
        }
    )

#stopping the spinner animation
stop_event.set()
t.join()
print(Fore.GREEN + "\rAnalysis complete!\n")

#printing the results, if you wan you can simply print(result) without styling
print(Fore.CYAN + f"Result: {result}" + Style.RESET_ALL)

