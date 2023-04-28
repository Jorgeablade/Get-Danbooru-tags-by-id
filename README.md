<h1 align="center" style="color:white;">Get Danbooru tags of a post by id</h1>

<div align="center">
  
  [![Status](https://img.shields.io/badge/status-OK-green?)]()
  
</div>

A super simple script to extract tags from a post on Danbooru, to be used as prompts.

## 🏁 How to clone it and run it

Clone the repository where you are gonna work
 
```bash
  git clone https://github.com/Jorgeablade/Get-Danbooru-tags-by-id.git
```

Create a new venv with python

```bash
 python3 -m venv .venv 
```

Activate de venv

```bash
 ./.venv/Scripts/Activate.ps1 # If you are in Windows
 source ./.venv/Scripts/activate # If Linux distribution
```

Install the requirements:

```bash
  pip install -r requirements.txt
```

Fill in the required fields:

  Username: Your Danbooru username.
  
  Post ID: The ID of the post from which you want to extract tags.
  
  API key: Your Danbooru API key. 
  
  To get your Danbooru API key, go to Danbooru, go to My account, and API KEY.

  And run the project
  
```bash
  py.exe main.py
```
