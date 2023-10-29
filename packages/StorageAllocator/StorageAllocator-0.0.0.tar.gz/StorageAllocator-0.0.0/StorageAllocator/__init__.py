from typing import Union


class Allocator:
    def __init__(self, amount: int = 1024) -> None:
        """
        Initialize the Allocator.

        :param amount: Initial data amount in bytes.
        """
        self.data = 0
        try:
            with open(".allocate", "r") as f:
                self.data = len(f.read())
        except FileNotFoundError:
            self.allocate(amount)

    def deallocate(self, amount: int = 1024) -> bool:
        """
        Deallocate a specified amount of data.

        :param amount: The amount of data to deallocate in bytes.
        :return: True if the deallocation is successful, False if it's not.
        """
        if (self.data - amount) >= 0:
            self.data -= amount
            self._loca()
            return True

        return False

    def allocate(self, amount: int = 1024) -> bool:
        """
        Allocate a specified amount of data.

        :param amount: The amount of data to allocate in bytes.
        :return: True if the allocation is successful, False if it's not.
        """
        if amount > 0:
            self.data += amount
            self._loca()
            return True

        return False

    def writeFile(self, data: Union[bytes, str] = "data", name: str = "filename.txt", byte: bool = False) -> bool:
        """
        Write data to a file.

        :param data: The data to write to the file.
        :param name: The name of the file to write to.
        :param byte: If True, data is treated as bytes.
        :return: True if writing the file is successful, False if it's not.
        """
        if self.deallocate(len(data)):
            if byte:
                if isinstance(data, bytes):
                    with open(name, "wb") as f:
                        f.write(data)
            else:
                if isinstance(data, str):
                    with open(name, "w") as f:
                        f.write(data)

            return True

        return False

    def _loca(self) -> None:
        """
        Update the .allocate file with 'a' characters to represent the current data size.
        """
        with open(".allocate", "w") as f:
            f.write("a" * self.data)

    @staticmethod
    def B(amount: int = 1) -> int:
        """
        Convert an amount to bytes.

        :param amount: The amount to convert.
        :return: The amount in bytes.
        """
        return amount

    def KB(self, amount: int = 1) -> int:
        """
        Convert an amount to kilobytes (KB).

        :param amount: The amount to convert.
        :return: The amount in kilobytes.
        """
        return self.B(amount) * 1024

    def MB(self, amount: int = 1) -> int:
        """
        Convert an amount to megabytes (MB).

        :param amount: The amount to convert.
        :return: The amount in megabytes.
        """
        return self.KB(amount) * 1024

    def GB(self, amount: int = 1) -> int:
        """
        Convert an amount to gigabytes (GB).

        :param amount: The amount to convert.
        :return: The amount in gigabytes.
        """
        return self.MB(amount) * 1024
