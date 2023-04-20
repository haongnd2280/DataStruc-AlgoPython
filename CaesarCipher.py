class CaesarCipher:
    """Class for doing encryption and decryption using a Caesar cipher."""

    def __init__(self, shift):
        """Construct Caesar cipher using given integer shift for rotation."""
        encoder = [None] * 26     # temp array for encryption
        decoder = [None] * 26     # temp array for decryption

        for k in range(26):
            encoder[k] = chr((k + shift) % 26 + ord('A'))
            decoder[k] = chr((k - shift) % 26 + ord('A'))

        self._forward = ''.join(encoder)     # will store as string
        self._backward = ''.join(decoder)    # since fixed

    def encrypt(self, message):
        """Returning string representing encrypted message."""
        return self._transform(message, self._forward)

    def decrypt(self, secret):
        """Return decrypted message given encrypted secret."""
        return self._transform(secret, self._backward)

    def _transform(self, original, code):
        """Utility to perform transformation based on given code string."""
        msg = list(original)
