# ubuntu-macos-keys
Ubuntu key-binding configuration to emulate some common macOS key-bindings

Maps common macOS key combinations to native Ubuntu key combinations using AutoKey
* Cmd+c: copy (Ctrl+c) (Ctrl+Shift+c in Ubuntu terminal)
* Cmd+v: paste (Ctrl+v) (Ctrl+Shift+v in Ubuntu terminal)
* Cmd+x: cut (Ctrl+x)
* Cmd+z: undo (Ctrl+z)
* Cmd+y: redo (Ctrl+y)
* Cmd+a: select all (Ctrl+a)
* Cmd+o: open (Ctrl+o)
* Cmd+s: save (Ctrl+s)
* Cmd+t: new tab (Ctrl+t)

Also shows how to configure the following macOS-style functionality in Ubuntu 16.04
* Cmd+Tab: Switch between apps
* Cmd+\`: Switch between windows of same app

Tested in a Ubuntu 18.04 Desktop.

To make ubuntu function like a Mac with a PC keyboard (So you don't have to get used to two different keyboards).
I use a mac for work and kubuntu at home 

## Install AutoKey
`# apt-get install autokey-gtk`

## Set up extra shortcuts you may want. 
Launch System Settings > Shortcut
I change the following:
win l -> lock screen (I swapped mac to the same from old habbits)
ctrl + shift + esc for system activity
win + tab for desktop
ctrl+tab for activities
ctrl+up for all open programs
ctrl+down to show virtual desktops

## Install albert to mimic alfred
alt+space -> run command albert toggle

## Set AutoKey Settings
1. Launch AutoKey
2. Add a Folder and point it to ubuntu-macos-keys/autokey (File -> New -> Folder)
3. Copy all files to your home dir data directory (`cp ubuntu-macos-keys/autokey/* ~/.config/autokey/data/autokey/`)
3. Quit AutoKey and restart (Note: it's not enough to just close the window, you need to close the application by using the Ubuntu toolbar icon in the top right. 

# Make kubuntu look like Mac: (Get used to layout)
https://www.youtube.com/watch?v=uyz4-KZOzyI&list=FLwVK6Jts85b37hV03pxXhAg&index=2&t=0s 
#Also add search widget to menu bar. Change kde logo to apple logo
https://www.google.com/url?sa=i&source=images&cd=&ved=2ahUKEwiQ9LiI3KHjAhVuT98KHYYSBzwQjRx6BAgBEAU&url=https%3A%2F%2Fhetzner.co.za%2Fhelp-centre%2Femail%2Fiphone-ipad-mail-troubleshooting%2F&psig=AOvVaw1jdt99XZ8guPVQBiNzKQOn&ust=1562551400386644
Change icons theme to cupertino-mojave
# Background
http://wallpapersimages.info/wp-content/uploads/HTML/Gif-Wallpapers-Mac/Gif-Wallpapers-Mac-59.html
# Download slingscold to mimic app launcher
# Update terminal to have tabs on top (not bottom, in konsole settings).

# Visual Studio
Add to keybindings.json
// Place your key bindings in this file to override the defaults
[
  { "key": "ctrl+c", "command": "workbench.action.terminal.copySelection", "when": "terminalFocus && terminalTextSelected" },
  { "key": "ctrl+v", "command": "workbench.action.terminal.paste", "when": "terminalFocus" }
] 


# Window Manager Settings (right click main bar on an app and find window manager settings)

## Task Switcher - Alt tab affect:
1. Large Icons

## Screen Edges:
Switch desktop on edge: Only When Moving Windows

## KWin Scripts:
1. MACsimize
1. MinimizeAll



