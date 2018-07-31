# pocketchip-speech-recognition
PocketChip by Next Thing with Speech Recognition feature and GPIOs output

Use **Google Speech-to-text API** to recognize input voice, requires a valid Google Cloud API service account:

https://developers.google.com/identity/protocols/OAuth2ServiceAccount

Add new Google service account in `keys` folder:
`keys/account.json`

Tested on PocketChip (first release) with **Marshmallow OS custom firmware** for home screen customization. 

https://github.com/o-marshmallow/PocketCHIP-pocket-home

Code written in `Python 2.7`

Execute `run.sh` command:
 
 * init pulseaudio server (kill in case of process deadlock)
 * load Google Service Account file in JSON format
 * start virtualenv in PocketChip OS Terminal
 * run python main script


## Virtual Environment

**Create a new virtualenv**
```
virtualenv venv
```


**Activate virtualenv**
```
source venv/bin/activate
```

**Install requirements**
```
pip install -r requirements.txt
```

## Configure PocketChip Home screen

After installation of Marshmallow firmware edit file `~/.pocket-home/config.json`

You can use a **custom 95x70 PNG icon** for your command launcher, add a new icon in `icons` folder and modify the name in _icon_ attribute.

Example is shown with my local script path.

```
{
  "defaultPage": "Apps",
  "pages": [
    {
      "name": "Apps",
      "items": [
[...]
        {
          "name": "Speech",
          "icon": "/home/chip/scripts/google-speech-recognition/icons/speech.png",
          "shell": "sudo /home/chip/scripts/google-speech-recognition/run.sh"
        },
[...]
```

##Install PulseAudio

PulseAudio is required to manage audio input/output interfaces and may extend application features in the future. 

**Installation**

```
apt-get install pulseaudio -y
```

**Error:** _'portaudio.h' file not found_
```
src/_portaudiomodule.c:29:10: fatal error: 'portaudio.h' file not found
  #include "portaudio.h"
           ^~~~~~~~~~~~~
  1 error generated.
  error: command 'cc' failed with exit status 1
```

**Solve:** Install portaudio development library
```
apt-get install portaudio19-dev -y
```

