import string
import argparse
import pyfiglet

banner = pyfiglet.figlet_format('Caesor Generator')
print(banner)

parser = argparse.ArgumentParser('Encoder')
parser.add_argument('-text', dest='input', required=True, type=str, help='Text you would like to be encoded')
parser.add_argument('-key', dest='key', required=True, type=int, help="Integer key used to encrypt or decrypt, positive number adds to letter's index, negative substract ")
parser. add_argument( choices= ['encrypt', 'decrypt'], dest='gen_type')


def find_letter_index(index):
    # since english alphabet has 26 letters, if a big key adds the index above 26, find the remainder
    if abs(index)>=26:
        index = index % 26
    return index


def caesor_generator(gen_type, text, key):
    encoded=[]
    input_list = list(text)
    if key != 0:
        for letter in input_list:
            # get charactder position in alphabet
            index = string.ascii_lowercase.index(letter)
            # Caesor encryptor adds the key value to the letter index
            if gen_type == 'encrypt':
                new = index + key
            # Caesor decryptor subtracts the key value from the letter index
            elif gen_type =='decrypt':
                new = index - key    
            new_index =find_letter_index(new)
            encoded.append(string.ascii_lowercase[new_index])
    else:
        print('Please note that the encoded text is exactly the same as original')
        encoded = input_list
    return encoded


def main():
    args= parser.parse_args()
    # Get list of letters from input text
    text = args.input
    # Get the generator type: encryptor or decryptor
    generator_type = args.gen_type
    # Key the generator key
    key = args.key
    # Encrypt or decrypt text using the caesor generator
    result = caesor_generator(generator_type, text, key)
    if generator_type == 'encrypt':
        # Add Banner
        print("-" * 50)
        print("You encrypted text: " + ''.join(result))
        print("-" * 50)
    elif generator_type =='decrypt':
        # Add Banner
        print("-" * 50)
        print("You decrypted text: " + ''.join(result))
        print("-" * 50)

if __name__ == "__main__":
    main()
