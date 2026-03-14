#imports again...
import os
from agents import CVE_explainer
from crewai import Task

#assigning the task, if many agents are involved later, tasks can be updated, here, there is no limit to features you can add by customizing propmt
exlpainer_task = Task(
    description="""
You are a cybersecurity vulnerability analyst.

Your task is to analyze a CVE vulnerability description from the National Vulnerability Database and produce a short, clear security analysis.

CVE description:
{CVE_info}

Exploit repositories related to this CVE:
{CVE_exploits}

Instructions:

1. Explain what the vulnerability is in simple technical language.
2. Briefly describe how attackers exploit it.
3. State the potential impact on systems.
4. Suggest the main mitigation or fix.
5. Determine the risk level: critical, high, medium, or low.

Use the exploit repositories only as supporting context to understand exploitability. Do not invent exploits that are not listed.

Output must be concise and structured like a cybersecurity CLI tool report.
Use plain text only. No markdown, no emojis, no bold or italic formatting.

Limit the explanation to 3–5 sentences maximum.
End the report with the risk level.

After the analysis, list the exploit repositories provided in the input under a section called "Known Exploit References".
""",

    expected_output="""
A short CLI-style vulnerability report explaining the CVE, exploitation method, impact, mitigation, and final risk level.
""",

    agent=CVE_explainer,
)