## About

This is light weight desktop widget, that shows random picture from given directory. It's similar to the same plasmoid from KDE 4.x. I very liked it and was very upset when KDE 4 became obsolete and there's no alternative plasmoid in KDE 5. That's why I decided to write it myself. It was written in Python 3 and PyQt 5 and it's compatible with all known desktop environments.

## Screenshots
![Main window in MATE](https://raw.github.com/rinaldus/photoframe/master/screenshots/screen1.jpg)

## Install

You need to install PyQt5 as dependency. Then just clone this git repository or download release and copy all files where you want to store this program. No additional installation is required.  

## Launch

Give execute permission to photoframe.py
```sh
$ chmod +x photoframe.py
```
After program start, you have to set directory with many pictures or photos in "Settings" window (this window will appear automatically at first program start).

## Features
* JPG and PNG only formats are supported.
* When you set directory, the program will search for JPG and PNG files in this directory and also in subdirectories recursively.
* Click on picture to choose another random picture immediately. You can also set update interval for automatic change.

## Changelog

### Version 1.01 (release date: 05.07.16)
* New Refresh context menu option instead of left mouse click on picture
* Code cleaning
* Several bug fixes

### Version 1.0 (release date: 29.02.16)
* Initial version
