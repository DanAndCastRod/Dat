import wx
class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, -1, title)
        btn = wx.Button(self, -1, "Hola")
        self.Bind(wx.EVT_BUTTON, self.say_hello, btn)

    def say_hello(self, *arg):
        print("Hola Mundo")

class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None, "Simple wxPython App")
        frame.Show(True)

        return True

MyApp().MainLoop()