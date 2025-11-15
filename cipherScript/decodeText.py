alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# This function encodes text and it uses 2 inputs
def decrypt(encoded_text, shift_amount):

    # step 1
    # invalidate the range choice before encoding
    if shift_amount < 1 or shift_amount > 25:
        print("Please choice the Alphabetic range 1 - 25")
        return
    # step 2
    # decode using for loop
    original_text = " "
    for each_letter in encoded_text:
        # If the character is a letter in the alphabet, the first for loop will create the encrypted letter.
        if each_letter in alphabet:
            shifted_position = alphabet.index(each_letter) - shift_amount #
            shifted_position = shifted_position % len(alphabet) # this ensures we don't go beyond our alphabetic range 1-25
            original_text += alphabet[shifted_position]

        # Otherwise like (spaces, numbers, punctuation), leave the character unchanged so the final
        # encrypted message keeps its original spacing and non-letter characters.
        else:
            original_text = original_text + encoded_text

    print(f"Your decoded text is : {original_text}")

# Step three, call the function and pass it to the user input to get the work
decrypt(text, shift)