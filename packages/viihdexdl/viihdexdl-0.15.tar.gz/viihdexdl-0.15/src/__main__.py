# Copyright (c) 2021-2023 Qotscha

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import argparse
import configparser
import locale
import os
import platform
from subprocess import Popen
import requests
import langcodes
os.system('color')

def get_language(lang_code):
    lang = langcodes.Language.get(lang_code)
    return lang

def get_iso(language, to_iso = True, iso = 'alpha_3b'):
    if not to_iso and '-' in str(language):
        lcode = str(language)
    elif iso == 'alpha_2':
        lcode = language.language
    elif iso == 'alpha_3':
        lcode = langcodes.Language.get(language).to_alpha3(variant='t')
    elif iso == 'alpha_3b':
        lcode = langcodes.Language.get(language).to_alpha3(variant='b')
    return lcode

def lang_in_langs(lang, langs):
    l = False
    for x in langs:
        if lang.language == x.language:
            fields = [k for k, v in vars(x).items() if not k.startswith('_') and v is not None]
            l = True
            for f in fields:
                if lang[f] != x[f]:
                    l = False
                    break
    return l

def list_tracks(available, wanted, default_list, dl_always = False):
    dl_list = []
    defaults = []
    if wanted:
        for x in wanted:
            for y in available:
                if lang_in_langs(y, [x]):
                    dl_list.append(y)
    else:
        for x in default_list:
            for y in available:
                if lang_in_langs(y, [x]):
                    dl_list.append(y)
        dl_list += [x for x in available if not lang_in_langs(x, default_list)]

    for x in default_list:
        default_found = False
        if dl_always and not dl_list:
            for y in available:
                if lang_in_langs(y, [x]):
                    dl_list.append(y)
                    defaults.append(y)
                    default_found = True
            if default_found:
                break
        else:
            for y in dl_list:
                if lang_in_langs(y, [x]):
                    defaults.append(y)
                    default_found = True
            if default_found:
                break
    if dl_always and not dl_list:
        dl_list = [available[0]]
    return dl_list, defaults

def is_hi_sub(name):
    sub_names = ['ohjelmatekstitys', 'hard of hearing']
    for x in sub_names:
        if x in name:
            return True
    else:
        return False

def create_config(config_path):
    config = configparser.ConfigParser()
    config['Download settings'] = { 'audio languages': '',
                                    'subtitle languages': '',
                                    'default audio': '',
                                    'default subtitle': '',
                                    'visual impaired': '',
                                    'hearing impaired': '',
                                    'maximum bandwidth': '0',
                                    'file extension': 'mkv',
                                    'external subtitles': 'true',
                                    'RFC 5646 to ISO 639': 'true',
                                    'ISO 639': 'alpha_3b',
                                    'ffmpeg options': '-v error -stats',
                                    'ffmpeg video codec': 'copy',
                                    'ffmpeg audio codec': 'copy',
                                    'overwrite': 'false',
                                    'never overwrite': 'false' }
    if not os.path.exists(config_path):
        os.mkdir(config_path)
    with open(os.path.join(config_path, 'settings.ini'), 'w') as configfile:
        config.write(configfile)
    return config

