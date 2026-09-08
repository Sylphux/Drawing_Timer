# What is this

This is a web drawing timer app + a python script to help you create your own reference pack.

# How to use it ?

Upload your references (it's not really an upload, everything happens locally). Then, use keywords in the navbar to make a selection of images you want based on the file names. Set the timer time using the format you want, and then click start to start the series.

## Selecting references

The white zone is for selecting references. The dark zone is for excluding references.
Both textboxes in them are AND and OR filters. It gives a lot of options for selecting references.

## Creating a nice reference pool with the python 'rename.py' script

use the 'rename.py' tool provided to batch rename reference files. What i like to do with it is download a lot of images, then sort them in folders and running the script in the folders to add tags. Then, when all images are tagged, I put them all in a 'sorted' folder which i use on the app.

### Use case of the script :

You download a folder of nature images. Launch the script in the folder with the 'add nature' as argument. the word 'nature' will be added to add the files in the folder.

There is a command to add a string, one to remove one, one to replace, and one to rename the files from scratch (with an incrementing number)

use `python rename.py help` to see details on the possible commands.

I recommend adding this script as an alias to it really works like a command taking arguments.

This script is hand coded, opposedly to the web app.

## Other functionnalities

- Ban images with X, unban them from the ban list
- Play / Pause with space, stop session with k
- Naviguate through references with the right left arrows or Q and D
- Zoom on the pictures with the mouse wheel. It's a bit clunky but it works.

# AI Disclaimer

I usually never vibe code, I don't like it. But I vibe coded this because I just really needed the tool and didnt want to spend days / months of work while I wanted to focus on drawing. So yeah it's vibe coded and the code quality is probably trash, it's a very low effort project please don't expect too much. But it works, so I'm quite happy with it for now.
