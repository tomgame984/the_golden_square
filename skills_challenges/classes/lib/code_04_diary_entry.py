import math

class DiaryEntry:
    def __init__(self, title, contents):
        self._title = title
        self._contents = contents
        self._contents_list = contents.split()
        self._accumulated_chunk_length = 0

    def format(self):
        return f"{self._title}: {self._contents}."

    def count_words(self):
        return len(self._contents_list)

    def reading_time(self, wpm):
        minutes = math.ceil(self.count_words()/wpm)
        return f"Estimated reading time: {minutes} minute(s)"

    def reading_chunk(self, wpm, minutes):
        chunk_length = wpm * minutes
        if self._accumulated_chunk_length >= self.count_words():
            self._accumulated_chunk_length = 0

        chunk_start = self._accumulated_chunk_length
        chunk_end = self._accumulated_chunk_length+chunk_length
        chunk = self._contents_list[chunk_start:chunk_end]
        self._accumulated_chunk_length = chunk_end
        return " ".join(chunk)
    