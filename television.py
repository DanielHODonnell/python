class Television:
    """
    This class represents a Television with attributes: power, channel, and volume.
    """
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """
        Initializes the television object.
        """
        self.__muted = False
        self.__status = False
        self.__channel = Television.MIN_CHANNEL
        self.__volume = Television.MIN_VOLUME

    def power(self) -> None:
        """
        Turns the television on or off.
        """
        if not self.__status:
            self.__status = True
        else:
            self.__status = False

    def mute(self) -> None:
        """
        Mutes and unmutes the television.
        """
        if self.__status:
            if not self.__muted:
                self.__muted = True
            else:
                self.__muted = False

    def channel_up(self) -> None:
        """
        Changes channel to the next channel up.
        If channel has reached the maximum channel (3),
        it will go back to the minimum channel (0)
        """
        if self.__status:
            self.__channel = (self.__channel + 1) % (Television.MAX_CHANNEL + 1)

    def channel_down(self) -> None:
        """
        Changes channel to the next channel down.
        If channel has reached the minimum channel (3),
        it will go back to the maximum channel (0)
        """
        if self.__status:
            self.__channel = (self.__channel - 1) % (Television.MAX_CHANNEL + 1)

    def volume_up(self) -> None:
        """
        Increases the volume by one.
        """
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self):
        """
        Decreases the volume by one.
        """
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Returns a string representation of the television object
        """
        if self.__muted:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = 0'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
