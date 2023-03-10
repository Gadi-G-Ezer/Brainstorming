"""
This code tries to decrypt an output generated by encrypt() of encrypt_for_decrypt_1.py.

Find and fix the bug(s)!

Author: Omer Rosenbaum
"""
SECRET = "9Y2{0C5m2c0r7t5%7p3v0 7h6}0e2u2q7t5j3/6&3x9|7l5%7p6z0,4$2c6t8l6&8l5t2p1(6z0 7m8w9{8o3h4x9)5y4s3#4t9~3w4$9|5t6s5j3#5g2t0e3d9t8x4s3l9w5y8{1/5320"


def decrypt(encrypted):
    decrypted = ""
    for i in range(0, len(encrypted), 2): # for i in range(0, len(encrypted)): --> for i in range(0, len(encrypted), 2):
        offset, character = encrypted[i], encrypted[i+1]  # (offset, character) = encrypted[i:i+2] --> offset, character = encrypted[i], encrypted[i+1]
        offset = int(offset)
        decrypted += chr(ord(character)-offset)

    return decrypted

if __name__ == "__main__":
    print(decrypt(SECRET))