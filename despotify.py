# A small python script for muting the speaker when an annoying audio ad starts to play in Spotify's Desktop App and resuming once the ad ends.

import time
import pyautogui


def start_spotify_func():
    import subprocess
    subprocess.call([r'start_spotify.bat'])


def locateIcon(icon):
    try:
        img = pyautogui.locateCenterOnScreen(f'{icon}')
        return img
    except TypeError:
        pass


def clickSpeaker(sX, sY):
    pyautogui.click(x=sX, y=sY)


def is_there_an_advert():
    for ad_symbol in ad_symbols:
        advert_playing = locateIcon(ad_symbol)
        if advert_playing is not None:
            time.sleep(0.25)
            # in case it catches it incorrectly
            advert_playing = locateIcon(ad_symbol)
            if advert_playing is not None:
                break
    return advert_playing


def play_spotify():
    my_x, my_y = pyautogui.position()
    try:
        sX, sY = locateIcon('screenshots/play_button.png')
        print("Playing...")
        clickSpeaker(sX, sY)
        pyautogui.moveTo(my_x, my_y)
    except TypeError:
        print("Already playing")


def unmute_spotify():
    my_x, my_y = pyautogui.position()
    try:
        sX, sY = locateIcon('screenshots/muted_speakerBtn.png')
        print("Unmuting")
        clickSpeaker(sX, sY)
        pyautogui.moveTo(my_x, my_y)
        sX, sY = locateIcon('screenshots/muted_speakerBtn.png')
        if sX is not None:
            sX_temp = sX + 125
            pyautogui.moveTo(sX_temp, sY)
            pyautogui.click(sX_temp, sY)
        pyautogui.moveTo(my_x, my_y)
    except TypeError:
        pass


ad_symbols = ['screenshots/ad30.png', 'screenshots/ad29.png',
              'screenshots/ad25.png', 'screenshots/ad16.png',
              'screenshots/ad20.png', 'screenshots/ad28.png',
              'screenshots/ad15.png', 'screenshots/ad22.png',
              'screenshots/ad26.png']


# Driver Code
start_spotify_func()
time.sleep(10)
play_spotify()
unmute_spotify()

spotify_is_on = True
print("Scanning for those shite adverts...")

while spotify_is_on:

    advert_playing = is_there_an_advert()

    if advert_playing is not None:
        print('Ad found, trying to mute')
        my_x, my_y = pyautogui.position()

        try:
            sX, sY = locateIcon('screenshots/speakerBtn.png')
            clickSpeaker(sX, sY)
            pyautogui.moveTo(my_x, my_y)
            advert_playing = is_there_an_advert()
            while advert_playing is not None:
                time.sleep(1)
                advert_playing = is_there_an_advert()
            my_x, my_y = pyautogui.position()
            start_spotify_func()
            clickSpeaker(sX, sY)
            pyautogui.moveTo(my_x, my_y)

        except TypeError:
            print('Speaker button out of range')
            pyautogui.moveTo(my_x, my_y)

    elif advert_playing is None:
        unmute_spotify()
