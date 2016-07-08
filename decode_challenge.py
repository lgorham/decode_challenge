def convert_to_list(encoded_message_string):
    """Converts the encoded message into a list for easier type evaluation"""
    
    as_list = []
    for char in encoded_message_string:
        try:
            int_char = int(char)
            as_list.append(int_char)
        except:
            as_list.append(char)
    return as_list


def decode(encoded_message):
    """Decode a string

    Each number tells you how many characters to skip before finding a good letter
    After each good letter should come the next number"""
    
    decoded_message = ""
    list_message = convert_to_list(encoded_message)
    for item in list_message:
        if type(item) is int:
            list_message = list_message[(item + 1):]
            decoded_message = decoded_message + list_message[item]
    print decoded_message

decode("0h1ae2bcy")