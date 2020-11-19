class Track:

    def __init__(self, track_title, track_duration):
        self.track_title = track_title
        self.track_duration = track_duration

    def show(self):
        return (f'{self.track_title}: {self.track_duration}')

    def count_track_time(self):
        return self.track_duration

    def __repr__(self):
        return f'{self.track_title}: {self.track_duration}'


track_1_1 = Track('Всё, что касается', 3)
track_1_2 = Track('О любви', 4)
track_1_3 = Track('Океаны', 5)

track_2_1 = Track('Я сошла с ума', 4)
track_2_2 = Track('Нас не догонят', 5)
track_2_3 = Track('Робот', 4)

# print(Track.show(track_1_1))
# print(track_1_1.show())


class Album:

    def __init__(self, album_title, band):
        self.album_title = album_title
        self.band = band
        self.track_list = []

    # def add_track(self, track_name, track_time):
    #     new_track = [track_name, track_time]
    #     self.track_list.append(new_track)

    def add_track(self, new_track):
        self.track_list.append(new_track)

    def get_tracks(self):
        for element in self.track_list:
            print(element.show())

    def get_duration(self):
        album_duration = 0
        for element in self.track_list:
            album_duration += element.count_track_time()
        print(f'Длительность альбома {self.album_title}: {album_duration} минут')

    def __repr__(self):
        return f'Альбом: {self.album_title}, Исполнитель {self.band}, Треки: {self.track_list}, '


album_1 = Album('Районы-кварталы', 'Звери')
album_2 = Album('200 по встречной', 'Тату')

album_1.add_track(track_1_1)
album_1.add_track(track_1_2)
album_1.add_track(track_1_3)

album_2.add_track(track_2_1)
album_2.add_track(track_2_2)
album_2.add_track(track_2_3)

# album_1.add_track(track_1_1.track_title, track_1_1.track_duration)
# album_1.add_track(track_1_2.track_title, track_1_2.track_duration)
# album_1.add_track(track_1_3.track_title, track_1_3.track_duration)
# album_2.add_track(track_2_1.track_title, track_2_1.track_duration)
# album_2.add_track(track_2_2.track_title, track_2_2.track_duration)
# album_2.add_track(track_2_3.track_title, track_2_3.track_duration)

print(album_1.__repr__())
print(album_2.__repr__())

print()

album_1.get_tracks()
album_2.get_tracks()

print()

album_1.get_duration()
album_2.get_duration()

# print(album_1.album_title)
# print(album_1.band)
# print(album_1.track_list)
#
# print(album_2.album_title)
# print(album_2.band)
# print(album_2.track_list)





