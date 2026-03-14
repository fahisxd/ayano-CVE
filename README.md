# Ayano

yano is a CLI-based AI cybersecurity assistant that analyzes CVE vulnerabilities and finds related exploit references.

"exploits may benot apropiate"

Example usage:

input: CVE-2021-44228

The tool fetches CVE data, searches for public exploit repositories, and generates a concise vulnerability report.

## Features

- CVE vulnerability analysis
- GitHub exploit repository discovery
- Risk level classification
- Clean CLI-style security report(optional)
- AI-powered explanation using agents

## Installation

git clone *will edit*

```bash
cd ayano
```

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate the virtual environment:

Linux / Mac:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install crewai requests python-dotenv litellm
```


## Prerequisites

Make sure you have the following installed:

- Python 3.10+
- pip
- Git

Python libraries used:

- crewai
- requests
- python-dotenv
- litellm

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the tool from the terminal:

```bash
python3 main.py
```

fill in the CVE code

## Disclaimer

This project is intended for educational and research purposes only.  
The author is not responsible for misuse of this tool.

## Future Plans

- Target reconnaissance support
- Technology detection
- CVE matching for discovered software
- Bug bounty assistant features

## Credits

Created by Fahis.

## whoami

i am an cybersecurity nerd, basically wanna explore this amazing world!! also i am 15 year old so pls suggest imporves for my future projects

*spare typos*
