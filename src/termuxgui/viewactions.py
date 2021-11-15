from json import dumps
import base64

from termuxgui.__send_read_msg  import __send_read_msg 
from termuxgui.__send_msg import __send_msg



def showcursor(mainSocket, aid, id, show):
    __send_msg(mainSocket, dumps({"method": "showCursor", "params": {"aid": aid, "id": id, "show": show}}))
    

def deleteview(mainSocket, aid, id):
    __send_msg(mainSocket, dumps({"method": "deleteView", "params": {"aid": aid, "id": id}}))

def clearchildren(mainSocket, aid, id):
    __send_msg(mainSocket, dumps({"method": "deleteChildren", "params": {"aid": aid, "id": id}}))

def settextsize(mainSocket, aid, id, size):
    __send_msg(mainSocket, dumps({"method": "setTextSize", "params": {"aid": aid, "id": id, "size": size}}))



def setimage(mainSocket, aid, id, img):
    '''Sets the image of an imageview. The image has to be a png or jpeg bytes object.'''
    __send_msg(mainSocket, dumps({"method": "setImage", "params": {"aid": aid, "id": id, "img": base64.standard_b64encode(img).decode("ascii")}}))


def setmargin(mainSocket, aid, id, margin, dir=None):
    args = {"aid": aid, "id": id, "margin": margin}
    if dir != None:
        args["dir"] = dir
    __send_msg(mainSocket, dumps({"method": "setMargin", "params": args}))


def setlinearlayoutparams(mainSocket, aid, id, weight):
    __send_msg(mainSocket, dumps({"method": "setLinearLayoutParams", "params": {"aid": aid, "id": id, "weight": weight}}))

def setwidth(mainSocket, aid, id, width):
    __send_msg(mainSocket, dumps({"method": "setWidth", "params": {"aid": aid, "id": id, "width": width}}))

def setheight(mainSocket, aid, id, height):
    __send_msg(mainSocket, dumps({"method": "setHeight", "params": {"aid": aid, "id": id, "height": height}}))

def settext(mainSocket, aid, id, text):
    __send_msg(mainSocket, dumps({"method": "setText", "params": {"aid": aid, "id": id, "text": text}}))


def gettext(mainSocket, aid, id):
    return __send_read_msg(mainSocket, dumps({"method": "getText", "params": {"aid": aid, "id": id}}))

def addbuffer(mainSocket, w, h, format):
    return __send_read_msg(mainSocket, dumps({"method": "addBuffer", "params": {"w": w, "h": h, "format": format}}))

def deleteBuffer(mainSocket, bid):
    __send_msg(mainSocket, dumps({"method": "deleteBuffer", "params": {"bid": bid}}))


def blitbuffer(mainSocket, bid):
    __send_msg(mainSocket, dumps({"method": "blitBuffer", "params": {"bid": bid}}))


def setbuffer(mainSocket, aid, id, bid):
    __send_msg(mainSocket, dumps({"method": "setBuffer", "params": {"aid": aid, "id": id, "bid": bid}}))


def refreshimageview(mainSocket, aid, id):
    __send_msg(mainSocket, dumps({"method": "refreshImageView", "params": {"aid": aid, "id": id}}))



