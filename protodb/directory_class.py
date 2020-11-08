# the directory class for protodb
# it can handle listing and making directories and documents

from . import protodb_pb2 as pdb
from . import utils
from . import document_class


# protodb directory wrapper
class ProtoDBDirectory:
    def __init__(self, directory):
        if not isinstance(directory, pdb.ProtoDBDirectory):
            raise TypeError("expected an instance of ProtoDBDirectory, got {}".format(type(directory)))

        self._dir = directory

    def make_dir(self, name):
        return ProtoDBDirectory(
            self._dir.directory.add(metadata=pdb.ProtoDBDirectoryMetadata(
                creationTimestamp=utils.get_timestamp()
            ), name=name)
        )

    def make_doc(self, name, data):
        if not isinstance(data, bytes):
            data = bytes(data, 'utf-8')
        return document_class.ProtoDBDocument(
            self._dir.document.add(metadata=pdb.ProtoDBDocumentMetadata(
                creationTimestamp=utils.get_timestamp()
            ), name=name, data=data)
        )

    def list_dir(self):
        return [d.name for d in self._dir.directory] + [d.name for d in self._dir.document]

    def __str__(self):
        return self._dir.name

    def __repr__(self):
        return "<ProtoDB Directory {}>".format(self._dir.name)
