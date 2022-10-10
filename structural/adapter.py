"""
Adapter pattern works as a bridge between two incompatible interfaces. This pattern involves a single class which is
responsible to join functionalities of independent or incompatible interfaces.
A real life example could be a case of  card reader which acts as an adapter between memory card and a laptop. We
plug in the memory card into card reader and card reader into the laptop so that memory card can be read via laptop.
"""
from abc import abstractmethod, ABCMeta


class MediaPlayer(metaclass=ABCMeta):
    @abstractmethod
    def play(self, filename):
        pass


class AdvanceMediaPlayer(metaclass=ABCMeta):
    @abstractmethod
    def play_vlc(self, filename):
        pass

    @abstractmethod
    def play_mp4(self, filename):
        pass


class MediaAdapter(MediaPlayer):
    def __init__(self):
        self.advance_audio_player = AdvanceAudioPlayer()

    def play(self, filename):
        if filename.endswith('vlc'):
            self.advance_audio_player.play_vlc(filename)
        elif filename.endswith('mp4'):
            self.advance_audio_player.play_mp4(filename)


class AdvanceAudioPlayer(AdvanceMediaPlayer):
    def play_vlc(self, filename: str):
        print(f'Playing Vlc File: {filename}')

    def play_mp4(self, filename: str):
        print(f'Playing MP4 File: {filename}')


class AudioPlayer(MediaPlayer):
    def __init__(self):
        self.media_adapter = MediaAdapter()

    def play(self, filename: str):
        if filename.endswith('mp3'):
            print(f'Playing MP3 File: {filename}')
        else:
            self.media_adapter.play(filename)


if __name__ == '__main__':
    audio_player = AudioPlayer()

    audio_player.play('naat.mp3')
    audio_player.play('noha.mp4')
    audio_player.play('hamd.vlc')
    audio_player.play('mangabat.mp3')
