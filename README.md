![fTerm](logo.png)
[![homebrew](https://img.shields.io/badge/homebrew-0.0.2a3-yellow.svg?style=flat-square)]()
<!-- [![GitHub Issues](https://img.shields.io/github/issues/lschumm/fterm-dev.svg)](https://github.com/lschumm/zapcore/issues) -->
[![License (GPL version 3)](https://img.shields.io/badge/license-GNU%20GPL%20version%203-blue.svg?style=flat-square)](http://opensource.org/licenses/GPL-3.0)
[![Awesome: true](https://img.shields.io/badge/awesome%20-yes-brightgreen.svg?style=flat-square)]()

# About

fTerm is a terminal with english syntax and natural language processing.

# How-To

To run *command* with arguments *a1, a2,...*, simply run

```
f command a1, a2,...
```

## Examples

```
$ ls
a.txt
b.rst
c.mp4
$ f remove b.rst
[f-i] delete a⏎
$ ls
a.txt
c.mp4
```

```
$ cat a
this is a test!
$ cat b
this is also a test!
$ f swap a b
[f-i]⏎
[f] Swapped a and b
$ cat a
this is also a test!
$ cat b
this is a test!
```

# Commands

## swap *file1* *file2*
A function that swaps the names of two files.

## run *filename*
A universal run function; runs *filename* based on its file extension.

## size *filename*
Return the size of *filename* in human-readable format.


## delete *name*
Delete the file or directory *name*.


## list
List the files the current directory.


## read *filename*
Read *filename*.


## edit *filename*
Edit *filename*.

## commands
List all fTerm commands.

## help *command*
Return the docstring of fTerm function *command*.

# Installing (Mac)

First, run

```
brew tap lschumm/tap
```
and then

```
brew install fterm
```

fTerm is now installed! Verify your installation by running:
```
$ f
[f-i] Please specify a command (e.g., f swap file1 file2)
```

# Notes
- Install either the *zsh* or *fish* shell. Autocomplete is **awesome**.
- fTerm currently does not have a `cd` command due to terminal session crud.


# Authors

* **Liam Schumm** - *Initial work* - [@lschumm](https://github.com/lschumm)
* **Andy Merrill** - *Idea* - [@appleinventor](https://github.com/appleinventor)
* **Jack Merrill** - *Development* - [@yoshifan509](https://github.com/yoshifan509)




#  License

This project is licensed under the GNU GPL License, version 3.0 - see the [LICENSE.md](LICENSE.md) file for details
