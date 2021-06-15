<h1 align="center">🥇🎮 Python Games (In development) 🎲🔫</h1>

</br></br>


<img src="./main/images/banner.webp" min-width="400px" max-width="400px" width="400px" align="right">

<p align="left">
  <h2>What is Python Games?</h2>
  This repository contains a set of python games that come with a main menu. I initially made these for a school assesment, but I have decided to add to the
  repository and develop more custom and advanced games. 
  
  Once there is enough games, I will catergorize them in the main menu to make it easier to choose what game to
  play. 
  
  At the moment, all of the games are text-based only, but grapical games will be added later on this year. Below, you will find out how to set the application
  up and how to use it. Enjoy!
</p>

</br>

<table>
  <tbody>
    <tr>
      <th>Table of contents</th>
    </tr>
    <tr>
      <td width="350px">
      </br>
        <ul>
          <li>
            <a href="#-python-games-">🥇🎮 Python Games 🎲🔫</a>
            <ul>
              <li><a href="#what-is-python-games">What is Python Games?</a></li>
            </ul>
          </li>
          <li><a href="#how-the-app-works">How the app works</a></li>
          <li><a href="#requirements">Requirements</a></li>
          <li><a href="#installation">Installation</a></li>
          <li>
            <a href="#getting-started">Getting Started</a>
            <ul>
              <li><a href="#password-pyga">Password</a></li>
            </ul>
          </li>
          <li>
            <a href="#commands">Commands</a>
            <ul>
              <li><a href="#commands-1">Commands</a></li>
              <li><a href="#command-details">Command Details</a></li>
            </ul>
          </li>
          <li>
            <a href="#game-details">Game Details</a>
            <ul>
              <li><a href="#lucky-unicorn">Lucky Unicorn</a></li>
            </ul>
          </li>
          <li><a href="#to-do--whats-coming">To Do / What's Coming</a></li>
          <li><a href="#advanced">Advanced</a></li>
          <li><a href="#contributing">Contributing</a></li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

</br>

**For Python Beginners** : This code would be great for python beginners, who are interested in game development, to start somewhere. I have commented all of the code so everyone will be able to understand what each part of the program does and how it all works. If you would like to make any improvements, feel free to contibute to this repo. If there is something you don't understand, my contact details can be found on my <a href="https://github.com/shannon-nz/">GitHub profile</a> or my <a href="http://shan.rf.gd">Profile Website</a>

</br>

# How The App Works
In the `config.json` file, you are given a default balance of $100, this is all the money that you are allowed to spend in the game. When you are below $0, you are in debt and will not be able to play anymore. To reset the balance, use the `reset` command. You can also just add unlimited money by changing the `config.json` file and setting the balance to whatever you want (as long as it is a number)

The app will automatically install any module required that are not already installed. These modules are required for the app to function fully. The app will also automatically become full screen, this is done with the keyboard module and using the code:
```
keyboard.press('win+up')
keyboard.release('win+up')
 ```

There are mutliple commands that you can use, some of which are just for the sake of seeing what you can do with python. Some of the code may not make sense if you have not used some of the modules that I am using. If this is the case, you could start in the `/python-games/main/games` folder to find the folders for each game. In the archive folder for each, you will find each of functions as an individual program. This may make it easier to understand.

</br>

# Requirements

<br>

<table align="center">
  <tbody>
    <tr>
     <th>Requirements</th>
      <th>How to meet requirements</th>
    </tr>
    <tr>
      <td>Windows 10</td>
      <td><a href="https://www.wikihow.com/Update-Windows">Click here</a> to learn how to update windows.</td>
    </tr>
    <tr>
      <td>Latest version of python</td>
      <td>Click the installer in the root folder called </td>
    </tr>
    <tr>
      <td>Latest version of pip</td>
      <td>Click on update pip in the root directory</td>
    </tr>
    <tr>
      <td>A stable internet connect</td>
      <td>Especially the first time. You can disable the internet requirement in the main/config.json or with the command `intreq -disable` command</td>
    </tr>
  </tbody>
</table>

<br>

