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

### Create a virtual environment with Python 3.11.x version

#### Python Version 3.11 Installation

- For Windows
  - Go to [Python Official Downloads](https://www.python.org/downloads/) Page (or) Click [here](https://www.python.org/ftp/python/3.11.7/python-3.11.7-amd64.exe) to download Python 3.11.7 installer directly.
  - Download 3.11.x version (x can be any number you find there)
  - Run the installer file.
  - Check tick the `Add python to PATH`.
  - During installation, make sure to select the option `Customize installation`.
  - Choose a unique installation directory for Python 3.11.x to avoid overwriting your existing Python version 3.x.x installation.
  - If Add Python to Path is `not` checked, open PATH Environment Variables and edit PATH variable by adding Python 3.11 version.

- For Linux (Open Terminal)
  - For Ubuntu
    - ```sudo apt install python3.11```
  - For Fedora
    - ```sudo dnf install python3.11```
- Verify Python Version
  - Windows
    - ```py -3.11 --version```
  - Linux
    - ```python3.11 --version```

#### Creation of Virtual Environment

- Windows
  - ```py -3.11 -m venv venv```
- Linux
  - ```python3.11 -m venv venv```
- Activating Virtual Environment
  - Windows
    - In Windows 10, Open Powershell (or) In Windows 11, Windows Terminal. 
    - ```venv\Scripts\Activate```
    - If you face any `error` with this command, it's because Microsoft disables Running Scripts by default.
    - To enable it temporarily, we run following command and try above command again.
      - ```powershell -ExecutionPolicy bypass```
  - Linux (In Terminal):
    - ```source venv/bin/activate```

#### Installing Requirements

- Check whether you can see (venv) in the terminal that gives the sign of successful virtual environment activation
- ```pip install -r requirements.txt```
- Take a moment of rest and comeback later while the requirements gets installed.

### Run the project on LocalHost

- ```uvicorn main:app --reload```
- Open [LocalHost](http://127.0.0.1:8000/) on your computer
- `Optional`: You can change the port number as per your wish.
- Now my assistant is at your hands. Ask and know about me!

### Complete CLI Commands for Linux Only.

- First go to the folder where you want to clone
- Then copy below commands in your terminal in Linux. All done.

```shell [Ubuntu]
git clone https://github.com/AjayRahul1/llm-talk-about-me-assistant.git
cd llm-talk-about-me-assistant/
sudo apt install python3.11
python3.11 --version
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```
```shell [Fedora]
git clone https://github.com/AjayRahul1/llm-talk-about-me-assistant.git
cd llm-talk-about-me-assistant/
sudo dnf install python3.11
python3.11 --version
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```