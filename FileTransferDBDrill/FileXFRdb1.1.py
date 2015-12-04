# !usr/local/bin/python2
# FileXFRdb1.1.py
# by Daniel Kawamoto

import os
import wx
import shutil
import time
import datetime
import dbFunctions as db


class Frame(wx.Frame):

    def __init__(self, title):
        wx.Frame.__init__(self, None, title=title, size=(650, 250))
        panel = wx.Panel(self)
        self.currentDirectory = os.getcwd()

        # Create Menu Bar
        menuBar = wx.MenuBar()
        fileMenu = wx.Menu()
        exitItem = fileMenu.Append(wx.NewId(), "&Exit")
        originItem = fileMenu.Append(wx.NewId(), '&Origin folder...')
        destinationItem = fileMenu.Append(wx.NewId(), '&Destination folder...')
        executeItem = fileMenu.Append(
            wx.NewId(), 'E&xecute file check/transfer')
        menuBar.Append(fileMenu, '&File')

        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU, self.exitProgram, exitItem)
        self.Bind(wx.EVT_MENU, self.selectOrigin, originItem)
        self.Bind(wx.EVT_MENU, self.selectDestination, destinationItem)
        self.Bind(wx.EVT_MENU, self.transferFiles, executeItem)

        # Setup file transfer UI
        # TEXT FOR DISPLAYING LAST FILE TRANSFER time
        self.most_recent_entry = db.mostRecentEntry()
        lastTime = "... actually it hasn't happened yet (because the FUTURE)."
        if not self.most_recent_entry:
            pass
        else:
            lastTime = self.most_recent_entry
        currently = datetime.datetime.fromtimestamp(
            int(time.time())).strftime('%H:%M:%S %m-%d-%Y')
        wx.StaticText(panel, label='It is currently ' +
                      currently, pos=(30, 15))
        wx.StaticText(
            panel, label='The last file transfer occurred at ' + lastTime, pos=(30, 30))

        # SET UP BUTTON/TEXT BOX FOR SELECTING "FROM" FOLDER
        originButton = wx.Button(
            panel, label="Select Origin Folder", pos=(30, 70))
        originButton.Bind(wx.EVT_BUTTON, self.selectOrigin, originButton)
        self.originPath = wx.TextCtrl(panel, size=(
            400, -1), pos=(220, 70), style=wx.TE_READONLY)

        # SET UP BUTTON/TEXT BOX FOR SELECTING "TO" FOLDER
        destinationButton = wx.Button(
            panel, label="Select Destination Folder", pos=(30, 100))
        destinationButton.Bind(
            wx.EVT_BUTTON, self.selectDestination, destinationButton)
        self.destinationPath = wx.TextCtrl(panel, size=(
            400, -1), pos=(220, 100), style=wx.TE_READONLY)

        # SET UP BUTTON FOR EXECUTING THE PROGRAM
        transferFilesButton = wx.Button(
            panel, label="Transfer Files", pos=(250, 150))
        transferFilesButton.Bind(
            wx.EVT_BUTTON, self.transferFiles, transferFilesButton)

    def exitProgram(self, event):
        self.Destroy()

    # Allows user to select the folder they would like to check for recently
    # modified files
    def selectOrigin(self, event):
        dlg = wx.DirDialog(self, "Choose a directory to check for changes.",
                           defaultPath=self.currentDirectory, style=wx.DD_DEFAULT_STYLE)
        if dlg.ShowModal() == wx.ID_OK:
            self.origin_folder = dlg.GetPath()
            self.originPath.AppendText(self.origin_folder)
        dlg.Destroy()

    # Allows the user to select the folder they would like files to bec
    # transferred to
    def selectDestination(self, event):
        dlg = wx.DirDialog(self, "Choose a directory to copy modified files to.",
                           defaultPath=self.currentDirectory, style=wx.DD_DEFAULT_STYLE)
        if dlg.ShowModal() == wx.ID_OK:
            self.destination_folder = str(dlg.GetPath())
            self.destinationPath.AppendText(self.destination_folder)
        dlg.Destroy()

    # Executes the file check/transfer process
    def transferFiles(self, event):
        # keeps a count of the files in the origin folder
        self.numFiles = 0
        # keeps a count of the number of files transferred
        self.filesTransferred = 0
        # gets the unix timestamp from the database for the most recent file
        # transfer
        self.mostRecentUnix = db.mostRecentUnix()
        # iterates through the selected directory
        for _file in os.listdir(self.origin_folder):
            self.numFiles += 1
            if int(os.stat(os.path.abspath(self.origin_folder + '/%s' % _file)).st_mtime) > self.mostRecentUnix:
                shutil.copyfile(self.origin_folder + '/%s' %
                                _file, self.destination_folder + '/%s' % _file)
                self.filesTransferred += 1
        if self.filesTransferred > 0:
            db.addEntry()
            wx.MessageBox('File check and transfer complete. ' + str(self.numFiles) +
                          ' files checked and ' + str(self.filesTransferred) + ' files copied.', 'Success!', wx.OK)
        else:
            wx.MessageBox('There were no recently modified files in the specified folder.',
                          'Hmm... have you been working?', wx.OK)


app = wx.App()
frame = Frame("Daily File Transfer Program")
frame.Show()
app.MainLoop()
