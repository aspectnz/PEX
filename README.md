<h1 align="center">PEX Documentation (in development)</h1>

<img src="./main/images/pex.jpg" align="center">

<p>
  <h2>What is PEX?</h2>
    The name PEX is not owned by me and its short for Python Experimental. As you would guess, this is just an experimental app based off exploring what is possible with python. This app started off as school project were I develop some games for an assessment, but I decided to make it into something more. With the assurance that I will be including comments of course. At the moment, everything is text-based and does not have a GUI, this may change in the future, but not anytime soon.
  <br><br>
  As I am sure I am only scratching the surface of the capabilities of python, I am uncovering lots of interesting things. With this, a lot of new modules are involved, so make sure you are okay with installing them. Below you will find the full documentation of the application and how to use it. If you find that there are any issues with the documentation or program, then feel free to edit it, bring up an issue or contact me. Enjoy!

</p>

</br>

<h1>Table of Contents</h1>
<ul>
  <li>
    <a href="#pex-documentation-in-development">PEX Documentation (in development)</a>
    <ul>
      <li><a href="#what-is-pex">What is PEX?</a></li>
    </ul>
  </li>
  <li><a href="#table-of-contents">Table of Contents</a></li>
  <li><a href="#a-brief-overview-into-how-pex-works">A brief overview into how PEX works</a></li>
  <li><a href="#requirements">Requirements</a></li>
  <li><a href="#installation">Installation</a></li>
  <li>
    <a href="#getting-started">Getting Started</a>
    <ul>
      <li><a href="#password-pass">PEX Admin Password</a></li>
    </ul>
  </li>
  <li>
    <a href="#trouble-shooting">Trouble Shooting</a>
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
 

</br>

**For Python Beginners** : This code would be great for python beginners, who are interested in game development, to start somewhere. I have commented all of the code so everyone will be able to understand what each part of the program does and how it all works. If you would like to make any improvements, feel free to contibute to this repo. If there is something you don't understand, my contact details can be found on my <a href="https://github.com/shannon-nz/">GitHub profile</a> or my <a href="http://shan.rf.gd">Profile Website</a>

**For everyone else**: I have attempted to make the setup of the program as simple as possible, but you can refer to the troubleshooting section of you need help or feel free to contact me at <a href="slekupvimplyrataqq@protonmail.com"></a>.

</br>

# A brief overview into how PEX works
You will find that in `main/config.json`, there are the settings for running the application. The settings include options which the user can change via commands, requirements which can only be changed by accessing the files, stats which are values changed by the program, and finally the user data which is dynamic and is flexible. The requirments are put in place so that the application will work properly in most circumstances, if you try to modify these, the application might not work as expected. 

You may notice that PEX will automatically do some things, such as... The app will automatically install any modules required that are not already installed. These modules are required for the app to function fully. The app will also automatically become full screen, this is done with the keyboard module. Your mouse will be moved to the top left since you do not want it in the way of important text. The `doc` command will be automatically typed for people who are using the application for the first time.

Games, both from the assesment as well as custom games that will be added can be found in `main/games`. Games which are from the assesment contain a folder named `Archive` these contain several files, each representing different functions involved in the game. 

For your enjoyment, there is a large list of commands which are available. While in development, not all of these will work as expected. Each command will contain at least one sub command, `-help`, and these will better define the intentions of the user and act accordingly.

The code is completly opensource and available to anyone who, as long as the intructions listed out in the MIT license are followed.

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

# Making sure everything is installed
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

# Running PEX
### Admin Password: `pass`  The admin password is required to run some of the admin commands or to reset everything back to the default with the `settings -reset` command.
- **Method 1 (recommended)** - This is the most easiest option - In the root folder, simply double click app.py to run the application. Note: At the moment, there is a bug that requires you to run the application twice on the first install. So the first time, the program will close, please doubel click app.py once more and it should work as expected. 
</br>

- **Method 2 - Terminal (advanced)** - I would likely consider this to be the better option. In the case that you run into a problem on the way, instead of the app closing immediatly, you will be able to see the errors. If you are able to fix the error yourself, feel free to push the code or inform me of the error.
Windows only:
```
C:\Users\User> cd folder\pexdirectory\pex
C:\Users\User> python app.py
```
</br>

- **Method 3 - This method is discontinued but still possible - Open the file in IDLE and press F5 or go `Run > Run Module`. Note: This will reopen the file in the default application for python, by default this should be the terminal. If it is not the terminal for you, please make the terminal the default application or try method 1 or 2.

</br>

# Trouble Shooting
<table>
  <tbody>
    <tr>
      <th>Issue</th>
      <th>Potential Fix</th>
    </tr>
    <tr>
      <td>Program closes on first run</td>
      <td>Run the program once again (currently an importing issue)</td>
    </tr>
    <tr>
      <td>Anything else</td>
      <td>Contact me at <a href="slekupvimplyrataqq@protonmail.com">slekupvimplyrataqq@protonmail.com</a> with the `main/data.log` file.</td>
    </tr>
  </tbody>
</table>

</br>

# Commands

Use the `-help` sub-command to list out all the sub-commands for any command, for example `download -help`. You can also list out the full list of commands and sub-commands with the `help -all` command.

### Commands

```
   admin                         perform admin tasks (caution)
   cls                           clear the terminal
   doc                           open python games documentation on GitHub
   download                      download documentations and other things
   help                          display commands and functions
   hl                            play higher/lower game
   log                           view all past logs
   ls                            list directory
   lu                            play lucky unicorn game
   profile                       open my profile website
   quit                          quit the entire program
   rps                           play rock paper scissors game
   restart                       restart the application
   settings                      print settings in JSON format
   shortcuts                     print settings in JSON format
   spaz                          SPAZ YOUR SCREEN for 7 seconds (caution)
   stats                         view your stats
   system                        get your system information
```


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
