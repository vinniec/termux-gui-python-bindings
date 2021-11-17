from json import dumps


from termuxgui.task import Task


class Activity:
    def __init__(self, connection, tid=None, dialog=None, pip=False, overlay=None, lockscreen=None, canceloutside=True):
        self.c = connection
        params = {"canceloutside": canceloutside}
        if dialog != None:
            params["dialog"] = dialog
        if tid != None:
            params["tid"] = tid
        if pip != None:
            params["pip"] = pip
        if overlay != None:
            params["overlay"] = overlay
        if lockscreen != None:
            params["lockscreen"] = lockscreen
        if tid == None:
            self.aid, tid = self.c.send_read_msg({"method": "newActivity", "params": params})
        else:
            self.aid = self.c.send_read_msg({"method": "newActivity", "params": params})
        self.t = Task(connection, tid)
        if self.aid == -1:
            raise RuntimeError("Could not create Activity")
    
    
    def finish(self):
        '''Finishes an Activity.'''
        self.c.send_msg({"method": "finishActivity", "params": {"aid": self.aid}})
    
    
    def setinputmode(mode):
        '''Sets the input mode for an Activity.'''
        self.c.send_msg({"method": "setInputMode", "params": {"aid": self.aid, "mode": mode}})
    
    def keepscreenon(on):
        self.c.send_msg({"method": "keepScreenOn", "params": {"aid": self.aid, "on": on}})
    
    def setpipmode(self, pip):
        self.c.send_msg({"method": "setPiPMode", "params": {"aid": self.aid, "pip": pip}})
    
    def setpipmodeauto(self, pip):
        self.c.send_msg({"method": "setPiPModeAuto", "params": {"aid": self.aid, "pip": pip}})
    
    def setpipparams(self, num, den):
        '''Sets the PiP parameters for the Activity, the aspect ration.'''
        self.c.send_msg({"method": "setPiPParams", "params": {"aid": self.aid, "num": num, "den": den}})
    
    def settaskdescription(self, text, img):
        '''Sets the Task icon. img has to be a PNG or JPEG image as a base64 encoded string.'''
        self.c.send_msg({"method": "setTaskDescription", "params": {"aid": self.aid, "img": img, "label": text}})
    
    def settheme(self, statusbarcolor, colorprimary, windowbackground, textcolor, coloraccent):
        '''Sets the Theme fro an Activity.'''
        self.c.send_msg({"method": "setTheme", "params": {"aid": self.aid, "statusBarColor": statusbarcolor, "colorPrimary": colorprimary, "windowBackground": windowbackground, "textColor": textcolor, "colorAccent": coloraccent}})
    
    def setorientation(orientation):
        self.c.send_msg({"method": "setOrientation", "params": {"aid": self.aid, "orientation": orientation}})
    
    
    

    def setposition(x, y):
        self.c.send_msg({"method": "setPosition", "params": {"aid": self.aid, "x": x, "y": y}})



    def sendoverlayevents(send):
        self.c.send_msg({"method": "sendOverlayTouchEvent", "params": {"aid": self.aid, "send": send}})
    
    
    
    

