# Alien Invasion

This is an alien invader game written using pygame library. Pygame is a powerful Python modules that manage graphics, animation, and even sound, making it easier for users to build sophisticated games. In this particular game, a user is given a ship at the bottom center of the screen. A ship will be able to move left, right, top, bottom and shoot bullets at the aliens who are invading the screen from top down. A scoring, level, and ship lives are displayed at the bottom of the screen for the users to keep track of their score, level and lives. The game will be over once a user loses all lives, and will be able to play a new game from the beginning.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

## Prerequisites

You'll need to install the following packages:
* python packages with pip/pip3
* pygame

### Checking for pip on Linux and OS X
```
pip/pip3 --version
```
You should see the similar output 
```
pip 21.3.1 from /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pip (python 3.7)
```
If you have more than one version of Python on your system, verify that pip is associated with the version of Python you're using--for example, ```python 3.7 ``` in this case.

If you can't run the pip command, try installing pip


## Installing

### Installing pip on Linux and OS X
```
sudo python get-pip.py
```
After the program runs, use the command ```pip --version``` (or ```pip3 --version```) to make sure pip was installed correctly.

### Installing pygame on OS X
To install the libraries that Pygame depends on, enter the following command:
```
brew install hg sdl sdl_image sdl_ttf
```
This will install the libraries needed to run the Alien Invasion. 

If you also want to enable more advanced functionality, such as including sound in games, ou can install two additional libraries (optional):
```
brew install sdl_mixer portmidi
```

To install the pygame, use the following command:
```
pipe3 install pygame
```
To check whether the installation was successful, start a Python terminal session and import pygame as follow:
```
python3
>>> import pygame
>>>
```

If you are on a different system, please check/look up how to install such packages on your particular system.

## Deployment

Since this game is built using pygame, no deployment is necessary. Just install the aforementioned packages and you'll be able to play it on your own local system.

## Built With

* [python3](https://docs.python.org/3/) -  The core language
* [pygame](https://www.pygame.org/docs/) - The Python library used

## Authors

* **Ye Aung** - *Initial work* - [Github](https://github.com/poppan2)

## Acknowledgments

* Python Crash Course by Eric Matthes
* I grew up playing Galaga, and I've always enjoyed it. I came across this python crash course book by Eric Matthes while I was learning Python on my own. I felt so excited and can't wait to recreate a much simpler version of the Galaga game. 
