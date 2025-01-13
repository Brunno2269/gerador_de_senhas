import os
import random
import string
import argparse
from pathlib import Path

class PasswordGenerator:
    """
    Classe para geração de senhas seguras com opções personalizáveis.
    """
    def __init__(self, length=12, include_uppercase=True, include_numbers=True, include_symbols=True):
        if length < 4:
            raise ValueError("Password length must be at least 4 characters.")
        self.length = length
        self.include_uppercase = include_uppercase
        self.include_numbers = include_numbers
        self.include_symbols = include_symbols

    def generate(self):
        """
        Gera uma senha baseada nas configurações fornecidas.
        :return: string
        """
        # Definir o conjunto de caracteres que será usado
        char_pool = string.ascii_lowercase + string.ascii_uppercase  # Apenas letras maiúsculas e minúsculas
        if self.include_numbers:
            char_pool += string.digits  # Adicionar números
        if self.include_symbols:
            symbol = random.choice(string.punctuation)  # Garantir apenas 1 símbolo
        else:
            symbol = ""

        # Gerar a senha
        password = ''.join(random.choices(char_pool, k=self.length - 1)) + symbol
        random.shuffle(list(password))  # Embaralha a senha para garantir aleatoriedade

        return password

    def save_to_file(self, passwords, file_path="generated_passwords.txt"):
        """
        Salva as senhas geradas em um arquivo especificado.
        :param passwords: Lista de senhas a serem salvas.
        :param file_path: Caminho do arquivo.
        """
        file_path = Path(file_path)
        file_path.parent.mkdir(parents=True, exist_ok=True)
        with file_path.open(mode="a") as file:
            for password in passwords:
                file.write(password + "\n")
        print(f"Passwords saved to {file_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate secure passwords with customizable options.")
    parser.add_argument("-l", "--length", type=int, default=12, help="Length of the password (default: 12)")
    parser.add_argument("-u", "--no-uppercase", action="store_false", help="Exclude uppercase letters from the password")
    parser.add_argument("-n", "--no-numbers", action="store_false", help="Exclude numbers from the password")
    parser.add_argument("-s", "--no-symbols", action="store_false", help="Exclude symbols from the password")
    parser.add_argument("-f", "--file", type=str, help="Path to save the generated passwords")
    parser.add_argument("-c", "--count", type=int, default=5, help="Number of passwords to generate (default: 5)")

    args = parser.parse_args()

    generator = PasswordGenerator(
        length=args.length,
        include_uppercase=args.no_uppercase,
        include_numbers=args.no_numbers,
        include_symbols=args.no_symbols
    )

    try:
        passwords = [generator.generate() for _ in range(args.count)]
        print("Generated Passwords:")
        for idx, password in enumerate(passwords, start=1):
            print(f"{idx}: {password}")

        if args.file:
            generator.save_to_file(passwords, args.file)
    except Exception as e:
        print(f"Error: {e}")
