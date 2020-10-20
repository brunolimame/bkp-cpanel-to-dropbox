## Save BKP from Cpanel to Dropbox Manually
This script is ideal for sending large files without losing connection to Dropbox.
The file when larger than 300MB is divided into blocks of up to 300MB.
At the end of sending blocks, the final file is saved in Dropbox.

### How to run a manual backup 

```bash
/usr/local/cpanel/scripts/pkgacct USERNAME DIRECTORY
```
**DOC** [https://support.cpanel.net/hc/en-us/articles/360051760834-How-to-run-a-manual-backup](https://support.cpanel.net/hc/en-us/articles/360051760834-How-to-run-a-manual-backup)

### Sending BKP to Dropbox
- Create an app on Dropbox
- Generate an authentication token
- Paste your key in the script

https://github.com/brunolimame/bkp-cpanel-to-dropbox/blob/4f2276e445c0d890ddd0c00a376fe8e5b57f0c6b/bkp-cpanel-dropbox.py#L55

- Install the dependencies
- Give the script permission
```bash
chmod -X bkp-cpanel-dropbox.py
```
- Run script

### Dependencies
- Python 2.7
- Install pip
- Install dependencies
```bash
pip install dropbox tqdm
```

### Run script

```bash
python bkp-cpanel-dropbox.py FILE_ORIGIN FILE_DESTINY
```
- **FILE_ORIGIN**: Location of the file to be sent
- **FILE_DESTINY**: Location where the file will be saved in the dropbox
	- default: "/BKP-CPANEL/"
