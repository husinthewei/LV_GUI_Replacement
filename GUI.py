import wx
class MyFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(900, 950))
        self.MainPanel = wx.Panel(self, -1)
        self.panel1 = wx.Panel(self.MainPanel, -1, style = wx.SUNKEN_BORDER)
        self.panel2 = wx.Panel(self.MainPanel, -1, size=(758, 180), style = wx.SUNKEN_BORDER)
        self.CreateMainPanel1()
        self.CreateMainPanel2()
        self.Create_Layout()
        self.MainPanel.SetSizer(self.sizer)

    #This creates the layout for the two main panels. The first main panel contains 4 smaller panels and the second main panel contains 1 smaller panel
    def Create_Layout(self):
        # 3x3 array, with 2 pixel spacing in both directions for the panels. 7 of the panels will be spacers
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
        
        self.SubPanel1 = wx.Panel(self.panel1, -1, size=(400, 260), style = wx.RAISED_BORDER)
        self.SubPanel2 = wx.Panel(self.panel1, -1, size=(350, 260), style = wx.RAISED_BORDER)
        self.SubPanel3 = wx.Panel(self.panel1, -1, size=(400, 260), style = wx.RAISED_BORDER)
        self.SubPanel4 = wx.Panel(self.panel1, -1, size=(350, 260), style = wx.RAISED_BORDER)

        self.CreateSubPanel1()
        self.CreateSubPanel2()
        
        sizer.Add(self.SubPanel1)
        sizer.Add(self.SubPanel2)
        sizer.Add(self.SubPanel3)
        sizer.Add(self.SubPanel4)
        
        self.panel1.SetSizer(sizer)

    def CreateSubPanel1(self):
        sizer = wx.FlexGridSizer(2,2,20,40);
        
	label = wx.StaticText(self.SubPanel1, label="string to sort")
	sizer.Add(label)
	label = wx.StaticText(self.SubPanel1, label="PrunedData")
	sizer.Add(label)
	
        self.StringToSort = wx.TextCtrl(self.SubPanel1, 1, "",wx.Point(20,20), wx.Size(175, 205),wx.TE_MULTILINE |  wx.TE_READONLY)
        #whenever you want to add text to this TextCtrl, use self.StringToSort.AppendText(""). Check ADDSTS() for an example.
        self.AddSTS()
	sizer.Add(self.StringToSort)	
	
        self.PrunedData = wx.TextCtrl(self.SubPanel1, 1, "",wx.Point(20,20), wx.Size(175,205),wx.TE_MULTILINE |  wx.TE_READONLY)
        #whenever you want to add text to this TextCtrl, use self.PrunedData.AppendText(""). Check ADDSTS() for an example.		
	sizer.Add(self.PrunedData)
	
	self.SubPanel1.SetSizer(sizer)
	
	
    def AddSTS(self):
         for i in range(30):
            self.StringToSort.AppendText("Sample Text %d \n"%i)

    def CreateSubPanel2(self):
        #You may want to play around with the sizer spacing, or even make spacer panels, to make it look better
        #The parameters for this sizer are (rows, columns, vertical spacing, and horizontal spacing)
        sizer = wx.FlexGridSizer(5,2, 40, 40)
        
        self.ADD = wx.TextCtrl(self.SubPanel2, style = wx.TE_PROCESS_ENTER, size=(90,20))
        self.ADD.Bind(wx.EVT_TEXT_ENTER, self.OnEnterADD, self.ADD)
        #For this text box, pressing enter triggers self.OnEnterAdd(). Check that function at the bottom.
        sizer.Add(self.ADD)   
        
        label = wx.StaticText(self.SubPanel2, label="ADD#")
        sizer.Add(label)
        
        self.SortedData = wx.TextCtrl(self.SubPanel2, style = wx.TE_PROCESS_ENTER, size=(90,20))
        self.SortedData.Bind(wx.EVT_TEXT_ENTER, self.OnEnterSD, self.SortedData)         
        #For this text box, pressing enter triggers self.OnEnterSD(). Check that function at the bottom.
        sizer.Add(self.SortedData)
        
        label = wx.StaticText(self.SubPanel2, label="Sorted Data")
        sizer.Add(label)
        
        #To add the other boxes, repeat what I did with the previous two boxes.
        
        self.SubPanel2.SetSizer(sizer)
        
    def CreateSubPanel3(self):
        print "In 3"
        
    def CreateSubPanel4(self):
        print "In 4"

    def CreateMainPanel2(self):
        #There is only one panel here, so there is no need for a new sizer
        print "InPanel2"    

    def OnEnterADD(self, event):
        print self.ADD.GetValue()
    def OnEnterSD(self, event):
        print self.SortedData.GetValue()        
        
class MyApp(wx.App):
     def OnInit(self):
         frame = MyFrame(None, -1, 'GUI.py')
         frame.Show(True)
         return True

if __name__ == '__main__':
    app = MyApp(0)
    app.MainLoop()