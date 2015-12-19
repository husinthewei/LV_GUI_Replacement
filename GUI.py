import wx
class MyFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(700, 900))
        self.MainPanel = wx.Panel(self, -1)
        self.panel1 = wx.Panel(self.MainPanel, -1, size=(580, 470), style = wx.SUNKEN_BORDER)
        self.panel2 = wx.Panel(self.MainPanel, -1, size=(580, 180), style = wx.SUNKEN_BORDER)
        self.CreateMainPanel1()
        self.CreateMainPanel2()
        self.Create_Layout()
        self.MainPanel.SetSizer(self.sizer)

    #This creates the layout for the two main panels. The first main panel contains 4 smaller panels and the second main panel contains 1 smaller panel
    def Create_Layout(self):

        
        # 3x3 array for the panels. 7 of the panels will be spacers
        self.sizer = wx.FlexGridSizer(3, 3, 2, 2)
        
        #adding 3 empty(spacer) panels at the top to center the main panels
        self.sizer.Add(wx.Panel(self.MainPanel, -1,  size=(18, 88)))
        self.sizer.Add(wx.Panel(self.MainPanel, -1,  size=(18, 88)))
        self.sizer.Add(wx.Panel(self.MainPanel, -1,  size=(18, 88))) 
        
        #adding 1 empty(spacer) panel to left to center main panels  
        self.sizer.Add(wx.Panel(self.MainPanel, -1,  size=(58, 8)))        
        
        #adding first main panel     
        self.sizer.Add(self.panel1, 1)
        
        #adding 1 empty(spacer) panel to right to center main panels  
        self.sizer.Add(wx.Panel(self.MainPanel, -1,  size=(8, 8)))
        
        #adding 1 empty(spacer) panel to left to center main panels  
        self.sizer.Add(wx.Panel(self.MainPanel, -1,  size=(50, 0)))   
                
        #adding second main panel        
        self.sizer.Add(self.panel2, 1)
        
        #adding 1 empty(spacer) panel to right to center main panels  
        self.sizer.Add(wx.Panel(self.MainPanel, -1,  size=(0, 0)))   
        
    def CreateMainPanel1(self):
        sizer = wx.FlexGridSizer(2, 2, 4, 4)
        #self.SubPanel1 = wx.Panel(self.MainPanel, -1, size=(580, 470), style = wx.SUNKEN_BORDER)
        sizer.Add(wx.Panel(self.panel1, -1, size=(370, 230), style = wx.RAISED_BORDER))
        sizer.Add(wx.Panel(self.panel1, -1, size=(176, 230), style = wx.RAISED_BORDER))
        sizer.Add(wx.Panel(self.panel1, -1, size=(300, 230), style = wx.RAISED_BORDER))
        sizer.Add(wx.Panel(self.panel1, -1, size=(0, 0), style = wx.RAISED_BORDER))
        self.panel1.SetSizer(sizer)

    def CreateMainPanel2(self):
        #There is only one panel here, so there is no need for a new sizer
        print "InPanel2"    

class MyApp(wx.App):
     def OnInit(self):
         frame = MyFrame(None, -1, 'wxBoxSizer.py')
         frame.Show(True)
         return True
app = MyApp(0)
app.MainLoop()