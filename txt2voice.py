# complete version
import pyttsx3
import time
import PySimpleGUI as sg
def read_aloud(txt_path=None,interval=2):
    # text in the text path
    dir_path = sg.popup_get_file("Select txt file")
    interval = float(sg.popup_get_text("Please enter interval"))
    if not dir_path:
        sg.popup("Cancel", "No txt file selected")
        raise SystemExit("Cancelling: no txt file selected")
    


    txt_path=dir_path
    with open(txt_path,encoding='utf-8') as f:
        words=f.readlines()
    words=[w.split('\n')[0] for w in words]
    for word in words:
        pyttsx3.speak(word)
        time.sleep(interval)
# read_aloud('chp3_1st_wrong.txt')
read_aloud()
