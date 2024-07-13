## 🤩 YTDownloader. 

- This project aims to test some libraries for downloading videos.

### 👉 Version and Dependencies:
- python v3.12.0
- pytube v15.0.0
- ffmpeg v0.2.0
#

### ➡️ Installation (project):

**1 - Create the virtual environment**
```bash
python3 -m venv .venv
```
**2 - Activate the environment**
```bash
source .venv/bin/activate
```
**3 - Install dependencies**
```bash
pip install -r requirements.txt
```
#

### ➡️ Installation (local)
- The library that merges audio and video must be installed on the system for proper functionality:
```bash
sudo apt update
sudo apt install ffmpeg
```
#

### ➡️ Configuration and workaround adjustment for the pytube v15.0.0 library
- In the function:
__def **get_throttling_function_name**(js: str) -> str:__

add another parameter in **function_patterns** (after line 273)

```bash
r'\([a-z]\s*=\s*([a-zA-Z0-9$]+)(\[\d+\])\([a-z]\)'
```
#

#### 🌟 Notes::

- When inserting a list of videos to be downloaded, remember that the merging of audio and video will depends of the speed rate conversion (check the terminal).
- So... if your video is 1 hour long, it will take some time for the total download and conversion.
#

### ➡️ Usage
- Go to the main.py file at "src" folder and adds yours links that you want to download:
 **example:**
```bash
pathsList = [
  "https://youtu.be/56Lpuiq3l5Y",
	"https://youtu.be/10HuNg1wZBA"
]
```
- save the file.


__**run the main.py file with python**__
- change the directory to the "src" folder, and run:
- python3 main.py
#
