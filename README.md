# Morse Code Converter

A simple Python program to convert text to Morse code and decode Morse code back to text.

## Features

- **Encode**: Convert English text into Morse code.
- **Decode**: Translate Morse code back into readable text.
- Simple and easy-to-use interface.
- 100% Python implementation.

## Usage

1. Clone the repository:
    ```
    git clone https://github.com/ivantsowlad/Morse-Code.git
    ```

2. Run the main Python script:
    ```bash
    python morse_code.py
    ```

3. Follow the on-screen prompts to encode or decode messages.

## Example

### Encoding
Input:
```
HELLO WORLD
```

Output:
```
.... . .-.. .-.. --- / .-- --- .-. .-.. -..
```

### Decoding
Input:
```
.... . .-.. .-.. --- / .-- --- .-. .-.. -..
```

Output:
```
HELLO WORLD
```

## How It Works

- The program uses a dictionary to map letters and numbers to their Morse code equivalents.
- When encoding, each character is converted to Morse code separated by spaces. Words are separated by `/`.
- When decoding, the process is reversed to obtain the original text.

## Requirements

- Python 3.x

No external dependencies are required.

## Contributing

Pull requests are welcome! If you find a bug or want a new feature, feel free to open an issue or submit a PR.

## License

This project is open source and available under the [MIT License](LICENSE).

## Author

- [ivantsowlad](https://github.com/ivantsowlad)

