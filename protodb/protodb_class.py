# Copyright 2017 Sayan Dutta
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# import the protodb databse definitions
from . import protodb_pb2 as pdb
from . import directory_class
from . import utils

from google.protobuf.message import DecodeError as ProtoDBParseError

import os

# the header should be constant for all databases
_pdb_header = pdb.ProtoDBHeader(magic=b'ProtoDB', dbversion=b'0.0.1')
_pdb_rootdir_meta = pdb.ProtoDBDirectoryMetadata(creationTimestamp=utils.get_timestamp())
_pdb_rootdir = pdb.ProtoDBDirectory(metadata=_pdb_rootdir_meta, name="root")


# TODO: Implement the path wise addition and deletion of directories and documents
class ProtoDB(object):
    def __init__(self, dbname):
        self._dbname = dbname
        self._db = pdb.ProtoDB(header=_pdb_header, directory=_pdb_rootdir)
        # check if the database exists if not create else read the db into memory
        if not os.path.exists(self._dbname):
            self.flush()
        else:
            with open(self._dbname, 'rb') as dbfile:
                try:
                    # this should succeed for minor and patch updates
                    self._db.ParseFromString(b''.join(dbfile.readlines()))
                except ProtoDBParseError:
                    # This may happen if file format went through a major update
                    # or if the file is malformed
                    raise RuntimeError(
                        "could not parse database '{}', malformed database or incompatible version".format(
                            self._dbname))

        # checks whether the library supports the detected version or not
        # panic if current header could not be matched
        if self._db.header != _pdb_header:
            raise RuntimeError(
                "Unsupported header, expected '{}' found '{}'".format(repr(_pdb_header)[:-1].replace('\n', " "),
                                                                      repr(self._db.header)[:-1].replace('\n', " ")))

        self._root_dir = directory_class.ProtoDBDirectory(self._db.directory)

    def list_dir(self, dir_path="/"):
        pass

    def flush(self):
        with open(self._dbname, 'wb') as dbfile:
            dbfile.write(self._db.SerializeToString())

    def __del__(self):
        self.flush()

    def __repr__(self):
        return "<ProtoDB '{}' @ {}>".format(self._db.header.dbversion.decode(), self._dbname)
