import os
import requests
import json
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
from Crypto.PublicKey import RSA
import base64
from Crypto.Cipher import AES, PKCS1_v1_5
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
import requests
import base64

class neuropacs:
    def __init__(self, api_key,server_url):
        """
        NeuroPACS constructor
        """
        self.api_key = api_key
        self.server_url = server_url

    def generate_aes_key(self):
        """Generate an 16-byte AES key for AES-CTR encryption.

        :return: AES key encoded as a base64 string.
        """
        aes_key = get_random_bytes(16)
        aes_key_base64 = base64.b64encode(aes_key).decode('utf-8')
        return aes_key_base64

    def oaep_encrypt(self,plaintext,format):
        """
        OAEP encrypt plaintext.

        :param * plaintext: Plaintext to be encrypted.
        :param str format: Format of plaintext. Defaults to "string".

        :return: Base64 string OAEP encrypted ciphertext
        """

        if format == "JSON":
            plaintext = json.dumps(plaintext)
        if format == "string":
            pass

        # get public key of server
        PUBLIC_KEY = self.get_public_key()

        PUBLIC_KEY = PUBLIC_KEY.encode('utf-8')

        # Deserialize the public key from PEM format
        public_key = serialization.load_pem_public_key(PUBLIC_KEY)

        # Encrypt the plaintext using OAEP padding
        ciphertext = public_key.encrypt(
            plaintext.encode('utf-8'),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        ciphertext_key_base64 = base64.b64encode(ciphertext).decode('utf-8')

        # Return the ciphertext as bytes
        return ciphertext_key_base64

    def connect(self, api_key, aes_key):
        """Create a connection with the server

        :param str api_key: Base64 API key.
        :param str aes_key: Base64 AES key.

        Returns:
        :returns: Base64 string encrypted AES key.
        """

        try:
            headers = {
            'Content-Type': 'text/plain',
            'client': 'api'
            }

            body = {
                "aes_key": aes_key,
                "api_key": api_key
            }

            encrypted_body = self.oaep_encrypt(body,"JSON")

            res = requests.post(f"{self.server_url}/connect/", data=encrypted_body, headers=headers)

            if res.status_code == 200:
                    json = res.json()
                    connectionID = json["connectionID"]
                    return connectionID
            else:
                raise RuntimeError("Connection failed.")
        except requests.exceptions.RequestException as e:
            return(f"An error occurred: {e}")

    def get_public_key(self):
        """Retrieve public key from server.

        :return: Base64 string public key.
        """

        res = requests.get(f"{self.server_url}/getPubKey")
        if(res.status_code != 200):
            raise RuntimeError("Public key retrieval failed.")
            
        json = res.json()
        pub_key = json['pub_key']
        return pub_key

    def upload (self, file, connectionID, orderID, aes_key):
        """Upload a file to the server

        :param str file: Path to file to be uploaded.
        :param str connectionID: Base64 connectionID.
        :param str orderID: Base64 orderID.
        :param str aes_key: Base64 AES key.

        :return: Upload status code.
        """
    
        BOUNDARY = "neuropacs----------"
        DELIM = ";"
        CRLF = "\r\n"
        SEPARATOR="--"+BOUNDARY+CRLF
        END="--"+BOUNDARY+"--"+CRLF
        CONTENT_TYPE = "Content-Type: application/octet-stream"

        form = {
            "Content-Disposition": "form-data",
            "filename": file,
            "name":"test123"
        }

        header = SEPARATOR
        for key, value in form.items():
            header += f"{key}: {value}"
            header += DELIM
        header += CRLF
        header += CONTENT_TYPE
        header += CRLF + CRLF

        header_bytes = header.encode("utf-8")

        encrypted_orderID = self.encrypt_aes_ctr(orderID, aes_key,"string", "string")

        if(os.path.isfile(file)):

            with open(file, 'rb') as f:
                binary_data = f.read()

                encrypted_binary_data = self.encrypt_aes_ctr(binary_data,aes_key,"bytes","bytes")

                message = header_bytes + encrypted_binary_data + END.encode("utf-8")

                headers = {
                "Content-Type": "application/octet-stream",'connection-id': connectionID, 'client': 'API', 'order-id': encrypted_orderID
                }

                res = requests.post(f"{self.server_url}/upload/",data=message,headers=headers)

                if(res.status_code == 201):
                    return res.status_code 
                else:
                    raise RuntimeError("File upload failed.")

        else:
            raise RuntimeError("Not a file.")


    def new_job (self,connectionID, aes_key):
        """Create a new order

        :param str connectionID: Base64 connectionID.
        :param str aes_key: Base64 AES key.

        :return: Base64 string orderID.
        """
    
        headers = {'Content-type': 'text/plain', 'connection-id': connectionID, 'client': 'API'}

        res = requests.post(f"{self.server_url}/newJob/", headers=headers)

        if res.status_code == 201:
            text = res.text
            text = self.decrypt_aes_ctr(text,aes_key,"string")
            return text
        else:
            raise RuntimeError("Job creation failed.")


    def run_job(self,ConnectionID, aes_key, productID, orderID ):
        """Run a job

        :param str ConnectionID: Base64 connectionID.
        :param str aes_key: Base64 AES key.
        :param str productID: Product to be executed.
        :prarm str orderID: Base64 orderID.

        :return: Job run status code.
        """

        headers = {'Content-type': 'text/plain', 'connection-id': ConnectionID, 'client': 'api'}

        body = {
            'orderID': orderID,
            'productID': productID
        }

        encryptedBody = self.encrypt_aes_ctr(body, aes_key, "JSON","string")

        res = requests.post(f"{self.server_url}/runJob/", data=encryptedBody, headers=headers)
        
        if res.status_code == 202:
            return res.status_code
        else:
            raise RuntimeError("Job run failed.")

    # default format == string
    def encrypt_aes_ctr(self, plaintext, aes_key, format_in, format_out):
        """AES CTR encrypt plaintext

        :param * plaintext: Plaintext to be encrypted.
        :param str aes_key: Base64 AES key.
        :param str format_in: format of plaintext. Defaults to "string".
        :param str format_out: format of ciphertext. Defaults to "string".

        :return: Encrypted ciphertext in requested format_out.
        """
        aes_key_bytes = base64.b64decode(aes_key)

        plaintext_bytes = ""

        if format_in == "JSON":
            plaintext = json.dumps(plaintext) 
            plaintext_bytes = plaintext.encode("utf-8")
        elif format_in == "string":
            plaintext_bytes = plaintext.encode("utf-8")  
        elif format_in == "bytes":
            plaintext_bytes = plaintext
            pass


        padded_plaintext = pad(plaintext_bytes, AES.block_size)

        # generate IV
        iv = get_random_bytes(16)

        # Create an AES cipher object in CTR mode
        cipher = AES.new(aes_key_bytes, AES.MODE_CTR, initial_value=iv, nonce=b'')

        # Encrypt the plaintext
        ciphertext = cipher.encrypt(padded_plaintext)

        # Combine IV and ciphertext
        encrypted_data = iv + ciphertext

        encryped_message = ""

        if format_out == "string":
            encryped_message = base64.b64encode(encrypted_data).decode('utf-8')
        elif format_out == "bytes":
            encryped_message = encrypted_data

        return encryped_message


    def decrypt_aes_ctr(self,encryptedData, aes_key, format_out):
        """AES CTR decrypt ciphertext.

        :param str ciphertext: Ciphertext to be decrypted.
        :param str aes_key: Base64 AES key.
        :param * format_out: Format of plaintext. Default to "string".

        :return: Plaintext in requested format_out.
        """

        aes_key_bytes = base64.b64decode(aes_key)

        # Decode the base64 encoded encrypted data
        encrypted_data = base64.b64decode(encryptedData)

        # Extract IV and ciphertext
        iv = encrypted_data[:16]

        ciphertext = encrypted_data[16:]

        # Create an AES cipher object in CTR mode
        cipher = AES.new(aes_key_bytes, AES.MODE_CTR, initial_value=iv, nonce=b'')

        # Decrypt the ciphertext and unpad the result
        decrypted = cipher.decrypt(ciphertext)

        decrypted_data = decrypted.decode("utf-8")

        if format_out == "JSON":
            decrypted_data = json.loads(decrypted_data)
        elif format_out == "string":
            pass

        return decrypted_data