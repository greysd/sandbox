import os
import time

import tornado.web

from atomicfile import AtomicFile

from apiserver.route import route
from apiserver.settings import PRIVATE_FILES_PATH


class File(object):
    def __init__(self, display_name, url):
        self.display_name = display_name
        self.url = '/dl/' + url


@route('/')
class UploadFileHandler(tornado.web.RequestHandler):
    def _save(self, request_file, media_path=PRIVATE_FILES_PATH):
        filename = str(time.time())
        ext = os.path.splitext(request_file.filename)[1].lower()

        dirpath = os.path.join(media_path)
        if not os.path.exists(dirpath):
            os.makedirs(dirpath)

        path = os.path.join(dirpath, '%s%s' % (filename, ext))
        with AtomicFile(path, 'wb') as uploaded:
            uploaded.write(request_file.body)

        display_name = request_file.filename
        url = '%s%s' % (filename, ext)
        return File(display_name, url)

    def get(self):
        self.render("upload.html")

    def post(self):
        files = []

        if "attach" in self.request.files:
            assert len(self.request.files["attach"]) == 1, "Only one file at a time is expected"

            for f in self.request.files["attach"]:
                files.append(self._save(f))

        self.render("uploaded.html", files=files)


@route('/files')
class AllFilesHandler(tornado.web.RequestHandler):
    def get(self):
        all = []
        for root, dirs, files in os.walk(PRIVATE_FILES_PATH):
            for name in files:
                all.append(File(name, name))

        self.render("files.html", files=all)
