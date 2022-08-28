# Settings

import playsound
from time import sleep as wait

# Welcome

wait(2)

print('Welcome to our music app!')

wait(2)

print('Here, you can play some music that we have downloaded for you!')

wait(2)

print('But it is okay! Because you can download your OWN music!')

wait(2)

print('Anyways, enjoy your music!')

wait(4)


# App Function

def script():
    m = input('∂p.cmd ')
    if m == 'help':
        print('KING KONG - MHD, ID: MKK34')
        print('Bad Habits - Ed Sheeran, ID: ESBH90')
        print('ILoveUIHateU - Playboi Carti, ID: ILUIHUPC12')
        print('Stay - The Kid LAROI, ID: STKL45')
        print("We Don't Talk Anymore - Charlie Puth, ID: WDTACP93")
        print('Sin Señal - Quevedo, ID: SSQ43')
        print('Use "play:<song id>" to play songs!')
        script()
    if m == 'play:MKK34':
        print('Playing "KING KONG - MHD"')
        playsound.playsound('/Users/nipeal/Desktop/kMusic/p.music/KING KONG - MHD.mp3')
        script()
    if m == 'play:ESBH90':
        print('Playing "Bad Habits - Ed Sheeran"')
        playsound.playsound('/Users/nipeal/Desktop/kMusic/p.music/Ed Sheeran - Bad Habits.mp3')
        script()
    if m == 'play:ILUIHUPC12':
        print('Playing "ILoveUIHateU - Playboi Carti"')
        playsound.playsound('/Users/nipeal/Desktop/kMusic/p.music/Playboi Carti - ILoveUIHateU.mp3')
        script()
    if m == 'play:SSQ43':
        print('Playing "Sin Señal - Quevedo, Ovy on the Drums"')
        playsound.playsound('/Users/nipeal/Desktop/kMusic/p.music/Sin Señal - Quevedo, Ovy on the Drums.mp3')
        script()
    if m == 'play:STKL45':
        print('Playing "Stay - The Kid LAROI"')
        playsound.playsound('/Users/nipeal/Desktop/kMusic/p.music/Stay - The Kid LAROI.mp3')
        script()
    title = "Charlie Puth - We Don't Talk Anymore" # We had to put the title in a variable :)
    if m == 'play:WDTACP93':
        print('Playing "' + title + '"')
        playsound.playsound("/Users/nipeal/Desktop/kMusic/p.music/Charlie Puth - We Don't Talk Anymore.mp3")
        script()
    if m == 'loop:MKK34':
        y_or_n = input('Are you sure you want to loop this song? You will need to restart the script when you want to stop. ')
        if y_or_n == 'yes':
            while True:
                playsound.playsound('/Users/nipeal/Desktop/kMusic/p.music/KING KONG - MHD.mp3')
        elif y_or_n == 'no':
            print('Loading Canceled.')
            script()
    if m == 'loop:ESBH90':
        y_or_n = input('Are you sure you want to loop this song? You will need to restart the script when you want to stop. ')
        if y_or_n == 'yes':
            while True:
                playsound.playsound('/Users/nipeal/Desktop/kMusic/p.music/Ed Sheeran - Bad Habits.mp3')
        elif y_or_n == 'no':
            print('Loading Canceled.')
            script()
    if m == 'loop:ILUIHUPC12':
        yes_or_no = input('Are you sure you want to loop this song? You will need to restart the script when you want to stop. ')
        if yes_or_no == 'yes':
            while True:
                playsound.playsound('/Users/nipeal/Desktop/kMusic/p.music/Playboi Carti - ILoveUIHateU.mp3')
        elif yes_or_no == 'no':
            print('Loading Canceled.')
            script()
    if m == 'loop:SSQ43':
        yes_or_no = input('Are you sure you want to loop this song? You will need to restart the script when you want to stop. ')
        if yes_or_no == 'yes':
            while True:
                playsound.playsound('/Users/nipeal/Desktop/kMusic/p.music/Sin Señal - Quevedo, Ovy on the Drums.mp3')
        elif yes_or_no == 'no':
            print('Loading Canceled.')
            script()
    if m == 'loop:STKL45':
        yes_or_no = input('Are you sure you want to loop this song? You will need to restart the script when you want to stop. ')
        if yes_or_no == 'yes':
            while True:
                playsound.playsound('/Users/nipeal/Desktop/kMusic/p.music/Stay - The Kid LAROI.mp3')
        elif yes_or_no == 'no':
            print('Loading Canceled.')
            script()
    if m == 'loop:WDTACP93':
        yes_or_no = input('Are you sure you want to loop this song? You will need to restart the script when you want to stop. ')
        if yes_or_no == 'yes':
            while True:
                playsound.playsound("/Users/nipeal/Desktop/kMusic/p.music/Charlie Puth - We Don't Talk Anymore.mp3")
        elif yes_or_no == 'no':
            print('Loading Canceled.')
            script()
# app.Start()

script()
