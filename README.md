# Infrastructure-utility

The tools provided are cross-platform.

_club.py_ clubs all the files in the specified path on the basis of file extension and move them in separate folders .

_dir.py_ lists all files the with top disk usage in the specified path

NOTE: _dir.py_ has some issues on windows due to permission errors and if granted enough permissions works right

### Prerequisites

Need python version atleast 3.5 .
To check python version do

```
python --version
```

### Installing

Just clone the repo with 
```
git clone https://github.com/kinochi/Infrastructure-Utility
```

## Getting Started

### Clubbing

To get all the list of extensions supported for club.py

```
python3 club.py -list
```
or
```
python3 club.py -l
```
<a href="https://imgflip.com/gif/25ur85"><img src="https://i.imgflip.com/25ur85.gif" title="made at imgflip.com"/></a>

To do the clubbing simply provide the relative or absolute path to the directory
```
python3 /path/to/script/club.py /path/to/directory
```
For eg., there are pdf and ppt files in _current directory_ , so here the file is in _current directory_ and _. (current directory)_ is given for clubbing

<a href="https://imgflip.com/gif/25utti"><img src="https://i.imgflip.com/25utti.gif" title="made at imgflip.com"/></a>


### Top File Usage Stats

To get top file stats provide a relative or absolute path with optionally number of top results to be shown to dir.py

<a href="https://imgflip.com/gif/25usgn"><img src="https://i.imgflip.com/25usgn.gif" title="made at imgflip.com"/></a>

