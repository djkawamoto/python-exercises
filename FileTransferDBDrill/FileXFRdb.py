# !usr/local/bin/python2
# File_XFR_UI.py
# This drill uses wxPython which is intended to be used with Python 2.7

from __future__ import unicode_literals
import os
import wx
import wx.lib.agw.multidirdialog as MDD
import shutil
import time


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
        global source_folder
        dlg = MDD.MultiDirDialog(self, title="Choose a directory to check for changes:",
                                 defaultPath=self.currentDirectory,
                                 agwStyle=0)
        if dlg.ShowModal() == wx.ID_OK:
            source_folder = dlg.GetPaths()
            print source_folder
        dlg.Destroy()

    def ToButton(self, event):
        global destination_folder
        dlg = MDD.MultiDirDialog(self, title="Choose the location to copy files TO:",
                                 defaultPath=self.currentDirectory,
                                 agwStyle=0)
        if dlg.ShowModal() == wx.ID_OK:
            destination_folder = dlg.GetPaths()
            print destination_folder
        dlg.Destroy()

    def CheckButton(self, event):
        #Source
        global source_folder
        print source_folder
        #Destination
        global destination_folder
        print destination_folder

        now = int(time.time())
        fileCount = 0


        
        for _file in os.listdir(str(source_folder)):

            ###
            ### NEED TO CHANGE THE LOGIC HERE TO INCLUDE dB data
            ###

            print ("\n\n")
            print (_file)
            print (os.path.getmtime(_file))
            #print (os.stat(source_folder))
            #print (os.stat(os.path(source_folder)))
            #print (os.stat(os.path(source_folder)).st_mtime)

            if int(os.stat(os.path(source_folder)).st_mtime) > (now - 86400):
                shutil.copy2(source_folder+'%s' % _file, dst+'%s' % _file)
                fileCount += 1
                print fileCount, " files copied."
            else:
                print "No new files or modified files were found."
                
        # BELOW IS JUST A COPY OF WHAT'S ABOVE,PRIOR TO MAKING CHANGES - FOR REFERENCE
        # for _file in source_folder:
        #     ###
        #     ### NEED TO CHANGE THE LOGIC HERE TO INCLUDE dB data
        #     ###
        #     if int(os.stat(os.path.abspath(source_folder+'%s' % _file)).st_mtime) > (now - 86400):
        #         shutil.copy2(source_folder+'%s' % _file, dst+'%s' % _file)
        #         fileCount += 1
        #         print fileCount, " files copied."
        #     else:
        #         print "No new files or modified files were found." #add logic for False

    def Quit(self, event):
        self.Close()

def main():
    app = wx.App()
    windowClass(None)

    app.MainLoop()

if __name__ == "__main__":
    main()
