# File_XFR_UI.py
# This is uses wxPython which is intended to be used with Python 2.7

import os
import wx
import wx.lib.agw.multidirdialog as MDD

# THIS IS A PLACEHOLDER FOR THE ASSUMED PRE-EXISTING CODE
# These would likely be imported from a separate module, but 
#for the sake of this drill dummy functions are below.
def checks_for_changes_in_folder():
    pass
    
def copies_files_to_new_location():
    pass

class windowClass(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(windowClass, self).__init__(*args, **kwargs)
        self.currentDirectory = os.getcwd()
        self.gui()
    
    def gui(self):
        panel = wx.Panel(self)
        menuBar = wx.MenuBar()
        
        #This creates the necessary menu(s)
        fileMenu = wx.Menu()
        #ADD "Change 'From' folder..."
        changeFromFolderItem = wx.MenuItem(fileMenu, wx.ID_ANY,
                                           'Change &From Folder...\tCtrl+F')
        fileMenu.AppendItem(changeFromFolderItem)
        #ADD "Change 'to' folder...
        changeToFolderItem = wx.MenuItem(fileMenu, wx.ID_ANY,
                                         'Change &To Folder...\tCtrl+T')
        fileMenu.AppendItem(changeToFolderItem)
        #ADD "Check files"
        checkFilesItem = wx.MenuItem(fileMenu, wx.ID_ANY,
                                     'Chec&k Files\tCtrl+K')
        fileMenu.AppendItem(checkFilesItem)
        #EXIT function
        exitItem = wx.MenuItem(fileMenu, wx.ID_ANY, '&Quit\tCtrl+Q')
        fileMenu.AppendItem(exitItem)
        
        #attaches menu items to the menu
        menuBar.Append(fileMenu, '&File')
        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU, self.FromButton, changeFromFolderItem)
        self.Bind(wx.EVT_MENU, self.ToButton, changeToFolderItem)
        self.Bind(wx.EVT_MENU, self.CheckButton, checkFilesItem)
        self.Bind(wx.EVT_MENU, self.Quit, exitItem)
        
        #TOOLBAR W/ ICONS: This creates a tool bar with icons.
        toolBar = self.CreateToolBar(style=(wx.TB_HORZ_LAYOUT | wx.TB_TEXT))
        toolBar.SetToolBitmapSize((32,32))
        #FROM FOLDER button
        fromFolderButton = toolBar.AddLabelTool(wx.ID_ANY, 'Change From Folder',
                                                wx.Bitmap('from.png'))
        self.Bind(wx.EVT_TOOL, self.FromButton, fromFolderButton)
        #TO FOLDER button
        toFolderButton = toolBar.AddLabelTool(wx.ID_ANY, 'Change To Folder',
                                              wx.Bitmap('to.png'))
        self.Bind(wx.EVT_TOOL, self.ToButton, toFolderButton)
        #CHECK FILES button
        checkFilesButton = toolBar.AddLabelTool(wx.ID_ANY, 'Check Files',
                                                wx.Bitmap('check.png'))
        self.Bind(wx.EVT_TOOL, self.CheckButton, checkFilesButton)
        
        toolBar.Realize()
        
        self.SetTitle('File Transfer GUI Drill Window')
        self.Show(True)
        
    #BUTTON FUNCTIONS
    def FromButton(self, event):
        dlg = MDD.MultiDirDialog(self, title="Choose a directory to check for changes:",
                                 defaultPath=self.currentDirectory,
                                 agwStyle=0)
        if dlg.ShowModal() == wx.ID_OK:
            paths = dlg.GetPaths()
            print "You chose the following file(s):"
            for path in paths:
                print path
        dlg.Destroy()
        
    def ToButton(self, event):
        dlg = MDD.MultiDirDialog(self, title="Choose the location to copy files TO:",
                                 defaultPath=self.currentDirectory,
                                 agwStyle=0)
        if dlg.ShowModal() == wx.ID_OK:
            paths = dlg.GetPaths()
            print "You chose the following file(s):"
            for path in paths:
                print path
        dlg.Destroy()
    
    def CheckButton(self, event):
        print "Theoretically checking for files..."
        checks_for_changes_in_folder()
        print "Files have been checked."
        if 1 == 1:
            print "Theoretically copying files to new location..."
            copies_files_to_new_location()#add logic for True
            print "Files have been copied."
            okBox = wx.MessageDialog(None, 'Your files have been copied.', 'Status', wx.OK)
            okBox.ShowModal()
            okBox.Destroy()
        else: 
            print "No new files or modified files were found." #add logic for False

    def Quit(self, event):
        self.Close()
    
def main():
    app = wx.App()
    windowClass(None)

    app.MainLoop()

if __name__ == "__main__":
    main()













































