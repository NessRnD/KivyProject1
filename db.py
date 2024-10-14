import sqlite3

class database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    # Создание новой заметки
    def create_note(self, note_text):
        with self.connection:
            return self.cursor.execute("INSERT INTO notes (note) VALUES (?)", (note_text,))

    # Удаление заметки
    def delete_note(self, note_id):
        with self.connection:
            return self.cursor.execute("DELETE FROM notes WHERE id = ?", (note_id,))

    # Чтение всех заметок
    def read_notes(self):
        with self.connection:
            self.cursor.execute("SELECT id, created_at, note FROM notes")
            notes = self.cursor.fetchall()
            all_notes =''
            for note in notes:
                all_notes += str(note) +'\n'
            return all_notes

    def delete_all_notes(self):
        with self.connection:
            self.cursor.execute("DROP TABLE notes")
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS notes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                    note TEXT
                )
            """)
