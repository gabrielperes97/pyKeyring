import unittest
from security import DefaultCryptography, StorageFormat

class TestSecurrity(unittest.TestCase):

    def cryptographyDependencies(self):
        dependencies = DefaultCryptography.generateCryptographyDependencies(storage_format=StorageFormat.BSON)

        salt_length = int.from_bytes(dependencies[:DefaultCryptography.SALT_BYTES], byteorder='big')
        self.assertEqual(salt_length, DefaultCryptography.SALT_LENGTH)

        salt = dependencies[DefaultCryptography.SALT_BYTES:salt_length+DefaultCryptography.SALT_BYTES]
        self.assertEqual(len(salt), salt_length)

        storage_format = StorageFormat(int.from_bytes(dependencies[salt_length+DefaultCryptography.SALT_BYTES:salt_length+DefaultCryptography.SALT_BYTES+DefaultCryptography.STORAGE_BYTES], byteorder='big'))
        self.assertEqual(storage_format, StorageFormat.BSON)


        dependencies = DefaultCryptography.generateCryptographyDependencies(storage_format=StorageFormat.JSON)

        salt_length = int.from_bytes(dependencies[:DefaultCryptography.SALT_BYTES], byteorder='big')
        self.assertEqual(salt_length, DefaultCryptography.SALT_LENGTH)

        salt = dependencies[DefaultCryptography.SALT_BYTES:salt_length+DefaultCryptography.SALT_BYTES]
        self.assertEqual(len(salt), salt_length)

        storage_format = StorageFormat(int.from_bytes(dependencies[salt_length+DefaultCryptography.SALT_BYTES:salt_length+DefaultCryptography.SALT_BYTES+DefaultCryptography.STORAGE_BYTES], byteorder='big'))
        self.assertEqual(storage_format, StorageFormat.JSON)
