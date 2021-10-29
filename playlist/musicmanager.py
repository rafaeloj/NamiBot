from pytube import YouTube
from playlist import playlist as pl
# from discord import 
import os

MUSIC_DIR = "/mnt/datawindows/Users/rafae/Documents/discord_bot/songs/"
class MusicManager():
    def __init__(self, playlist=pl.PlayList()):
        self.__pl = playlist

    @property
    def pl(self):
        return self.__pl
    @property
    def music(self):
        return self.pl.current_music
    @property
    def now(self):
        return self.__pl.current_music_title
    def __str__(self):
        return self.__pl.__str__()
    def __getitem__(self,index):
        return self.__pl[index]
    def download(self, index):
        """
            index: It's the music index on self.__pl to download
        """
        # Formats the song title to the way it was saved
        musics = os.listdir(MUSIC_DIR)
        music_name = "_".join(self.__pl[index].title.split(" ")).upper()+".mp4"
        if music_name not in musics:
            self.__pl[index].streams.filter(only_audio=True).first().download(MUSIC_DIR,filename=music_name)

    def add_music(self,url):
        """
            url: It's the youtube music link 
        """
        music = YouTube(url)
        if len(self.__pl) <= 3:
            self.__pl.add(music)
            self.download(-1)
            return
        self.__pl.add(music)

    def next(self):
        self.__pl.next()
        if self.__pl.current_index+2 < len(self.__pl):
            self.download(self.__pl.current_index+2)
        # if self.__pl.current_index > 2:
        #     self.__pl.rm_music(0)
        #     os.remove(f"/mnt/c/Users/rafae/Documents/discord_bot/songs/{self.now}")

    def prev(self):
        try:
            self.__pl.prev()
            return True
        except IndexError:
            return False

    def finished(self):
        return True if len(self.__lg)-1 == self.__lg.current_index else False


def main():
    pl = PlayList()
    mm = MusicManager(pl)

    mm.add_music(YouTube("https://www.youtube.com/watch?v=7zok9co_8E4"))
    mm.add_music(YouTube("https://www.youtube.com/watch?v=fUpdfpOPf4Y"))
    mm.add_music(YouTube("https://www.youtube.com/watch?v=fPO76Jlnz6c"))
    mm.add_music(YouTube("https://www.youtube.com/watch?v=RRHmy56Ir40"))

if __name__ == '__main__':
    main()
