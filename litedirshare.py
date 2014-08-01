#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# dirShare is a ultralightweight web application for directory sharing.
# $ python litedirshare.py /directory/path host_ip port
#
# Copyright 2013 Caner BAŞARAN
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from bottle import route, run, static_file, request, redirect
import os
import sys

try:
    PATH_LOCAL = u"{0}".format(sys.argv[1])
except:
    raise Exception("You must give a directory path")

HEADER = """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"><html lang="en"><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>liteDirShare</title><style>body{margin:50px 0;padding:0;text-align:center;font-family:"Lucida Sans Unicode","Lucida Grande",Sans-Serif}div.content{width:800px;margin:0 auto}div.path{text-align:left;padding:0 0 .3em .7em;border-bottom:2px solid #6b6b6b}#fileTable{font-size:12px;background:#fff;width:800px;border-collapse:collapse;text-align:left}#fileTable th{font-weight:400;text-align:left;padding-left:1em;border-bottom:1px solid #ff1405;height:2.5em}#fileTable td{border-bottom:1px solid #e0e0e0;color:#3c3c3c;height:25px;padding-left:1em}#fileTable td.data{background-color:#ededed;width:12.5%}#fileTable a{text-decoration:none;color:#3c3c3c}#fileTable a:hover{color:#555}</style></head><body></form><div class="content"><div class="path"><INPUT TYPE="button" VALUE="<<--" onClick="history.go(-1)"> <INPUT TYPE="button" VALUE="-->>" onClick="history.go(1)"> PATH: {{ path_dir }}</div><table id="fileTable"><thead><tr><th>Name</th><th>Size</th></tr></thead><tbody>"""
FOOTER = """</tbody></table></div></body></html>"""


@route('/')
@route('/index/')
def index_2():
    redirect('/index')


@route('/index')
@route('/index/<path:re:.+>')
def index(path=None):
    return read_folder('') if path is None else read_folder(path)


@route('/download')
def download():
    filename = request.GET.get('file')
    return static_file(filename.decode("utf-8"), root=PATH_LOCAL, download=filename)


def read_folder(path):
    path = path.decode("utf-8")
    to_html = ""
    if path == '':
        path_dir = PATH_LOCAL
    else:
        path_dir = PATH_LOCAL + "/" + path
    for archive in sorted(os.listdir(path_dir)):
        if not archive.startswith('.'):
            file_path = os.path.join(path_dir, archive)
            if os.path.isdir(file_path) is True:
                to_html += u"<tr><td>[DIR ] &#x2605; <a href='%s/%s'>%s </a></td> <td class='data'></td> </tr>" % (request.fullpath, archive, archive)
            else:
                to_html += u"<tr><td>[FILE] &#x2606; <a href='/download?file=%s/%s'>%s</a></td> <td class='data'>%s</td></tr>" % (path, archive, archive, convert_bytes(file_path))
    return HEADER.replace("{{ path_dir }}", path) + to_html + FOOTER


def convert_bytes(path):
    bytes = float(os.path.getsize(path))
    abbrevs = ((1073741824, 'GB'), (1048576, 'MB'), (1024, 'kB'), (1, 'bytes'))
    for factor, suffix in abbrevs:
        if bytes >= factor:
            break
    return '%.1f %s' % (bytes / factor, suffix)

run(host=u"{0}".format(sys.argv[2]), port=u"{0}".format(sys.argv[3]))