# Installation
Make sure that you have the latest version of <a href="https://www.python.org/downloads/">python</a> installed and that you're using Windows 10. If you do not currently have the latest version of python installed, you can find the installer in the root directory named `python-3.9.5-amd64.exe`. Double click the installer file to install python. When installing, make sure you check `add to path` and `disable path limit`.
<br>
To install the game, you will need to either:
- Clone the repository to a local folder
- Download the zip file and extract it

<div align="center">
  <img src="./main/images/installation.JPG">
  </br>
  <i>Where the option are</i>
</div>

<br>

# Getting Started
### Password: `pyga`
- **Option 1 (recommended)** - The Easy Option - Simply open the folder that contains the python files and double click app.py. Further instructions will be shown in the app.

<div align="center">
  <img src="./main/images/getting-started.JPG">
  <br>
  <i>Which file to click</i>
</div>

</br>

- Option 2 - Terminal - Use the terminal, to run the application.
Windows:
```
C:\Users\User> cd folder
C:\Users\User> python app.py
```

</br>

- **Option 3 - will not work - (DISCONTINUED) ** - IDE - Open your IDE, Ctrl + o, open the app.py and press F5.

<div align="center">
  <img src="./main/images/getting-started-3.JPG">
  <br>
  <i>running the file in IDLE</i>
</div>

Running the program in IDLE is now disabled. This is because IDLE lacks the flexability of a terminal, henceforth I have decided to strictly limit the application to the terminal. 

</br>

# Commands
### Commands
```
clear
lu
rps
hl
stats
system
profile
doc
spaz
settings
log
log -clean
log -disable
log -enable
restart
quit
help
help -des
```

### Command Details 

- `clear`           = clear the terminal (action) </br>
- `lu`              = [lucky unicorn (game)](#lucky-unicorn) </br>
- `rps`             = rock paper scissors (game) </br>
- `hl`              = higher/lower (game) </br>
- `stats`           = View your stats </br>
- `system`          = get your system information (info) </br>
- `profile`         = open my profile website (website) </br>
- `doc`             = open python games documentation (website) </br>
- `spaz`            = SPAZ YOUR SCREEN for 7 seconds (fun) </br>
- `settings`        = print settings in JSON format (info) </br>
- `log`             = view all past logs (info) </br>
- `log -clean`      = view all past logs (info) </br>
- `log -disable`    = disable logs (action) </br>
- `log -enable`     = enable logs (info) </br>
- `restart`         = restart the application (action) </br>
- `quit`            = quit the entire program (action) </br>
- `help`            = display command details (help) </br>
- `help -des`       = display command details and an longer description (help) </br>

<i>When all of the commands have been added, this message will be removed</i>
</br>
You can also clone/pull the repository to recieve the latest commands with the `help` command. I update the commands almost daily, when I stop I will remove this message.

</br>

# Game Details
### Lucky Unicorn
Lucky Unicorn is essentially a luck-based game. Here are the steps to playing the game: <br>
1. Type `lu` in the main menu.
2. If you have played the game before type `yes` or `y`, otherwise type `no` or `n`.
3. Choose the pretend amount of money you want to spend, you can choose from 0 to 100.
4. Simply press <enter> each round or type `quit` to quit the game.
5. When the game finished, you will be directed back to the main menu.
 
</br>

# To Do / What's Coming
- Count the amount of times each program has been run as well as the total
- Rock Paper Scissors game
- Higher/Lower game
- Create modules for large sets of functions
- Finish the Documentaion (last)

To find other tasks that are being or need to be completed, have a look at the <a href="https://github.com/shannon-nz/python-games/issues">issues page for this reposiotory</a>. 

</br>

# Advanced
If you would like to change the application settings, feel free to edit the config.json file on your own copy. I will be adding more settings there, so don't forget to pull from the repo frequently! 

</br>

# Contributing
If you would like to contribute to this project, simply clone the repository, make some changes, and create a pull request. I will review the request and accept it if appropriate. If you would like to contribute to this project or my other projects more than once, feel free to contact me: [slekupvimplyrataqq@protonmail.com](slekupvimplyrataqq@protonmail.com).
Some skills that would be specifically useful to this project are:
- Fundamental knowledge of python
- Tkinter
- Pygame
- Django

If these do not apply to you, then simply starring the repository would be great.
