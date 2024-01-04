# my-professional-llm

- Chat about me with my assistant!
- 

## Steps to Clone, Install, `Run` the project

### Cloning the project locally

For HTTPS Method,

```sh
# Cloning the GitHub Repository
git clone https://github.com/AjayRahul1/llm-talk-about-me-assistant.git

# Going into the directory
cd llm-talk-about-me-assistant/
```

For SSH Method (Prefer this only if SSH Key was setup on your computer),

```sh
# Cloning the GitHub Repository
git clone git@github.com:AjayRahul1/llm-talk-about-me-assistant.git

# Going into the directory
cd llm-talk-about-me-assistant/
```

### For Windows

#### Create a virtual environment with Python 3.11.x version

##### Python Version 3.11 Installation

- Go to [Python Official Downloads](https://www.python.org/downloads/) Page (or) Click [here](https://www.python.org/ftp/python/3.11.7/python-3.11.7-amd64.exe) to download Python 3.11.7 installer directly.
- Download 3.11.x version (x can be any number you find there)
- Run the installer file.
- Check tick the `Add Python to PATH`.
- During installation, make sure to select the option `Customize installation`.
- Choose a unique installation directory for Python 3.11.x to avoid overwriting your existing Python version 3.x.x installation.
- If 'Add Python to Path' is `not` checked, open PATH Environment Variables and edit PATH variable by adding Python 3.11 version.

- Verify Python Version
  - ```py -3.11 --version```

##### Creation of Virtual Environment

- ```py -3.11 -m venv venv```
- Activating Virtual Environment
  - In Windows 10, Open Powershell (or) In Windows 11, Windows Terminal. 
  - ```venv\Scripts\Activate```
  - If you face any `error` with this command, it's because Microsoft disables Running Scripts by default.
  - To enable it temporarily, we run following command and try above command again.
    - ```powershell -ExecutionPolicy bypass```

##### Installing Requirements

- Check whether you can see (venv) in the terminal that gives the sign of successful virtual environment activation
- ```pip install -r requirements.txt```
- Take a moment of rest and comeback later while the requirements gets installed.

##### Run the project on LocalHost

- ```uvicorn main:app --reload```
- Open [LocalHost](http://127.0.0.1:8000/) on your computer
- `Optional`: You can change the port number as per your wish.
- Now my assistant is at your hands. Ask and know about me!

### For Linux (CLI Commands)

- First go to the folder where you want to clone using `cd your-directory-path/`
- Then copy below commands in your terminal in Linux. All done.

Ubuntu

```shell
# Installing Python 3.11.x
sudo apt install python3.11
# Verifying Python v3.11
python3.11 --version
# Create Virtual Environment with name 'venv'
python3.11 -m venv venv
# Activating Virtual Environment
source venv/bin/activate
# Installing Requirements
pip install -r requirements.txt
# Run the project on LocalHost
uvicorn main:app --reload
```

Fedora

```shell
# Installing Python 3.11.x
sudo dnf install python3.11
# Verifying Python v3.11
python3.11 --version
# Create Virtual Environment with name 'venv'
python3.11 -m venv venv
# Activating Virtual Environment
source venv/bin/activate
# Installing Requirements
pip install -r requirements.txt
# Run the project on LocalHost
uvicorn main:app --reload
```
