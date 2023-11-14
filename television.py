class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self.__muted = False
        self.__status = False
        self.__channel = Television.MIN_CHANNEL
        self.__volume = Television.MIN_VOLUME

    def power(self):
        if not self.__status:
            self.__status = True
        else:
            self.__status = False

    def mute(self) -> None:
        if not self.__muted:
            self.__muted = True
        else:
            self.__muted = False

    def channel_up(self):
        if self.__status:
            if self.__channel <= Television.MAX_VOLUME:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self):
        if self.__status:
            if self.__channel >= Television.MIN_VOLUME:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_VOLUME

    def volume_up(self):
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self):
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        if self.__muted:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
