"""
CSCI-603 Lab 2: Ciphers

A program that encodes/decodes a message by applying a set of transformation operations.
The transformation operations are:
    shift - Sa[,n] changes letter at index a by moving it n letters fwd in the alphabet. A negative
        value for n shifts the letter backward in the alphabet.
    rotate - R[n] rotates the string n positions to the right. A negative value for n rotates the string
        to the left.
    duplicate - Da[,n] follows character at index a with n copies of itself.
    trade - Ta,b swap the places of the a-th and b-th characters.
    affine - Aa,b applies the affine cipher algorithm y = (ax + b) mod 26 using a and b as keys.

All indices numbers (the subscript parameters) are 0-based.

author: Mariam Abidi
"""


def shift(message, i, k):
    """
    This function is used to shift the number on the index i to the next
    alphabet.

    :param message: It stores the user's input string.
    :param i: It stores the index value.
    :param k: It stores the number of times to shift.
    :return: The complete encrypted message is returned after shifting.
    """
    h = message[i]
    g = ord(h)
    g = g + k
    # This if condition checks if the unicode exceeds 90. It helps to wrap
    # around to "A" if value goes beyond "Z".
    if g > 90:
        difference = g - 90
        g = 64 + difference
    if g < 65:
        difference = 65 - g
        g = 64 + difference
    g = str(chr(g))
    a = message[:i]
    b = message[i + 1:]
    encrypted_message = a + g + b
    return encrypted_message


def rotate(message, k):
    """
    This function is used to rotate the characters according to the parameters.
    :param message: It stores the user's input string.
    :param k: It stores the number of times to rotate.
    :return: The complete encrypted message is returned after rotating.
    """
    # Checks if the value of k is positive or negative.
    if k > 0:
        for _ in range(k):
            a = message[:len(message) - 1]
            b = message[-1]
            message = b + a
        return message
    if k < 0:
        for _ in range(abs(k)):
            a = message[1:len(message)]
            b = message[0]
            message = a + b
        return message


def duplicate_enc(message, i, k):
    """
    This function is used to duplicate a character in a message while
    encrypting.
    :param message: It stores the user's input string.
    :param i: It stores the index value of character to duplicate.
    :param k: It stores the number of times to duplicate.
    :return: The complete encrypted message is returned after duplicating.
    """
    for _ in range(k):
        a = message[i]
        message = message[:i] + a + message[i:]
    return message


def duplicate_dec(message, i, k):
    """
    This function is used to duplicate a character in a message while
    decrypting.
    :param message: It stores the user's input string.
    :param i: It stores the index value of character to duplicate.
    :param k: It stores the number of times to duplicate.
    :return: The complete encrypted message is returned after duplicating.
    """
    message = message[:i + 1] + message[i + k + 1:]
    return message


def trade(message, i, j):
    """
    This function is used to flip two characters of a string.
    :param message: It stores the user's input string.
    :param i: It stores the index value of first character to flip.
    :param j: It stores the index value of second character to flip.
    :return: Returns the string with flipped characters.
    """
    a = message[i]
    b = message[j]
    message = message[:i] + b + message[i + 1: j] + a + message[j + 1:]
    return message


def affine_enc(message, a, b):
    """
    This function is used to carry out the affine transformation for
    encrypting.
    :param message: It stores the user's input string.
    :param a: This is the first value given by user for the formula.
    :param b: This is the second value given by user for the formula.
    :return: Returns the string after encrypting.
    """
    final_encryption = ""

    for i in message:
        encryption_function = ((a * (ord(i) - 65)) + b) % 26
        final_encryption += chr(encryption_function + 65)

    return final_encryption


def inverse_function(a, m):
    """
    This function is used to carry out the modular inverse which will be used
    while decrypting for affine transformation
    :param a: This is the first value given by user for the formula.
    :param m: This has a fixed value of 26.
    :return: Returns the number d which gives value 1.
    """
    for d in range(1, m):
        if (a * d) % m == 1:
            return d


