from typing import Dict


# Flyweight (Intrinsic state)
class CharacterFormat:
    def __init__(self, font: str, size: int, bold: bool, italic: bool):
        self.font = font
        self.size = size
        self.bold = bold
        self.italic = italic

    def __str__(self) -> str:
        style = []
        if self.bold:
            style.append("bold")
        if self.italic:
            style.append("italic")
        style_str = ", ".join(style) if style else "normal"
        return f"Format[font={self.font}, size={self.size}, style={style_str}]"


# Flyweight Factory
class FormatFactory:
    _formats: Dict[str, CharacterFormat] = {}

    @classmethod
    def get_format(cls, font: str, size: int, bold: bool = False, italic: bool = False) -> CharacterFormat:
        """Get or create a character format"""
        # Create a key for the format combination
        key = f"{font}-{size}-{bold}-{italic}"

        # Return existing format if it exists
        if key not in cls._formats:
            cls._formats[key] = CharacterFormat(font, size, bold, italic)

        return cls._formats[key]

    @classmethod
    def format_count(cls) -> int:
        """Return the number of format objects created"""
        return len(cls._formats)


# Context class that contains extrinsic state
class FormattedCharacter:
    def __init__(self, char: str, format_: CharacterFormat):
        self.char = char  # Extrinsic state
        self.format_ = format_  # Reference to flyweight

    def render(self) -> str:
        return f"'{self.char}' with {self.format_}"


# Text editor that uses the flyweight pattern
class TextEditor:
    def __init__(self):
        self.characters: list[FormattedCharacter] = []

    def add_character(self, char: str, font: str, size: int, bold: bool = False, italic: bool = False):
        """Add a character with specified formatting"""
        format_ = FormatFactory.get_format(font, size, bold, italic)
        self.characters.append(FormattedCharacter(char, format_))

    def add_text(self, text: str, font: str, size: int, bold: bool = False, italic: bool = False):
        """Add multiple characters with the same formatting"""
        for char in text:
            self.add_character(char, font, size, bold, italic)

    def display(self):
        """Display the formatted text"""
        for char in self.characters:
            print(char.render())


def main():
    editor = TextEditor()

    # Add some text with different formatting
    print("Adding formatted text to editor...")
    editor.add_text("Hello", "Arial", 12, bold=True)
    editor.add_text(" ", "Arial", 12)
    editor.add_text("World", "Times New Roman", 14, italic=True)
    editor.add_text("!", "Arial", 12, bold=True, italic=True)

    print("\nDisplaying formatted text:")
    editor.display()

    # Show memory savings
    total_chars = len(editor.characters)
    total_formats = FormatFactory.format_count()
    print(f"\nMemory usage statistics:")
    print(f"Total characters: {total_chars}")
    print(f"Unique format objects: {total_formats}")
    print(f"Memory saved: {total_chars - total_formats} format objects")

    # Demonstrate format reuse
    print("\nDemonstrating format reuse:")
    format1 = FormatFactory.get_format("Arial", 12, bold=True)
    format2 = FormatFactory.get_format("Arial", 12, bold=True)
    print(f"Are format objects the same instance? {format1 is format2}")


if __name__ == "__main__":
    main()
