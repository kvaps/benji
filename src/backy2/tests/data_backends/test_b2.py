import unittest

from . import DatabackendTestCase


class test_b2(DatabackendTestCase, unittest.TestCase):
    CONFIG = """
        configurationVersion: '0.1'
        logFile: /dev/stderr
        lockDirectory: {testpath}/lock
        hashFunction: blake2b,digest_size=32
        dataBackend:
          type: b2
          b2:
             accountId: ********
             applicationKey: *******************************
             bucketName: backy2
          simultaneousWrites: 1
          simultaneousReads: 1
          bandwidthRead: 0
          bandwidthWrite: 0
        """

if __name__ == '__main__':
    unittest.main()
