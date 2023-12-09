from PyQt6.QtWidgets import *
from gui import *

class Logic(QMainWindow, Ui_MainWindow):

    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.__status = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL

        '''Gui linked buttons and their functions'''

        self.onButton.clicked.connect(lambda :self.On())
        self.offButton.clicked.connect(lambda :self.Off())

        self.volumeUpButton.clicked.connect(lambda: self.Vup())
        self.volumeDownButton.clicked.connect(lambda: self.Vdown())

        self.channelUpButton.clicked.connect(lambda: self.Cup())
        self.channelDownButton.clicked.connect(lambda: self.Cdown())

        self.muteButton.clicked.connect(lambda: self.Mute())


    '''On function for changing the status variable from False to True'''
    def On(self) -> None:
        if self.__status == False:
            self.label.setText(f'Channel, {self.MIN_CHANNEL} Volume {self.MIN_VOLUME}')
            self.__status = True
        else:
            pass
    '''Off function for turning the status variable from True to False'''
    def Off(self) -> None:
        if self.__status == True:
            self.__status = False
            self.label.setText(f'')
        else:
            pass
    "Volume Up function for turning the volume variable up"
    def Vup(self) -> None:
        if self.__status == True:
            self.__muted = False
            if self.__volume < self.MAX_VOLUME:
                self.__volume += 1
                self.label.setText(f'Channel, {self.__channel} Volume {self.__volume}')
            else:
                self.__volume = self.MAX_VOLUME
                self.label.setText(f'Channel, {self.__channel} Volume {self.__volume}')
        else:
            pass
    '''Volume down function for turning the volume variable down'''
    def Vdown(self) -> None:
        if self.__status == True:
            self.__muted = False
            if self.__volume == self.MIN_VOLUME:
                self.__volume = self.MIN_VOLUME
                self.label.setText(f'Channel, {self.__channel} Volume {self.__volume}')
            else:
                self.__volume -= 1
                self.label.setText(f'Channel, {self.__channel} Volume {self.__volume}')
        else:
            pass
    '''Channel up function for turning the channel variable up'''
    def Cup(self) -> None:
        if self.__status == True and self.__muted == False:
            if self.__channel < self.MAX_CHANNEL:
                self.__channel += 1
                self.label.setText(f'Channel, {self.__channel} Volume {self.__volume}')
            else:
                self.__channel = self.MIN_CHANNEL
                self.label.setText(f'Channel, {self.__channel} Volume {self.__volume}')
        elif self.__status == True and self.__muted == True:
            if self.__channel < self.MAX_CHANNEL:
                self.__channel += 1
                self.label.setText(f'Channel, {self.__channel} Volume 0')
            else:
                self.__channel = self.MIN_CHANNEL
                self.label.setText(f'Channel, {self.__channel} Volume 0')
        else:
            pass
    '''Channel down function for turning the channel variable down'''
    def Cdown(self) -> None:
        if self.__status == True and self.__muted == False:
            if self.__channel == self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL
                self.label.setText(f'Channel, {self.__channel} Volume {self.__volume}')
            else:
                self.__channel -= 1
                self.label.setText(f'Channel, {self.__channel} Volume {self.__volume}')
        if self.__status == True and self.__muted == True:
            if self.__channel == self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL
                self.label.setText(f'Channel, {self.__channel} Volume 0')
            else:
                self.__channel -= 1
                self.label.setText(f'Channel, {self.__channel} Volume 0')
        else:
            pass
    '''Mute function for toggling the mute variable True and False'''
    def Mute(self) -> None:
        if self.__status == True:
            if self.__muted == False:
                self.__muted = True
                self.label.setText(f'Channel, {self.__channel} Volume 0')
            elif self.__muted == True:
                self.__muted = False
                self.label.setText(f'Channel, {self.__channel} Volume {self.__volume}')
        else:
            pass




