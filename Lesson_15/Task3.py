CHANNELS = ["BBC", "Discovery", "TV1000"]

class TVController:

    def __init__(self, channels):
        self.channels = channels

    def first_channel(self):
        self.the_channel = self.channels[0]
        print(self.the_channel)

    def last_channel(self):
        self.the_channel = self.channels[-1]
        print(self.the_channel)

    def turn_channel(self, channel_n):
        self.the_channel = self.channels[channel_n-1]
        print(self.the_channel)

    def next_channel(self):
        if self.channels.index(self.the_channel) == len(self.channels)-1:
            self.the_channel = self.channels[0]
            print(self.the_channel)
        else:
            self.the_channel = self.channels[self.channels.index(self.the_channel)+1]
            print(self.the_channel)

    def previous_channel(self):
        if self.channels.index(self.the_channel) == 0:
            self.the_channel = self.channels[-1]
            print(self.the_channel)
        else:
            self.the_channel = self.channels[self.channels.index(self.the_channel) - 1]
            print(self.the_channel)

    def current_channel(self):
        print(self.the_channel)

    def is_exist(self, channel):
        if channel in self.channels or channel in range(1, len(self.channels)+1):
            print('Yes')
        else:
            print('No')


controller = TVController(CHANNELS)
controller.first_channel()
controller.last_channel()
controller.turn_channel(1)
controller.next_channel()
controller.previous_channel()
controller.current_channel()
controller.is_exist(4)
controller.is_exist("BBC")











