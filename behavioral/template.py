"""
- Create templates in case of same problems with different details. Example: PPT presentation slide template
"""
from abc import ABCMeta, abstractmethod


class DeviceTest(metaclass=ABCMeta):  # Template class
    def test(self):  # Template method
        # Hook Methods
        self._electric_test()
        self._mechanical_test()
        self._radio_test()
        self._audio_test()

    def generate_report(self):
        self._gather_results()
        self._cleanup()
        self._create_summary()
        self._print()

    @abstractmethod
    def _electric_test(self):
        pass

    @abstractmethod
    def _mechanical_test(self):
        pass

    @abstractmethod
    def _radio_test(self):
        pass

    @abstractmethod
    def _audio_test(self):
        pass

    @abstractmethod
    def _gather_results(self):
        pass

    @abstractmethod
    def _cleanup(self):
        pass

    @abstractmethod
    def _create_summary(self):
        pass

    @abstractmethod
    def _print(self):
        pass


class Device1Test(DeviceTest):
    def _electric_test(self):
        print(f"Device 1: Electric Test")

    def _mechanical_test(self):
        print(f"Device 1: Mechanical Test :: Step 1")
        print(f"Device 1: Mechanical Test :: Step 2")

    def _radio_test(self):
        print(f"Device 1: Radio Test")

    def _audio_test(self):
        print(f"Device 1: Audio Test")

    def _gather_results(self):
        print(f"Device 1: Gathering results")

    def _cleanup(self):
        print(f"Device 1: Cleanup results")

    def _create_summary(self):
        print(f"Device 1: Creating summary")

    def _print(self):
        print(f"Device 1: Printing test report")


class Device2Test(DeviceTest):
    def _electric_test(self):
        print(f"Device 2: Electric Test")

    def _mechanical_test(self):
        print(f"Device 2: Mechanical Test :: Step 1")
        print(f"Device 2: Mechanical Test :: Step 2")

    def _radio_test(self):
        print(f"Device 2: Radio Test :: Step 1")
        print(f"Device 2: Radio Test :: Step 2")

    def _audio_test(self):
        print(f"Device 2: Audio Test")

    def _gather_results(self):
        print(f"Device 2: Gathering results")

    def _cleanup(self):
        print(f"Device 2: Cleanup results")

    def _create_summary(self):
        print(f"Device 2: Creating summary")

    def _print(self):
        print(f"Device 2: Printing test report")


if __name__ == '__main__':
    print("#################### DEVICE - 1 ####################")
    device_1_test = Device1Test()
    device_1_test.test()
    device_1_test.generate_report()

    print("#################### DEVICE - 2 ####################")
    device_2_test = Device2Test()
    device_2_test.test()
    device_2_test.generate_report()
