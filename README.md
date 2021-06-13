<h1 align="center">🥇🎮 Python Games (In Development) 🎲🔫</h1>
<br><br>
<table>
  <tbody>
    <tr>
      <th>What is Python Games?</th>
    </tr>
    <tr>
      <td align="center">
        This repository contains a set of python games that come with a main menu. I initially made these for a school assesment, but I have decided to add to the repository and develop more custom and advanced games. Once there is enough games, I will catergorize them in the main menu to make it easier to choose what game to play. At the moment, all of the games are text-based only, but grapical games will be added later on this year. Below, you will find out how to set the application up and how to use it. Enjoy!
        <br><br>
        <img src="./images/banner.jpg">
        <br>
        <i>Screenshot of the main menu</i>
       </td>
      </tr>
    </tbody>
</table>

<br>

**For Python Beginners** : This code would be great for python beginners, who are interested in game development, to start somewhere. I have commented all of the code so everyone will be able to understand what each part of the program does and how it all works. If you would like to make any improvements, feel free to contibute to this repo. If there is something you don't understand, my contact details can be found on my <a href="https://github.com/shannon-nz/">GitHub profile</a> or my <a href="http://shan.rf.gd">Profile Website</a>

<br><br>

# How The App Works
In the `config.json` file, you are given a default balance of $100, this is all the money that you are allowed to spend in the game. When you are below $0, you are in debt and will not be able to play anymore. To reset the balance, use the `reset` command. You can also just add unlimited money by changing the `config.json` file and setting the balance to whatever you want (as long as it is a number)

The app will automatically install any module required that are not already installed. These modules are required for the app to function fully. The app will also automatically become full screen, this is done with the keyboard module and using the code:
```
keyboard.press('win+up')
keyboard.release('win+up')
 ```

There are mutliple commands that you can use, some of which are just for the sake of seeing what you can do with python.

<br>

# Installation
- Make sure that you have the latest version of <a href="https://www.python.org/downloads/">python</a> installed and that you're using Windows 10.
To install the game, you will need to either:
- Clone the repository to a local folder
- Download the zip file and extract it

<div align="center">
  <img src="./images/installation.JPG">
  <br>
  <i>Where the option are</i>
</div>

<br>

# Getting Started
- **Option 1 (recommended)** - The Easy Option - Simply open the folder that contains the python files and double click app.py. Further instructions will be shown in the app.

<div align="center">
  <img src="./images/getting-started-1.JPG">
  <br>
  <i>Which file to click</i>
</div>

<br>

- Option 2 - Terminal - Use the terminal, to run the application.
Windows:
```
C:\Users\User> cd folder
C:\Users\User> python app.py
```

<br>

- **Option 3 - will not work - (DISCONTINUED) ** - IDE - Open your IDE, Ctrl + o, open the app.py and press F5.

<div align="center">
  <img src="./images/getting-started-3.JPG">
  <br>
  <i>running the file in IDLE</i>
</div>

<br>

# Commands
### Commands
```
clear
lu
rps
hl
system
profile
doc
spaz
restart
quit
help
help des
```

### Command Details 

- `clear` = clear the terminal (action)
- `lu` = [lucky unicorn (game)](#lucky-unicorn) <br>
- `rps` = rock paper scissors (game) <br>
- `hl` = higher/lower (game) <br>
- `system` = get your system information (info) <br>
- `profile` = Open my profile website (website) <br>
- `doc` = Open python games documentation (website) <br>
- `spaz` = SPAZ YOUR SCREEN for 7 seconds (USE WITH CAUTION) <br>
- `restart` = restart the application (action) <br>
- `quit` = quit the entire program (action) <br>
- `help` = display command details (help) <br>
- `help-des` = display command details and an longer description (help) <br>

<br>

# Game Details
### Lucky Unicorn
Lucky Unicorn is essentially a luck-based game. Here are the steps to playing the game: <br>
1. Type `lu` in the main menu.
2. If you have played the game before type `yes` or `y`, otherwise type `no` or `n`.
3. Choose the pretend amount of money you want to spend, you can choose from 0 to 100.
4. Simply press <enter> each round or type `quit` to quit the game.
5. When the game finished, you will be directed back to the main menu.
 
<br>

# To Do / What's Coming
- Count the amount of times each program has been run as well as the total
- Rock Paper Scissors game
- Higher/Lower game
- Create modules for large sets of functions
- Finish the Documentaion (last)

<br>

# Contributing
If you would like to contribute to this project, simply clone the repository, make some changes, and create a pull request. I will review the request and accept it if appropriate. If you would like to contribute to this project or my other projects more than once, feel free to contact me: [slekupvimplyrataqq@protonmail.com](slekupvimplyrataqq@protonmail.com).
