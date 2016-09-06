
import alsaaudio as aa
import decoder
import os


class MusicManager():

    def __init__(self):

        self.current_song = None

        self.current_queue = []

        self.shuffle = False

        self.output_driver_driver = aa.PCM(
            aa.PCM_PLAYBACK, aa.PCM_NORMAL, card="hw:0")
        self.output_driver.setchannels(2)
        self.output_driver.setformat(aa.PCM_FORMAT_S16_LE)
        # self.output_driver.setperiodsize(chunk)
        # self.output_driver.setrate(rate)

    def getSong(self, path):
        header = False

        if any([ax for ax in [".mp4", ".m4a", ".m4b"] if ax in path]):
            header = True

        return decoder.open(path, header)

    def playSong(self, file):
        pass
