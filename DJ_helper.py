def get_song(db, len_seconds):
    # Inicjalizacja zmiennej przechowującej najdłuższą piosenkę
    longest_song = None
    
    # Iteracja przez każdą piosenkę w bazie danych
    for song in db:
        # Obliczenie długości odtwarzania piosenki w sekundach
        playback_time = int(song['playback'][:2]) * 60 + int(song['playback'][3:])
        
        # Sprawdzenie, czy długość odtwarzania piosenki nie przekracza podanej wartości
        if playback_time <= len_seconds:
            # Jeśli najdłuższa piosenka jest None lub bieżąca piosenka jest dłuższa niż najdłuższa dotychczasowa
            if longest_song is None or playback_time > int(longest_song['playback'][:2]) * 60 + int(longest_song['playback'][3:]):
                # Aktualizacja najdłuższej piosenki
                longest_song = song
    
    # Jeśli znaleziono najdłuższą piosenkę, zwróć jej tytuł i artystę w odpowiednim formacie
    if longest_song:
        return "Best possible song: {}/{}/{}".format(longest_song['artist'], longest_song['title'], longest_song['playback'])
    else:
        # W przeciwnym razie zwróć False
        return False

# Przykładowe dane wejściowe
songs_db = [ {
 'artist': 'Led Zeppelin', 
 'title': 'Stairways to heaven', 
 'playback': '09:20' 
}, {
 'artist': 'Metallica', 
 'title': 'Master of puppets', 
 'playback': '04:30' 
}, {
 'artist': 'Nirvana', 
 'title': 'The Man who sold the world', 
 'playback': '03:10' 
}, {
 'artist': 'Stepan Galyabarda', 
 'title': 'Lyst do mamy', 
 'playback': '02:20' 
}]

# Wywołanie funkcji i wyświetlenie wyniku
print(get_song(songs_db, 145))
