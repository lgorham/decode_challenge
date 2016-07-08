
def decode(encoded_message):
    """Decode a string

    Each number tells you how many characters to skip before finding a letter 
    we want to print. After each printed letter should come the next number."""
    
    decoded_message = ""
    for i in encoded_message:
        if encoded_message.isdigit(i) == True:
            encoded_message = encoded_message[(int(i) + 1):]
            decoded_message = decoded_message + encoded_message[item]
    print decoded_message

decode("0h1ae2bcy")