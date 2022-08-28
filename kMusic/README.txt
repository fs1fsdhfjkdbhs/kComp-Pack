Hello and thank you for installing and using kMusic! We
are pretty sure that you have heard that you can put your own
music here, you can but you will need the following:

    1. PyInstaller Downloaded on the Terminal
    2. A simple PyInstaller command, type (pyinstaller --onefile ignore.py)

If you already have those, then you can start!

First, you need to actually download your song. If your song is from YouTube, you can use this link:
    en.onlinevideoconverter.pro
    Basically how this works is you get the link of your song and paste it into the text box.

Then what you have to do is to move the song into the 'p.music' folder.

After you've done that, go to the 'scripts' folder and open 'main.py', then write the following under
'def script():':

            if m == 'play:your song':
                print('Playing "your song"') -- This is optional, no need to enter this
                playsound.playsound("your song's path") -- This is to play the song
                script() -- This is so that you can run another script without needing to re-run the script

And there you go! You're done!


Now, you might get confused on where the app actually is. Just open the 'dist' folder and run the Terminal


