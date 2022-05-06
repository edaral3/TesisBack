import base64

def decodeBase64(data):
    b64 = base64.b64decode(data)
    with open('img.jpg', 'wb') as fh:
        fh.write(b64)