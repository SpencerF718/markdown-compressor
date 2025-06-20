import os


def get_markdown_files(obsidian_vault):

    markdown_files = []

    for current_directory, _, filenames_in_current_directory in os.walk(obsidian_vault):
        for filename in filenames_in_current_directory:
            if filename.endswith(".md"):
                full_path = os.path.join(current_directory, filename)
                markdown_files.append(full_path)

    return markdown_files


def write_markdown_files(decompressed_folder, relative_filepath, decompressed_content):

    decompressed_full_path = os.path.join(
        decompressed_folder, relative_filepath)
    decompressed_directory = os.path.dirname(decompressed_full_path)

    os.makedirs(decompressed_directory, exist_ok=True)

    with open(decompressed_full_path, "w", encoding="utf-8") as temp:
        temp.write(decompressed_content)
