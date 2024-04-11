# DJ_helper
Ten kod sprawdza każdą piosenkę w bazie danych i zwraca tytuł najdłuższej piosenki, której długość odtwarzania nie przekracza zadanej liczby sekund. Jeśli nie ma takiej piosenki, zwraca wartość False.
#
This code checks each song in the database and returns the title of the longest song that has a playback length of less than a given number of seconds. If there is no such song, it returns False.
#
#
#
Funkcja get_song przyjmuje dwa argumenty: db, który jest bazą danych piosenek, oraz len_seconds, który jest maksymalną długością piosenki wyrażoną w sekundach.

Inicjalizujemy zmienną longest_song na wartość None. Ta zmienna będzie przechowywać najdłuższą piosenkę spełniającą warunki.

Następnie przechodzimy przez każdą piosenkę w bazie danych db przy użyciu pętli for.

Dla każdej piosenki obliczamy długość odtwarzania playback_time w sekundach, konwertując godziny na minuty i dodając je do sekund z minut.

Sprawdzamy, czy długość odtwarzania nie przekracza wartości len_seconds. Jeśli tak, przechodzimy do następnego kroku. W przeciwnym razie, porównujemy ją z długością odtwarzania najdłuższej znalezionej piosenki.

Jeśli longest_song jest None (czyli nie znaleźliśmy jeszcze żadnej piosenki spełniającej warunek), lub jeśli playback_time dla bieżącej piosenki jest większa od długości odtwarzania najdłuższej piosenki, aktualizujemy longest_song na bieżącą piosenkę.

Po przejściu przez wszystkie piosenki, sprawdzamy, czy znaleźliśmy jakąkolwiek piosenkę, która spełnia warunki. Jeśli tak, zwracamy łańcuch znakowy zawierający nazwę artysty i tytuł najdłuższej piosenki w formacie "Best possible song: {artist}/{title}". W przeciwnym razie zwracamy wartość False.

Na końcu wywołujemy funkcję get_song z przykładową bazą danych songs_db i maksymalną długością piosenki 145 sekund, a następnie wyświetlamy wynik.
#
#
We initialize the longest_song variable to None. This variable will store information about the longest song whose playback length does not exceed the specified len_seconds value.

It iterates through each song in the songs_db list.

For each song, its playing time in seconds is calculated. The playback length is taken from the 'playback' key in the HH:MM format and converted to a number of seconds.

We check whether the song playback length does not exceed the len_seconds value. If so, we move on to the next song. If not, we move on to the next step.

We update the value of longest_song if the current song is longer than the previously stored song. This condition is checked based on the playing time of the current song.

After iterating through all songs, we return the title of the longest song, if one is found. If no song matching the criteria is found, we return False.

