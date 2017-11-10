# protodb-python
Python library for ProtoDB

## Why another NoSQL database ??
If you need a local database that avoids the overheads of a database server,
you probably would use the SQLite Project.
What if you need a local NoSQL database ??
Providing a local file based NoSQL database is what the ProtoDB project aims to achieve.

## Why is it called ProtoDB ??
The database uses Protocol Buffer or protobuf to generate the basic definitions
on top of which the libraries are written. Since database file format builds on top of the
protobuf binary format it is only fitting to name the project as ProtoDB. An advantage of
protobuf as the base is that it can generate bindings from the same definition file
for many different programming languages.

## License
This project is licensed under the Apache License, Version 2.0.
See [LICENSE](LICENSE) file for a copy of the license.