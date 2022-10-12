from interface import App as _App
from interface import AllTimers as _AllTimers
from interface import Timer as _Timer
from tkinter import *
import time


class App(_App):
    def __init__(self, keys: list):
        root = Tk()
        AllTimers(root, keys)
        root.mainloop()


class AllTimers(_AllTimers):
    def __init__(self, root: Tk, keys: list):
        self.state_all = 1
        self.timers = []

        for index, key in enumerate(keys, 1):
            timer = Timer(root, key, index)
            self.timers.append(timer)
        root.bind('<space>', lambda event: self.show_all_time())

    def __are_states_equal(self) -> None:
        if all([timer.state == self.state_all for timer in self.timers]):
            self.state_all = self.state_all + 1 if self.state_all <= 2 else 1

    def show_all_time(self) -> None:
        self.__are_states_equal()
        for timer in self.timers:
            if timer.state < self.state_all:
                timer.show_time()
        self.state_all = self.state_all + 1 if self.state_all <= 2 else 1


class Timer(_Timer):
    # todo: make properties instead of public variables. Bind T creation
    def __init__(self, root: Tk, key: str, index: int):
        self.__state = 0
        self.__index = index
        self.__time_start = ''
        self.__time_end = ''
        self.__total_seconds = 0
        self.__label = Label(text=f'{index}. timer: 00:00:00', anchor=W, font=24)
        self.__label.pack(side=LEFT, ipadx=10)
        root.bind(key, lambda event: self.show_time())

    @property
    def total_seconds(self):
        return self.__total_seconds

    @total_seconds.setter
    def total_seconds(self, value):
        self.__total_seconds = value

    @property
    def time_end(self):
        return self.__time_end

    @time_end.setter
    def time_end(self, value):
        self.__time_end = value

    @property
    def time_start(self):
        return self.__time_start

    @time_start.setter
    def time_start(self, value):
        self.__time_start = value

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, value):
        self.__state = value

    def show_time(self) -> None:
        if self.state == 0:
            self.state = 1
            time_from = int(time.time())
            self.time_start = time.strftime('%H:%M:%S')
            self.__tick(time_from)
        elif self.state == 1:
            self.state = 2
        elif self.state == 2:
            self.state = 0
            self.__label['text'] = f'{self.__index}. timer: 00:00:00'

    def __tick(self, time_from) -> None:
        # todo: Use datetime to replace everything
        real_time = int(time.time())
        total_seconds = real_time - time_from

        self.__label.config(text=f'{self.__index}. timer: {self.__get_time_string(total_seconds)}')
        if self.state == 1:
            self.__label.after(1000, self.__tick, time_from)
        else:
            self.time_end = time.strftime('%H:%M:%S')
            self.total_seconds = self.__get_time_string(total_seconds)

    @staticmethod
    def __get_time_string(seconds: int) -> str:
        hour = seconds // 3600
        minute = seconds // 60 % 60
        second = seconds % 60
        return f'{hour:02}:{minute:02}:{second:02}'


if __name__ == '__main__':
    App(['1', '2', '3'])
