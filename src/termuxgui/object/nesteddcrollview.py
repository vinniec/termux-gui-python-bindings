from json import dumps

from termuxgui.__send_read_msg  import __send_read_msg
from termuxgui.__send_msg import __send_msg
from termuxgui.object.framelayout import FrameLayout
from termuxgui.object.viewgroup import ViewGroup

class NestedScrollView(FrameLayout):
    
    def __init__(self, activity, parent=None):
        args = {"aid": activity.aid}
        if parent != None:
            args["parent"] = parent.id
        ViewGroup.__init__(self, activity, __send_read_msg(activity.c._main, dumps({"method": "createNestedScrollView", "params": args})))
    
    
    
 
