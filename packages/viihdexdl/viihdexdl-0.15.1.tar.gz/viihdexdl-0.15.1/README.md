# ViihdexDL

A command line tool for downloading HLS streams with multiple audio and subtitle tracks (designed especially for Elisa Viihde recordings) using FFmpeg.

## Requirements
[Python 3](https://www.python.org/downloads/) and libraries [langcodes](https://pypi.org/project/langcodes/) and [Requests](https://pypi.org/project/requests/) are required.

[FFmpeg](https://www.ffmpeg.org) is needed to download streams.
## Installation
Use pip to install ViihdexDL and its dependencies.
```
pip install -U viihdexdl
```
## Usage
```
viihdexdl "URL" "FILENAME" [OPTIONS]
```
The URL must point to a HLS master playlist.

Options include:
```
-h, --help            show this help message and exit
-v, --verbose         print FFmpeg command
-c CONFIG FILE, --config CONFIG FILE
                      config file
-s, --subonly         download subtitles only
-e, --extsubs         download subtitles to external files
-a AUDIO LANGUAGES, --audio AUDIO LANGUAGES
                      audio languages, e.g. "fin, en"
-u SUBTITLES, --subtitles SUBTITLES
                      subtitle languages
-b, --begin           start live stream from the first segment
-l LIVE_START_INDEX, --live_start_index LIVE_START_INDEX
                      start live stream from segment
-r VARIANT, --variant VARIANT
                      select variant
-y, --overwrite       overwrite output files without asking
-n, --never           never overwrite existing files
```
## Settings
Download settings are defined in settings.ini which in Windows systems is located in `%APPDATA%\viihdexdl`.  Preferred languages are set using two-letter ISO 639-1 or three-letter ISO 639-2 [codes](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes).
```
audio languages:      Languages of audio tracks to be downloaded.
                      If left empty, all available tracks are downloaded.
subtitle languages:   Languages of subtitle tracks to be downloaded.
                      If left empty, all available tracks are downloaded.
default audio:        Languages of the audio tracks for which 'default' flag can be set. Preferably
                      the track with the language listed first is flagged, but if no track of that
                      language is downloaded then the second listed is checked etc.
default subtitle:     Languages of the audio tracks for which 'default' flag can be set.
visual impaired:      Language of the audio track for which 'visual impaired' flag
                      is set (only works with .mkv files).
hearing impaired:     Language of the subtitle track for which 'hearing impaired' flag
                      is set (onlyworks with .mkv files).
maximum bandwidth:    The variant with the highest bitrate below this limit (bit/s) is downloaded.
                      If left empty or set to 0, the best variant is downloaded.
file extension:       File extension of the output file. Use mkv (preferred) or mp4.
external subtitles    Download subtitles to external files.
rfc 5646 to iso 639:  Convert RFC 5646 language (e.g. nl-NL) tags to ISO 639-1/2 language codes.
iso 639:              Type of language codes to use in metadata.
                      Use alpha_2 (nl), alpha_3 (nld) or alpha_3b (dut).
ffmpeg options:       FFmpeg global and input options.
ffmpeg video codec:   FFmpeg video codec options.
ffmpeg audio codec:   FFmpeg audio codec options.
overwrite:            Overwrite output files without asking.
never overwrite:      Never overwrite existing files.
```
