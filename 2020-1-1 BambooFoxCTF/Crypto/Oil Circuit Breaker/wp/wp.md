The attack follow this paper https://eprint.iacr.org/2019/311.pdf

To do universal forgery with only 2 encryption oracles and 1 decryption oracles.
First use 1 encryption oracle and 1 decryption oracle to get a few of random mappings.
Then, you can brute force the last byte of the block to get the ciphertext and tag with only 1 encryption oracle.
