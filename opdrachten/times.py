
class Time:
    """
    >>> t = Time("10:31:00")
    >>> print(t)
    10:31:00
    >>> print(t + 90)
    10:32:30
    >>> print(t - 45)
    10:30:15
    >>> print(t.next_hour())
    11:00:00
    >>> print(t.prev_minute())
    10:30:00
    >>> print(t)
    10:31:00
    >>> print(Time("23:59:30") + 60)
    00:00:30
    >>> print(Time("00:00:30") - 60)
    23:59:30
    """

    def __init__(self, time: str):
        hours, minutes, seconds = time.split(":")
        self.hours = int(hours)
        self.minutes = int(minutes)
        self.seconds = int(seconds)

    def __str__(self) -> str:
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def to_seconds(self) -> int:
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def __add__(self, other: int) -> 'Time':
        total = (self.to_seconds() + other) % 86400

        addhours = total // 3600
        addminutes = (total % 3600) // 60
        addseconds = total % 60

        return Time(f"{addhours:02d}:{addminutes:02d}:{addseconds:02d}")

    def __sub__(self, other: int) -> 'Time':
        total = (self.to_seconds() - other) % 86400

        subhours = total // 3600
        subminutes = (total % 3600) // 60
        subseconds = total % 60

        return Time(f"{subhours:02d}:{subminutes:02d}:{subseconds:02d}")
        #je kan het waarschijnlijk ook doen met self.__add__(-other) maar idk met modulo enzo

    def next_hour(self) -> 'Time':
        seconds = (self.hours + 1) * 3600
        return self.__add__(seconds - self.to_seconds())

    def prev_minute(self) -> 'Time':
        seconds = self.to_seconds() - self.seconds - 60
        return self.__add__(seconds - self.to_seconds())


if __name__ == '__main__':
    t = Time("10:31:00")
    print(t + 90)
    print(t - 45)
    print(t.next_hour())
    print(t.prev_minute())
    print(t)
