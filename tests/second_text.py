import os
import subprocess
from ebooklib import epub

def change_author(input_ebook_path, cover, output_ebook_path):
    try:
        # Use ebook-convert to change the author
        subprocess.run(['ebook-convert', input_ebook_path, output_ebook_path, '--cover', cover], check=True)
        print(f'Successfully changed the author of the e-book to {cover}.')
    except subprocess.CalledProcessError as e:
        print(f'Error changing the author: {e}')

# Example usage:
if __name__ == "__main__":
    input_ebook_path = "/Users/michaelarens/Desktop/teee/testmobi2.zip"  # Replace with the actual path of your input e-book
    output_ebook_path = "/Users/michaelarens/Desktop/teee/testmobi4.mobi"  # Replace with the actual path of your input e-book
    cover = "/Users/michaelarens/Desktop/teee/testmobi/cover.png"  # Replace with the actual path of your input e-book
    title = "New Book Title"
    converted_ebook_path = change_author(input_ebook_path, cover, output_ebook_path)
    if converted_ebook_path:
        # Now, you can use the method from the previous responses to send the converted e-book to your Kindle.
        # send_to_kindle(converted_ebook_path, "/path/to/your/kindle/mounted/folder")
        pass
