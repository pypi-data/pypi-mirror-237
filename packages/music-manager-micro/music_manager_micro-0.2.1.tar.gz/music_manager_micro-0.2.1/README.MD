# MusicManager
Build a list of media files from a root directory
# Usage
First time usage should use the execute function. This will return the python list of entries containing tuples in the form 
```
[
(mtime:int,path:str),
...
]
```
```python
import MusicManager as mm

library = 'my_library'
root_dir = '/media/music'
music_list = mm.execute(library, root_dir)
```
Since the program stores the result in a sqlite DB in 
```
$HOME/.config/MusicManagerMicro/<library_name>
```
we can retrieve the data quickly without re-scanning the directory. We only need to execute when we want to check for new files.

Get an existing list
```python
import MusicManager as mm
library = '<library_name>'
mm.setLibrary(library)
music_list = mm.get_list()
```
# Features
* Default searches for .mp3 and .flac files
* Supports absolute and relative root directory
# Maintenance
* Remove .config/MusicManager directory to safely clear all library data
* Backup .config/MusicManager directory and restore
# Notes
* Library name is intended for internal use so should only contain characters acceptable for a folder name A-Z, a-z, _, -.

# Build

```bash
python -m build
python -m twine upload dist/*
```