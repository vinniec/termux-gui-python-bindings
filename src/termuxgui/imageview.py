import base64
from json import dumps

from termuxgui.view import View

class ImageView(View):
    
    def __init__(self, activity, parent=None):
        args = {"aid": activity.aid}
        if parent != None:
            args["parent"] = parent.id
        View.__init__(self, activity, activity.c.send_read_msg({"method": "createImageView", "params": args}))
    
    
    
    def setimage(self, img):
        self.a.c.send_msg({"method": "setImage", "params": {"aid": self.a.aid, "id": self.id, "img": base64.standard_b64encode(img).decode("ascii")}})
    
    def setbuffer(self, b):
        self.a.c.send_msg({"method": "setImage", "params": {"aid": self.a.aid, "id": self.id, "bid": b.bid}})
    
    def refresh(self):
        self.a.c.send_msg({"method": "setImage", "params": {"aid": self.a.aid, "id": self.id}})
    
