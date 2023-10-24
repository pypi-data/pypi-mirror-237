"""Module providing the MusicManager class"""
import os
import logging
import sqlite3
from pathlib import Path
from ._file import File as F

class MusicManager():
    """Class to manage finding media files within a directory"""
    app_name = 'MusicManagerMicro'
    default_root_dir = os.path.join(str(Path.home()), ".config/", app_name)
    library_file = 'library.db'
    library_dir = ''
    library = ''
    logging.basicConfig(
        format='%(asctime)s | %(levelname)s | %(message)s', level=logging.DEBUG)
    DEBUG = False

    def __debug_message(self, message):
        if self.DEBUG:
            logging.debug(str(message))

    def __init__(self, library):
        self.library = library
        self.set_library(self.library)

    def instantiate_sqlite_table(self, file_name: str) -> sqlite3.Cursor:
        """Sets up the required sqlite db"""
        con = sqlite3.connect(file_name)
        cur = con.cursor()
        res = cur.execute("SELECT ? FROM sqlite_master", ('music',))
        is_created = res.fetchone()
        if is_created is None:
            cur.execute("CREATE TABLE music(mtime, file_path type UNIQUE)")
        return cur

    def db_get_all(self, cur: sqlite3.Cursor) -> list:
        """Returns all values from the current db"""
        res = cur.execute("SELECT * FROM music")
        ret_val = res.fetchall()
        # print(f'db_get_all ret val {ret_val}')
        return [] if ret_val is None else ret_val

    def db_insert(self, cur: sqlite3.Cursor, entry: tuple):
        """Places an entry into the db with two values
        mtime and file_path from the tuple
        will match on file_path to update existing rows"""
        sub_obj = {
            'mtime': entry[0],
            'file_path': entry[1]
        }
        cur.execute("""
                    INSERT INTO music(mtime,file_path) 
                    VALUES (:mtime, :file_path) 
                    ON CONFLICT(file_path) 
                    DO UPDATE SET mtime=:mtime, file_path=:file_path
                    """,
                      sub_obj)

    def db_delete(self, cur: sqlite3.Cursor) -> None:
        """Performs a delete on all rows in the music db"""
        cur.execute("DELETE FROM music")

    def db_commit(self, sql_con: sqlite3.Connection) -> None:
        """Commits all outstanding statements"""
        sql_con.commit()

    def db_close(self, sql_con: sqlite3.Connection) -> None:
        """Closes the connection"""
        sql_con.close()

    ###
    # Config manager
    ###

    def set_library(self, library_id: str) -> None:
        """Updates the current library to be used"""
        self.library = library_id
        self.__update_root_dir()

    def _construct_library_dir(self, library) -> str:
        return os.path.join(
            self.default_root_dir, library)

    def __update_root_dir(self) -> None:
        self.library_dir = self._construct_library_dir(self.library)
        os.makedirs(self.library_dir, exist_ok=True)

    library_root = ''

    ###
    # Utils
    ###
    extensions = ('.mp3', '.flac')

    def get_files_from_folder(self, folder: str) -> list:
        """Returns the list of all files recursively in a directory"""
        ret_val = []
        for r, _, f in os.walk(folder):
            for file in f:
                if file.endswith(self.extensions):
                    ret_val.append(f'{r}/{file}')
        return ret_val

    ###
    # Program Functions
    ###

    library_list = []

    def build_entry(self, file_path: str) -> tuple | None:
        """docstring"""
        try:
            file = F(file_path, '', '', os.path.getmtime(file_path))
            return (file.mtime, file.path)
        except FileNotFoundError as err:
            self.__debug_message(f"Error in build_entry {err=}, {type(err)=}")
            return None

    def build_list(self, root_path: str) -> list:
        """Given a path string constructs a list of File objects"""
        self.library_list = []
        # return library_list
        files = self.get_files_from_folder(root_path)
        self.__debug_message(f"Found {len(files)} files")
        for f in files:
            # __debugMessage(f)
            self.library_list.append(self.build_entry(f))
        # __save_list()
        return self.library_list


    def execute(self, library: str, root_path: str) -> list:
        """Main entry function for the MusicManager, takes a library name
          and the root directory to search from"""
        self.set_library(library)
        return_value = self.build_list(root_path)
        self.__save_list()
        return return_value

    def reset_library(self, library: str) -> None:
        """Takes the current library db and clears all rows"""
        self.set_library(library)
        _file = self.__build_file_path()
        cur = self.instantiate_sqlite_table(_file)
        self.db_delete(cur)
        self.db_commit(cur.connection)
        self.db_close(cur.connection)

    def get_list(self) -> list:
        """Returns the list for the set library without running the search"""
        self.__load_list()
        return self.library_list

    def __build_file_path(self) -> str:
        return os.path.join(self.library_dir, self.library_file)

    def __load_list(self) -> None:
        _file = self.__build_file_path()
        cur = self.instantiate_sqlite_table(_file)
        self.library_list = self.db_get_all(cur)

    def __save_list(self) -> None:
        """Uses a filepath + filename string and content string overwrites the resulting file"""
        content = self.library_list
        write_file = self.__build_file_path()
        if os.path.dirname(write_file) != '':
            os.makedirs(os.path.dirname(write_file), exist_ok=True)
        cur = self.instantiate_sqlite_table(write_file)
        for x in content:
            self.__debug_message(f'Inserting {x}')
            self.db_insert(cur, x)
        self.db_commit(cur.connection)
        self.db_close(cur.connection)
