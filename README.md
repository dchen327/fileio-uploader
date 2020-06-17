# File.io Uploader
A python command line utility to allow for quick file transfers using file.io

# Usage
`python3 fileio_upload.py test.txt`

This command will print the file.io link and will also copy the link to clipboard.
Optional arguments:
* `--noclip` will not copy link to clipboard after upload
* `-j` or `--join` will push the link to a phone connected through Join by Joaoapps.

Optional alias for convenience:
* Put alias `fileio="python3 PATH/TO/CODE/fileio_upload.py"` in ~/.bashrc
* New Usage: `fileio test.txt`