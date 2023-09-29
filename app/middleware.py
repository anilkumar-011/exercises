from django.utils.deprecation import MiddlewareMixin
from cryptography.fernet import Fernet


class CustomMiddleware(MiddlewareMixin):

    def __init__(self, get_response):
        super().__init__(get_response)
        self.key = b'4q1fQoa0lYVlj479bvk2XxEav9Ev3LeoPyzTO5MsmrU=' or Fernet.generate_key()
        self.cipher_suite = Fernet(self.key)

    def process_request(self, request):
        if request.body:
            decrypted_data = self.cipher_suite.decrypt(request.body)
            request._body = decrypted_data
            pass
        print(self.key, '2')

    def process_response(self, request, response):
        if response.content:
            encrypted_data = self.cipher_suite.encrypt(response.content)
            response.content = encrypted_data
        return response



#
# from cryptography.fernet import Fernet
#
# # Generate a secret key (store this securely)
# secret_key = b'4q1fQoa0lYVlj479bvk2XxEav9Ev3LeoPyzTO5MsmrU='
# cipher_suite = Fernet(secret_key)
#
# # Encrypt the data
# encrypted_data =b'gAAAAABlFAAXWwde_7NepXFY5NwC6IDKPvOOXSESp1zsYWy2QvkmnNOuBAwn-8a2xiqkd4mIzdwAjCjctxsCrvRhS5qyTIxLt9gD8dUj4MUSI2t3r7CNg5ZRWp8v8tCbs4_O_l5sahRm'
#
# # Decrypt the data
# decrypted_data = cipher_suite.decrypt(encrypted_data).decode()
#
# print("Encrypted Data:", encrypted_data)
# print("Decrypted Data:", decrypted_data)
# print('secret_key:', secret_key)
