# resume-upload

## Setup
```shell
python -m venv venv
```

Active python veritural environment
Windows
```shell
.\venv\Scripts\activate.bat
```
Linux
```shell
source venv/bin/activate
```

Install dependencies
```shell
pip install -r requirements.txt
```

Download TUS binary from [tus.io](https://github.com/tus/tusd/releases/tag/v2.9.1) and Extract it to `bin/tusd.exe` for windows or `bin/tusd` for linux.


Run the server 
```shell
python app.py
```
