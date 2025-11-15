from operator import index

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(original_text, shift_amount, encode_or_decode):
    # step 1
    # invalidate the range choice before encoding
    if shift_amount < 1 or shift_amount > 25:
        print("Please choice the Alphabetic range 1 - 25")
        return

    # step 2 automate the shift_amount + or - before the loop so if the user choose decode it
    # should change to - shift_amount in our code in the shifted_position
    if encode_or_decode == "decode":
        shift_amount *= -1 # in maths if you multiply a number by -1 it will reverse sign + to -
            # so if the user chooses decode we will get - shift_amount in line 22 of our code

    user_text = " "
    for each in original_text:
        shifted_position = alphabet.index(each) + shift_amount
        shifted_position = shifted_position % len(alphabet)
        user_text += alphabet[shifted_position]

    print(f"your result is :{user_text}")

caesar(encode_or_decode= direction, shift_amount=shift,original_text = text)