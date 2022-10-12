from abc import ABC, abstractmethod
from tkinter import Tk


class App(ABC):
    @abstractmethod
    def __init__(self):
        """
        Main class which connects everything
        """


class AllTimers(ABC):
    @abstractmethod
    def __init__(self):
        """
        Container for all the timers
        """

    @abstractmethod
    def __are_states_equal(self) -> None:
        """
        Checks if states of timers are equal

        :return: None
        """

    @abstractmethod
    def show_all_time(self) -> None:
        """
        Shows time of all the timers in the class

        :return: None
        """


class Timer(ABC):
    @abstractmethod
    def __init__(self, root: Tk, key: str, index: int):
        """
        Creates timer

        :param root: main window where timers will be placed
        :param key: key on the keyboard which will control timer
        :param index: timer index
        """

    @property
    @abstractmethod
    def state(self):
        """
        State of the timer. 0 if it was not started. 1 if it is going. 2 if it is stopped

        :return: int. Should be 0 or 1 or 2
        """

    @state.setter
    @abstractmethod
    def state(self, value):
        """
        State of the timer. 0 if it was not started. 1 if it is going. 2 if it is stopped

        """

    @property
    @abstractmethod
    def total_seconds(self):
        """
        Number of time timer was running

        :return: "HH:MM:SS"
        """

    @total_seconds.setter
    @abstractmethod
    def total_seconds(self, value):
        """
        Number of time timer was running

        """

    @property
    @abstractmethod
    def time_end(self):
        """
        Time in which timer stopped to run

        :return: "HH:MM:SS"
        """

    @time_end.setter
    @abstractmethod
    def time_end(self, value):
        """
        Time in which timer stopped to run

        """

    @property
    @abstractmethod
    def time_start(self):
        """
        Time in which timer started to run

        :return: "HH:MM:SS"
        """

    @time_start.setter
    @abstractmethod
    def time_start(self, value):
        """
        Time in which timer started to run

        """

    @abstractmethod
    def show_time(self) -> None:
        """
        Shows time on timer

        :return: None
        """

    @abstractmethod
    def __tick(self, time_from) -> None:
        """
        Change seconds on timer

        :param time_from: in seconds
        :return: None
        """

    @staticmethod
    @abstractmethod
    def __get_time_string(seconds: int) -> str:
        """
        Converts second in time

        :param seconds: int
        :return: "hh.mm.ss"
        """
