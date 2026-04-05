"""
Source id: 4 # Personal reference.
This is based on my understanding of the problem. Unfortunately, the explanation was convoluted and not well written,
leaving certain aspects up to interpretation.
We have gained access to a remote filesystem obtained a list of files that we can read.
The files contain pieces of the system's root password.
The contents of each file are all the same length, the length of the password.
The files contain alphanumeric characters and dots. If a character is alphanumeric, it means that is a character that
goes in the password at that location. If a character is a dot, we don't have that character.
In addition to the list of files, we have another list specifying which files we have read already and the contents of
the file. Each list element is a string with this format:
"<path_to_read_file_n> <password_fragment>"
We want to issue commands to the system to either
- read another file from the list (to get more pieces of the password) "READ <path/to/next_file_to_read>"
- get root access privileges "ROOT <password>"
Each time we call the function issue_command(), we should get either the next READ command to issue or the ROOT command
with the full password.
Example:
    We are given:
    files = [
        "/home/user/my_file.txt",
        "/home/user/notes.txt",
        "/home/user/Documents/important.txt",
        "/home/user/Videos/fun_stuff.txt"
    ]
    read_files = [
        "/home/user/my_file.txt ....ord...456"
        "/home/user/notext.txt ......d123...",
    ]

    We haven't seen yet:
      - the contents of the file "/home/user/Documents/important.txt" are "Pas.....12...6
      - the contents of the file "/home/user/Videos/fun_stuff.txt" are "...sWo........"

    From this, we know that
    - we have read two files and thus far have the following characters in the password ....ord123456.
    - we are missing the first four characters of the password.
    - the fragments can contain overlapping characters.

    What the output should be at each call
        1. "READ /home/user/Documents/important.txt"
        2. "READ /home/user/Videos/fun_stuff.txt"
        3. "ROOT PassWord123456"
"""
from typing import List

def issue_command(files: List[str], files_read: List[str]) -> List[str]:
    pass

if __name__ == "__main__":
    # For simplicity, we are going to simulate filenames and contents with a dictionary, which would make "reading"
    # files a trivial matter. This functionality was not part of the original problem.

    pass


