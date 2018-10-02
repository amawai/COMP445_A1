# COMP445_A1
HTTP client library implementation

### Getting the Commandline Tool
To obtain the httpc executable:
1. `pip install pyinstaller`
2. `pyinstaller --onefile path/to/COMP445_A1/httpc/httpc.py`
3. The `httpc` executable is found in `path/to/COMP445_A1/httpc/build`
4. Use the executable as you wish (can use the path to this executable in the next step)

To have httpc as a commandline tool, do the following:
For linux or macOS
1. Edit `~/.bashrc` or `~/.bash_profile` using any editor
2. Add `alias httpc-command="python /path/to/COMP445_A1/httpc/httpc.py` to the file
3. Run `source ~/.bashrc` or `source ~/.bash_profile`


Sample Commands:
1. `httpc get -v https://httpbin.org/status/418`
2. `httpc post -h Content-Type:application/json -d '{"Assignment": 1}' http://httpbin.org/post`
