from lib.code_04_diary_entry import *


# When an entry is created with a title and contents
# The entry is reflected in the format attribute
def test_format_entry_with_title_and_contents():
    entry = DiaryEntry('Friday', 'Another week is completed')
    assert entry.format() == "Friday: Another week is completed."

# When an entry is created with a title and contents
# The word count is reflected in the count_words attribute
def test_word_count_for_contents():
    entry = DiaryEntry('Friday', 'Another week is completed')
    assert entry.count_words() == 4



# When an entry is created with a title and contents
# And we provide the wpm value
# The reading time is reflected in the reading_time attribute
def test_reading_time_with_1_wpm_and_5_words_in_content_string():
    entry = DiaryEntry('My Title', 'one two three four five')
    assert entry.reading_time(1) == "Estimated reading time: 5 minute(s)"


# When an entry is created with a title and contents
# And we provide the wpm value and the time the user has available to read.
# It returns a section of the entry based the WPM and time available.
# If the reading_chunk attribute is called again, the next section should be returned.
# This will continue until the entire entry has been returned and it will then return the beginning of the entry.
def test_chunk_read_for_wpm_of_1_and_2_minutes():
    entry = DiaryEntry('My Title', 'one two three four five')
    assert entry.reading_chunk(1, 2) == "one two"

def test_recalled_chunk():
    entry = DiaryEntry('My Title', 'one two three four five')
    assert entry.reading_chunk(1, 2) == "one two"
    assert entry.reading_chunk(1, 1) == "three"
    assert entry.reading_chunk(2, 1) == "four five"

def test_recalled_chunk_and_return_to_contents_start():
    entry = DiaryEntry('My Title', 'one two three four five')
    assert entry.reading_chunk(1, 2) == "one two"
    assert entry.reading_chunk(2, 2) == "three four five"
    assert entry.reading_chunk(1, 2) == "one two"

