import os
from .file_manager import get_markdown_files


def get_character_frequency(obsidian_vault):

    char_frequencies = {}
    markdown_file_paths = get_markdown_files(obsidian_vault)

    for file_path in markdown_file_paths:
        with open(file_path, 'r', encoding='utf-8') as temp:
            markdown_content = temp.read()
            for char in markdown_content:
                char_frequencies[char] = char_frequencies.get(char, 0) + 1

    return char_frequencies
