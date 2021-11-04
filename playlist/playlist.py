from pytube import YouTube

class PlayList():
    def __init__(self):
        self.__songs   = []
        self.__current = 0
        self.__size = 0
        
    def __str__(self):
        output_string = ""
        for i, music in enumerate(self.__songs):
                output_string += f"***{i}*** - {music.title}\n"
        return output_string

    def __getitem__(self,index):
        return self.__songs[index]

    @property
    def current_index(self):
        return self.__current

    @property
    def current_music(self):
        return self.__songs[self.__current]
    @property
    def current_music_title(self):
        return "_".join(self.__songs[self.__current].title.split(" ")).upper()+".mp4"
        
    def __len__(self):
        return self.__size

    def next(self):
        if self.__current < self.__size:
            self.__current += 1
            return self.__songs[self.__current]
        raise IndexError("Não há mais musica na lista")

    def prev(self):
        if self.__current > 0:
            self.__current -= 1
            return self.__songs[self.__current]
        raise IndexError("Não há músicas anteriores")
    def add(self,url):
        self.__size += 1
        self.__songs.append(url)

    def rm_music(self,index):
        del self.__songs[index]
        self.__size = len(self.__songs)
        if index < self.__current:
            self.__current -= 1

    def mv_music(self,index_A, index_B):
        tmp_song = self.__songs[index_A]
        self.__songs.insert(index_A,self.__songs[index_B])
        self.__songs.pop(index_A+1)
        self.__songs.insert(index_B,tmp_song)
        self.__songs.pop(index_B+1)

if __name__ == "__main__":
    main()
