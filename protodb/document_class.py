from . import protodb_pb2 as pdb


# the document wrapper
class ProtoDBDocument:
    def __init__(self, document):
        if not isinstance(document, pdb.ProtoDBDocument):
            raise TypeError("expected an instance of ProtoDBDocument, got {}".format(type(document)))

        self._doc = document

    def __repr__(self):
        return "<ProtoDB Document {}>".format(self._doc.name)

    def __str__(self):
        return self._doc.name