def affine_dec(message, a, b):
    """
    This function is used to carry out the affine transformation for
    decrypting.
    :param message: It stores the user's input string.
    :param a: This is the first value given by user for the formula.
    :param b: This is the second value given by user for the formula.
    :return: Returns the string after decrypting.
    """
    final_decryption = ""

    for i in message:
        decryption_function = int(inverse_function(a, 26) * (ord(i) - 65 - b)) % 26
        final_decryption += chr(decryption_function + 65)
    return final_decryption


def main() -> None:
    """
    The main loop responsible for getting the input details from the user
    and printing in the standard output the results
    of encrypting or decrypting the message applying the transformations
    :return: None
    """
    print("E : Encryption; D : Decryption; Q : QUIT")
    choice = input("Enter your choice: ")

    # This is a condition for Encryption
    if choice == "E":
        message_enc = input("Enter your message to encrypt: ")
        operations_enc = input("Enter the operations to perform: ")
        # Splits the input given by the user.
        all_operations_enc = operations_enc.split(';')

        for m in all_operations_enc:
            # If condition to call shift function.
            if m[0] == "S":
                if len(m) == 2:
                    message_enc = shift(message_enc, int(m[1]), 1)
                elif len(m) == 4:
                    message_enc = shift(message_enc, int(m[1]), int(m[3]))
                elif "-" in m and len(m) == 5:
                    message_enc = shift(message_enc, int(m[1]), int(m[3:5]))

            # If condition to call rotate function.
            if m[0] == "R":
                if "-" in m and len(m) >= 3:
                    message_enc = rotate(message_enc, int(m[1:3]))
                elif len(m) >= 2:
                    message_enc = rotate(message_enc, int(m[1]))
                else:
                    message_enc = rotate(message_enc, 1)

            # If condition to call duplicate function.
            if m[0] == "D":
                if len(m) == 2:
                    message_enc = duplicate_enc(message_enc, int(m[1]), 1)
                else:
                    message_enc = duplicate_enc(message_enc, int(m[1]), int(m[3]))

            # If condition to call trade function.
            if m[0] == "T":
                if int(m[1]) < int(m[3]):
                    if len(m) == 4:
                        message_enc = trade(message_enc, int(m[1]), int(m[3]))

            # If condition to call affine transformation function.
            if m[0] == "A":
                if len(m) == 4:
                    message_enc = affine_enc(message_enc, int(m[1]), int(m[3]))

        print(message_enc)

    # This is condition for Decrypting
    if choice == "D":
        message_dec = input("Enter your message to decrypt: ")
        operations_dec = input("Enter the operations performed: ")
        all_operations_dec = operations_dec.split(';')
        all_operations_dec_reverse = all_operations_dec[::-1]

        for d in all_operations_dec_reverse:
            # If condition to call shift function.
            if d[0] == "S":
                if len(d) == 2:
                    message_dec = shift(message_dec, int(d[1]), -1)
                if len(d) == 4:
                    message_dec = shift(message_dec, int(d[1]), int("-" + d[3]))
                if len(d) == 5:
                    message_dec = shift(message_dec, int(d[1]), int("-" + d[3:5]))

            # If condition to call rotate function.
            if d[0] == "R":
                if len(d) == 3:
                    new_k = len(message_dec) - int(d[1:3])
                    print(new_k)
                    message_dec = rotate(message_dec, new_k)
                if len(d) == 2:
                    new_k = len(message_dec) - int(d[1])
                    message_dec = rotate(message_dec, new_k)
                else:
                    new_k = len(message_dec) - 1
                    message_dec = rotate(message_dec, new_k)

            # If condition to call duplicate function.
            if d[0] == "D":
                if len(d) == 2:
                    message_dec = duplicate_dec(message_dec, int(d[1]), 1)
                else:
                    message_dec = duplicate_dec(message_dec, int(d[1]), int(d[3]))

            # If condition to call trade function.
            if d[0] == "T":
                if len(d) == 4:
                    message_dec = trade(message_dec, int(d[1]), int(d[3]))

            # If condition to call affine transformation function.
            if d[0] == "A":
                if len(d) == 4:
                    message_dec = affine_dec(message_dec, int(d[1]), int(d[3]))

        print(message_dec)
    #  If condition for terminating the code.
    if choice == "Q":
        exit()


if __name__ == '__main__':
    main()
