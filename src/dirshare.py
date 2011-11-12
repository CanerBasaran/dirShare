from bottle import route, run, debug, template, static_file, request, redirect, error
import os
import time
import sys

TEXT_TYPE = ['doc', 'docx', 'txt', 'rtf', 'odf', 'text', 'nfo']
AUDIO_TYPE = ['aac', 'mp3', 'wav', 'wma', 'm4p', 'flac']
IMAGE_TYPE = ['bmp', 'eps', 'gif', 'ico', 'jpg', 'jpeg', 'png', 'psd', 'psp', 'raw', 'tga', 'tif', 'tiff', 'svg']
VIDEO_TYPE = ['mv4', 'bup', 'mkv', 'ifo', 'flv', 'vob', '3g2', 'bik', 'xvid', 'divx', 'wmv', 'avi', '3gp', 'mp4', 'mov', '3gpp', '3gp2', 'swf', 'mpg', 'mpeg']
COMPRESS_TYPE = ['7z', 'dmg', 'rar', 'sit', 'zip', 'bzip', 'gz', 'tar', 'ace']
EXEC_TYPE = ['exe', 'msi', 'mse']
SCRIPT_TYPE = ['js', 'html', 'htm', 'xhtml', 'jsp', 'asp', 'aspx', 'php', 'xml', 'css', 'py', 'bat', 'sh', 'rb', 'java']

try:
	PATH_LOCAL = u"{0}".format(sys.argv[1])
except:
	PATH_LOCAL = u"."

@route('/')
@route('/index/')
def index_2():
    redirect('/index')

@route('/index')
@route('/index/:path#.+#')
def index(path=None):
    if path is None:
        return read_folder('')
    else:
        return read_folder(path)

@route('/download')    
def download():
    filename = request.GET.get('file')
    return static_file(filename, root=PATH_LOCAL, download=filename)

@error(404)
def error404(error):
    return 'Nothing here, sorry'

def read_folder(path):
    to_html_1 = []
    to_html_2 = []
    if path == '':
        path_dir = PATH_LOCAL
    else:
        path_dir = PATH_LOCAL + '/' + path
    file_list = os.listdir(path_dir)
    for archivo in file_list:
        if archivo == 'mia_main.py' or archivo == 'bottle.py' or archivo == 'bottle.pyc':
            pass
        else:
            file_path=os.path.join(path_dir, archivo)
            if os.path.isdir(file_path) == True:
                to_html_1.append([request.fullpath, archivo, archivo, date_file(file_path), convert_bytes(file_path)])
            else:
                extension = os.path.splitext(archivo)[1].replace('.','')
                if extension in TEXT_TYPE:
                    type_file = 'text'
                elif extension in AUDIO_TYPE:
                    type_file = 'audio'
                elif extension in IMAGE_TYPE:
                    type_file = 'imagen'
                elif extension in VIDEO_TYPE:
                    type_file = 'video'
                elif extension in COMPRESS_TYPE:
                    type_file = 'compress'
                elif extension in EXEC_TYPE:
                    type_file = 'exec'
                elif extension in SCRIPT_TYPE:
                    type_file = 'script'
                elif extension == 'pdf':
                    type_file = 'pdf'
                else:
                    type_file = 'unknow'
                to_html_2.append([type_file, path, archivo, archivo, date_file(file_path), convert_bytes(file_path)])
    return template('layout', to_html_1=to_html_1, to_html_2=to_html_2, path_dir=path_dir)

def convert_bytes(path):
    bytes = float(os.path.getsize(path))
    if bytes >= 1099511627776:
        terabytes = bytes / 1099511627776
        size = '%.2f Tb' % terabytes
    elif bytes >= 1073741824:
        gigabytes = bytes / 1073741824
        size = '%.2f Gb' % gigabytes
    elif bytes >= 1048576:
        megabytes = bytes / 1048576
        size = '%.2f Mb' % megabytes
    elif bytes >= 1024:
        kilobytes = bytes / 1024
        size = '%.2f Kb' % kilobytes
    else:
        size = '%.2f Byte' % bytes
    return size

def date_file(path):
    tiempo = time.gmtime(os.path.getmtime(path))
    return time.strftime("%d/%m/%Y-%H:%M:%S", tiempo)

@route('/static/:filename', name='static')
def static_files(filename):
    return static_file(filename, root='./static/')

debug(True)
run(host='0.0.0.0', port=8080, reloader=True)
