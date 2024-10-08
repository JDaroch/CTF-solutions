#Write UP BY DAROCH
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
import hashlib
import base64

# private key in PEM format
private_key_pem = b"""
-----BEGIN RSA PRIVATE KEY-----
MIICXgIBAAKBgQDwkrxVrZ+KCl1cX27SHDI7EfgnFJZ0qTHUD6uEeSoZsiVkcu0/
XOPbz1RtpK7xxpKMSnH6uDc5On1IEw3A127wW4Y3Lqqwcuhgypd3Sf/bH3z4tC25
eqr5gA1sCwSaEw+yBxdnElBNOXxOQsST7aZGDyIUtmpouI1IXqxjrDx2SQIDAQAB
AoGBAOwd6PFitnpiz90w4XEhMX/elCOvRjh8M6bCNoKP9W1A9whO8GJHRnDgXio6
/2XXktBU5OfCVJk7uei6or4J9BvXRxQpn1GvOYRwwQa9E54GS0Yu1XxTPtnBlqKZ
KRbmVNpv7eZyZfYG+V+/f53cgu6M4U3SE+9VTlggfZ8iSqGBAkEA/XvFz7Nb7mIC
qzQpNmpKeN4PBVRJBXqHTj0FcqQ5POZTX6scgE3LrxVKSICmm6ungenPXQrdEQ27
yNQsfASFGQJBAPL2JsjakvTVUIe2JyP99CxF5WuK2e0y6N2sU3n9t0lde9DRFs1r
mhbIyIGZ0fIkuwZSOqVGb0K4W1KWypCd8LECQQCRKIIc8R9iIepZVGONb8z57mA3
sw6l/obhfPxTrEvC3js8e+a0atiLiOujHVlLqD8inFxNcd0q2OyCk05uLsBxAkEA
vWkRC3z7HExAn8xt7y1Ickt7c7+n7bfGuyphWbVmcpeis0SOVk8QrbqSNhdJCVGB
TIhGmBq1GnrHFzffa6b1wQJAR7d8hFRtp7uFx5GFFEpFIJvs/SlnXPvOIBmzBvjU
yGglag8za2A8ArHZwA1jXcFPawuJEmeZWo+5/MWp0j+yzQ==
-----END RSA PRIVATE KEY-----
"""

# load private key
private_key = serialization.load_pem_private_key(
    private_key_pem,
    password=None,
    backend=default_backend()
)

# get the public key in bytes 
public_key = private_key.public_key()

# convert the public key to binary DR format (without PEM head)
public_key_der = public_key.public_bytes(
    encoding=serialization.Encoding.DER,  # DER format (binary)
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)
# Get base64 public key
public_key_base64 = base64.b64encode(public_key_der)
print('Public Key base64:\n',public_key_base64.decode('utf-8'))

# Compute MD5 hash from base64 public key
md5_hash = hashlib.md5(public_key_base64).hexdigest()

# Print MD5 hash
print("MD5 public key hash:", md5_hash)