def main():
    finnish = bool(locale.getlocale()[0].split('_')[0] == 'Finnish')
    # Read arguments
    parser = argparse.ArgumentParser(description='Download HLS streams.')
    parser.add_argument('url', metavar='URL', help='stream URL')
    parser.add_argument('filename', metavar='OUTPUT', help='output file')
    parser.add_argument('-v', '--verbose', help='print FFmpeg command', action='store_true')
    parser.add_argument('-c', '--config', help='config file', metavar='CONFIG FILE')
    parser.add_argument('-s', '--subonly', help='download subtitles only', action='store_true')
    parser.add_argument('-e', '--extsubs', help='download subtitles to external files', action='store_true')
    parser.add_argument('-a', '--audio', help='audio languages, e.g. \"fin, en\"', metavar='AUDIO LANGUAGES', default=None)
    parser.add_argument('-u', '--subtitles', help='subtitle languages', default=None)
    parser.add_argument('-b', '--begin', help='start live stream from the first segment', action='store_true')
    parser.add_argument('-l', '--live_start_index', help='start live stream from segment', default=None)
    parser.add_argument('-r', '--variant', help='select variant', default=None)
    parser.add_argument('-y', '--overwrite', help='overwrite output files without asking', action='store_true')
    parser.add_argument('-n', '--never', help='never overwrite existing files', action='store_true')
    # parser.add_argument('-f', '--ffmpeg_options', help='ffmpeg general and input options', default=None)
    args = parser.parse_args()

    # Load config
    if platform.system() == 'Windows':
        config_path = os.path.join(os.environ['APPDATA'], 'viihdexdl')
    if not args.config:
        if not os.path.exists(os.path.join(config_path, 'settings.ini')):
            config = create_config(config_path)
        else:
            config = configparser.ConfigParser()
            config.read(os.path.join(config_path, 'settings.ini'))
    else:
        config = configparser.ConfigParser()
        config.read(args.config)
    dl_settings = config['Download settings']

    recording_url = args.url
    filename = args.filename
    sub_only = args.subonly
    ext_subs = args.extsubs
    if dl_settings.getboolean('overwrite') or args.overwrite:
        dl_settings['ffmpeg options'] = dl_settings['ffmpeg options'] + ' ' + '-y'
    if dl_settings.getboolean('never overwrite') or args.never:
        dl_settings['ffmpeg options'] = dl_settings['ffmpeg options'] + ' ' + '-n'
    if args.begin:
        dl_settings['ffmpeg options'] = dl_settings['ffmpeg options'] + ' ' + '-live_start_index 0'
    elif args.live_start_index:
        dl_settings['ffmpeg options'] = dl_settings['ffmpeg options'] + ' ' + '-live_start_index ' + args.live_start_index

    # if args.ffmpeg_options:
        # dl_settings['ffmpeg_options'] = dl_settings['ffmpeg_options'] + ' ' + args.ffmpeg_options

    dl_settings['audio languages'] = args.audio if args.audio else dl_settings['audio languages']
    dl_settings['subtitle languages'] = args.subtitles if args.subtitles else dl_settings['subtitle languages']
    to_iso = dl_settings.getboolean('RFC 5646 to ISO 639') if 'RFC 5646 to ISO 639' in dl_settings else True
    iso = dl_settings['ISO 639'] if 'ISO 639' in dl_settings else 'alpha_3b'

    if filename.endswith('.mkv'):
        dl_settings['file extension'] = 'mkv'
        filename = filename[:-4]
    elif filename.endswith('.mp4'):
        dl_settings['file extension'] = 'mp4'
        filename = filename[:-4]

    # Download HLS master playlist
    get_playlist = requests.get(recording_url)

    # Parse playlist and create FFmpeg command
    playlist_lines = get_playlist.text.splitlines()
    recording_url = get_playlist.url
    hls_url = recording_url.rsplit('/',1)[0]
    av_audio = []
    audio_dict = {}
    audio_count = {}
    audio_metadata = ''
    av_subs = []
    sub_dict = {}
    sub_inputs = ''
    sub_mappings = ''
    sub_metadata = ' -default_mode infer_no_subs' if dl_settings['file extension'] == 'mkv' else ''
    # sub_metadata = ' -default_mode passthrough' if dl_settings['file extension'] == 'mkv' else ''
    wanted_audio = [] if not dl_settings['audio languages'] else [get_language(x.strip()) for x in dl_settings['audio languages'].split(',')]
    wanted_subs = [] if not dl_settings['subtitle languages'] else [get_language(x.strip()) for x in dl_settings['subtitle languages'].split(',')]
    default_audio_list = [] if not dl_settings['default audio'] else [get_language(x.strip()) for x in dl_settings['default audio'].split(',')]
    default_sub_list = [] if not dl_settings['default subtitle'] else [get_language(x.strip()) for x in dl_settings['default subtitle'].split(',')]
    visual_impaired = None if (not dl_settings['visual impaired'] or dl_settings['file extension'] == 'mp4') else get_language(dl_settings['visual impaired'])
    hearing_impaired = None if (not dl_settings['hearing impaired'] or dl_settings['file extension'] == 'mp4') else get_language(dl_settings['hearing impaired'])
    variant = 0
    max_bw = 0
    max_dl_bw = 0 if not dl_settings['maximum bandwidth'] else int(dl_settings['maximum bandwidth'])
    if sub_only:
        cmd = ''
        for x in playlist_lines:
            if x.startswith('#EXT-X-MEDIA:TYPE=SUBTITLES'):
                l = x.split('LANGUAGE=', 1)[1].split(',', 1)[0].strip('"')
                lang = get_language(l)
                # if lang not in av_subs:
                if not lang_in_langs(lang, av_subs):
                    sub_uri = x.rsplit('URI=', 1)[1].split(',', 1)[0].strip('"')
                    if not (sub_uri.startswith('http://') or sub_uri.startswith('https://')):
                        sub_uri = hls_url + '/' + sub_uri
                    av_subs.append(lang)
                    sub_dict[lang] = ' -i \"' + sub_uri + '\"'
        if not sub_dict:
            if finnish:
                print('Tekstityksiä ei löytynyt.')
            else:
                print('No subtitles found.')
        else:
            sub = list_tracks(av_subs, wanted_subs, default_sub_list, True)[0][0]
            complete_filename = filename + '.' + get_iso(sub, to_iso, iso) + '.srt'
            sub_cmd = 'ffmpeg ' + dl_settings['ffmpeg options'] + sub_dict[sub] + ' -c:s subrip \"' + complete_filename + '\"'
            if finnish:
                print('Aloitetaan tekstityksen \033[32m' + complete_filename + '\033[39m lataus.\n')
            else:
                print('Starting downloading subtitle \033[32m' + complete_filename + '\033[39m.\n')
            Popen(sub_cmd).wait()

    else:
        for x in playlist_lines:
            # Parse available variants
            if x.startswith('#EXT-X-STREAM-INF:'):
                bandwidth = int(x.split('BANDWIDTH=', 1)[1].split(',', 1)[0])
                if (not args.variant and (not max_dl_bw or bandwidth <= max_dl_bw) and bandwidth > max_bw) or (args.variant is not None and variant == int(args.variant)):
                    best_variant = variant
                    try:
                        audio_tracks = True
                        audio_group = x.split('AUDIO=', 1)[1].split(',', 1)[0]
                    except:
                        audio_tracks = False
                    try:
                        sub_tracks = True
                        sub_group = x.split('SUBTITLES=', 1)[1].split(',', 1)[0]
                    except:
                        sub_tracks = False
                    max_bw = bandwidth
                variant += 1
        mappings = ' -map 0:p:' + str(best_variant) + ':v'

        for x in playlist_lines:
            # Parse available audio tracks
            if audio_tracks and x.startswith('#EXT-X-MEDIA:TYPE=AUDIO') and 'GROUP-ID=' + audio_group in x:
                try:
                    l = x.split('LANGUAGE=', 1)[1].split(',', 1)[0].strip('"')
                    lang = get_language(l)
                    if not lang_in_langs(lang, av_audio):
                        av_audio.append(lang)
                        audio_dict[lang] = l
                        audio_count[lang] = 1
                    else:
                        audio_count[lang] += 1
                except:
                    pass

            # Parse available subtitle tracks
            elif sub_tracks and x.startswith('#EXT-X-MEDIA:TYPE=SUBTITLES') and 'GROUP-ID=' + sub_group in x:
                l = x.split('LANGUAGE=', 1)[1].split(',', 1)[0].strip('"')
                n = x.split('NAME=', 1)[1].split(',', 1)[0].strip('"')
                lang = get_language(l)
                sub_uri = x.rsplit('URI=', 1)[1].split(',', 1)[0].strip('"')
                if not (sub_uri.startswith('http://') or sub_uri.startswith('https://')):
                    sub_uri = hls_url + '/' + sub_uri
                if not lang_in_langs(lang, av_subs):
                    av_subs.append(lang)
                    sub_dict[lang] = [(' -i \"' + sub_uri + '\"', is_hi_sub(n), get_iso(lang, to_iso, iso))]
                else:
                    sub_dict[lang].append((' -i \"' + sub_uri + '\"', is_hi_sub(n), get_iso(lang, to_iso, iso)))

        # Create FFmpeg command
        if not av_audio:
            mappings += ' -map 0:p:' + str(best_variant) + ':a:0'
            audio_list = None
        else:
            audio_list, default_audio = list_tracks(av_audio, wanted_audio, default_audio_list, True)
            a = 0
            for i, x in enumerate(audio_list):
                mappings += ' -map 0:p:' + str(best_variant) + ':a:m:language:' + audio_dict[x]
                for j in range(audio_count[x]):
                    audio_metadata += ' -metadata:s:a:' + str(i+a) + ' language=' + get_iso(x, to_iso, iso)
                    a += 1
                a -= 1
                if x in default_audio:
                    audio_metadata += ' -disposition:a:' + str(i+a) + ' default'
                    if x == visual_impaired:
                        audio_metadata += '+visual_impaired'
                elif x == visual_impaired:
                    audio_metadata += ' -disposition:a:' + str(i+a) + ' visual_impaired'
        if av_subs:
            sub_list, default_sub = list_tracks(av_subs, wanted_subs, default_sub_list)
            if ext_subs:
                dl = {}
                dl_hi = {}
                for x in sub_list:
                    for y in sub_dict[x]:
                        if y[1]:
                            if not dl_hi.get(y[2]):
                                complete_filename = filename + '.' + y[2] + '.HI.srt'
                                dl_hi[y[2]] = 1
                            else:
                                complete_filename = filename + '.' + y[2] + '.HI.(' + str(dl_hi[y[2]]) + ')' + '.srt'
                                dl_hi[y[2]] += 1
                        else:
                            if not dl.get(y[2]):
                                complete_filename = filename + '.' + y[2] + '.srt'
                                dl[y[2]] = 1
                            else:
                                complete_filename = filename + '.' + y[2] + '.(' + str(dl[y[2]]) + ')' + '.srt'
                                dl[y[2]] += 1
                        sub_cmd = 'ffmpeg ' + dl_settings['ffmpeg options'] + y[0] + ' -c:s subrip \"' + complete_filename + '\"'
                        if finnish:
                            print('Aloitetaan tekstityksen \033[32m' + complete_filename + '\033[39m lataus.\n')
                        else:
                            print('Starting downloading subtitle \033[32m' + complete_filename + '\033[39m.\n')
                        if args.verbose:
                            print(sub_cmd)
                            print()
                        Popen(sub_cmd).wait()
                        print()
            else:
                a = 0
                for x in sub_list:
                    for y in sub_dict[x]:
                        sub_inputs += y[0]
                        sub_mappings += ' -map ' + str(a+1) + ':s'
                        sub_metadata += ' -metadata:s:s:' + str(a) + ' language=' + y[2]
                        if x in default_sub:
                            sub_metadata += ' -disposition:s:' + str(a) + ' default'
                            if y[1] or x == hearing_impaired:
                                sub_metadata += '+hearing_impaired'
                        elif y[1] or x == hearing_impaired:
                            sub_metadata += ' -disposition:s:' + str(a) + ' hearing_impaired'
                        a += 1

        if dl_settings['file extension'] == 'mp4':
            sub_codec = ' -c:s mov_text'
        else:
            sub_codec = ' -c:s subrip'
        cmd = ( 'ffmpeg ' + dl_settings['ffmpeg options'] + ' -i \"' + recording_url + '\"' + sub_inputs + mappings + sub_mappings
                + ' -c:v ' + dl_settings['ffmpeg video codec'] + ' -c:a ' + dl_settings['ffmpeg audio codec'] + sub_codec
                + audio_metadata + sub_metadata + ' \"' + filename + '.' + dl_settings['file extension'] + '\"' )

    # Launch FFmpeg
        if finnish:
            print('Aloitetaan tallenteen \033[92m' + filename + '.' + dl_settings['file extension'] + '\033[39m lataus.')
        else:
            print('Starting downloading \033[92m' + filename + '.' + dl_settings['file extension'] + '\033[39m.')
        if not audio_list:
            if finnish:
                print('Ladattava ääniraita: (nimetön)')
            else:
                print('Audio track to download: (undefined)')
        else:
            if finnish:
                print('Ladattavat ääniraidat: ' + ', '.join([get_iso(x, to_iso, iso) for x in audio_list]))
            else:
                print('Audio tracks to download: ' + ', '.join([get_iso(x, to_iso, iso) for x in audio_list]))
        if not ext_subs:
            if not sub_tracks:
                if finnish:
                    print('Ei tekstityksiä')
                else:
                    print('No subtitles')
            else:
                if finnish:
                    print('Ladattavat tekstitysraidat: ' + ', '.join([get_iso(x, to_iso, iso) for x in sub_list]))
                else:
                    print('Subtitle tracks to download: ' + ', '.join([get_iso(x, to_iso, iso) for x in sub_list]))
        print()
        if args.verbose:
            print(cmd)
            print()
        Popen(cmd).wait()

if __name__ == "__main__":
    main()
