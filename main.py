# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class FrameWindowTitle
###########################################################################

class FrameWindowTitle(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"VoV Brain Calibrator 2 (v: 0.0.1)",
                          pos=wx.DefaultPosition, sizpe=wx.Size(400, 800),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.Centre(wx.BOTH)
        m_Panel(self)
        self.Show()

    def __del__(self):
        pass


###########################################################################
## Class m_Panel
###########################################################################

class m_Panel(parent=wx.Frame, style=None):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(380, 780),
                          style=wx.TAB_TRAVERSAL)

        b_PanelBox = wx.BoxSizer(wx.VERTICAL)

        self.m_selectDevice = wx.StaticText(self, wx.ID_ANY, u"Select your Device below", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_selectDevice.Wrap(-1)
        b_PanelBox.Add(self.m_selectDevice, 0, wx.TOP | wx.BOTTOM | wx.LEFT, 5)

        m_choiceSelectDevice_ChoiceChoices = [u"Muse 2 (MU03)", u"Muse S", u"Muse 2016 (MU02)", u"Muse 2014 (MU01)"]
        self.m_choiceSelectDevice_Choice = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(380, -1),
                                                     m_choiceSelectDevice_ChoiceChoices, 0)
        self.m_choiceSelectDevice_Choice.SetSelection(0)
        b_PanelBox.Add(self.m_choiceSelectDevice_Choice, 0, wx.ALL, 5)

        self.m_StartStopButton = wx.Button(self, wx.ID_ANY, u"Start Cailbration", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_StartStopButton.SetMinSize(wx.Size(380, -1))

        b_PanelBox.Add(self.m_StartStopButton, 0, wx.ALL, 5)

        fg_EEGValueLoggerBox = wx.FlexGridSizer(2, 2, 0, 0)
        fg_EEGValueLoggerBox.SetFlexibleDirection(wx.HORIZONTAL)
        fg_EEGValueLoggerBox.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        bsizer_RawEEG = wx.BoxSizer(wx.VERTICAL)

        bsizer_RawEEG.SetMinSize(wx.Size(170, -1))
        self.m_RawEEGLabel = wx.StaticText(self, wx.ID_ANY, u"RawEEG", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_RawEEGLabel.Wrap(-1)
        bsizer_RawEEG.Add(self.m_RawEEGLabel, 0, wx.ALL, 5)

        self.m_RawEEG = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.Point(-1, -1), wx.Size(175, 120), 0)
        bsizer_RawEEG.Add(self.m_RawEEG, 0, wx.ALL, 5)

        fg_EEGValueLoggerBox.Add(bsizer_RawEEG, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 5)

        m_Likelihood = wx.BoxSizer(wx.VERTICAL)

        m_Likelihood.SetMinSize(wx.Size(170, -1))
        self.m_LikelihoodLabel = wx.StaticText(self, wx.ID_ANY, u"Likelihood", wx.DefaultPosition, wx.DefaultSize,
                                               0 | wx.TAB_TRAVERSAL)
        self.m_LikelihoodLabel.Wrap(-1)
        m_Likelihood.Add(self.m_LikelihoodLabel, 0, wx.ALL, 5)

        self.m_ProcessedLikelihood = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(175, 120),
                                                 0)
        m_Likelihood.Add(self.m_ProcessedLikelihood, 0, wx.ALL, 5)

        fg_EEGValueLoggerBox.Add(m_Likelihood, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 5)

        b_PanelBox.Add(fg_EEGValueLoggerBox, 0, wx.ALIGN_LEFT, 5)

        b_Log = wx.BoxSizer(wx.VERTICAL)

        self.m_LoggerLabel = wx.StaticText(self, wx.ID_ANY, u"Log", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_LoggerLabel.Wrap(-1)
        b_Log.Add(self.m_LoggerLabel, 0, wx.ALL, 5)

        self.m_CalibratorLog = wx.TextCtrl(self, wx.ID_ANY, u"Calibrator Loaded", wx.DefaultPosition, wx.DefaultSize, 0)
        b_Log.Add(self.m_CalibratorLog, 1, wx.EXPAND, 5)

        self.m_CopyLog = wx.Button(self, wx.ID_ANY, u"Copy Log", wx.DefaultPosition, wx.DefaultSize, 0)
        b_Log.Add(self.m_CopyLog, 0, wx.ALIGN_RIGHT, 5)

        b_PanelBox.Add(b_Log, 1, wx.EXPAND, 5)

        self.SetSizer(b_PanelBox)
        self.Layout()

        # Connect Events
        self.m_choiceSelectDevice_Choice.Bind(wx.EVT_CHOICE, self.OnDevicesChoiceChanged)
        self.m_StartStopButton.Bind(wx.EVT_BUTTON, self.OnStartStopButton_Clicked)
        self.m_RawEEG.Bind(wx.EVT_TEXT, self.OnRawEEGChanged)
        self.m_ProcessedLikelihood.Bind(wx.EVT_TEXT, self.OnLikelilhoodChanged)
        self.m_CalibratorLog.Bind(wx.EVT_TEXT, self.OnLogChanged)
        self.m_CopyLog.Bind(wx.EVT_BUTTON, self.OnCopyLogButtonClicked)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def OnDevicesChoiceChanged(self, event):
        self.m_CalibratorLog.AppendText(self, "\n Using: " + str(self.m_choiceSelectDevice_Choice.GetSelection()))
        event.Skip()
    def OnStartStopButton_Clicked(self, event):
        event.Skip()

    def OnRawEEGChanged(self, event):
        event.Skip()

    def OnLikelilhoodChanged(self, event):
        event.Skip()

    def OnLogChanged(self, event):
        print()
        event.Skip()

    def OnCopyLogButtonClicked(self, event):
        event.Skip()


app = wx.App()
FrameWindowTitle(None)
app.MainLoop()
