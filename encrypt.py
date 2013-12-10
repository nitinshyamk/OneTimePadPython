#encrypt.py
#Nitin Shyamkumar (https://github.com/nitinshyamk)
#12.10.13

"""This module executes the one time pad cipher on any string 
(provided that ord(chr) for any chr in the string is in the range 0<=255).
The key can be changed as desired."""


#KEY (must be 8-bit string for current specification)
#feel free to change the key - though make sure each item is an int
# and that each item has 
KEY = [0,1,0,1,1,0,1,1]
#keyspace is defined as the the universe of all n-bit strings.
#KEYSPACE_N is the value of n. Leave KEYSPACE_N unchanged unless
# you understand the cipher
KEYSPACE_N = len(KEY)

def encrypt_string(s, key = KEY):
    """prints the encrypted string s as a series of 8-bit binary strings"""
    assert(type(s)==str)
    char_list = _convert_char_2_int(s)
    ciphertext= []
    for i in char_list:
        ciphertext.append(_xor(_convert_base10_binary(i),key))
        #ciphertext is a 2d list of ciphered 8 bit strings

    for i in ciphertext:
        print _convert_binlist_str(i)


#the methods below are hidden helper methods, used in encrypt_string function
def _convert_char_2_int(string):
    """converts a string of chars into a list of ints by using the ord
    built in method"""
    assert(type(string)==str)
    list_num = []
    for i in range(len(string)):
        list_num.append(ord(string[i]))
    return list_num


def _convert_base10_binary(num):
    """converts an int in the range [0,255] to an 8-bit list of ints"""
    assert(type(num)==int and num>=0 and num<=(pow(2,KEYSPACE_N)-1))
    #2^8 possibilities - 5 bit string
    exp  = KEYSPACE_N - 1
    bin_list = [] #first bit will always be a string
    while exp >=0:
        if pow(2,exp) > num:
            bin_list.append(0)
        else:
            bin_list.append(1)
            num-=pow(2,exp)
        exp-=1
    return bin_list


def _convert_binlist_str(bin_list):
    assert(type(bin_list)==list)
    """converts bin_list from a list of binary ints to a string format
    to improve readability"""
    assert(type(bin_list)==list)
    bin_str = ''
    for i in range(len(bin_list)):
        bin_str+=str(bin_list[i])
    return bin_str

def _xor(bin, key = KEY):
    """xor s the plaintext with the key to produce the ciphertext
    returns the ciphertext as a list of ints"""
    assert(type(bin)==list), "improper type"
    assert len(bin)==len(key), 'length mismatch'
    ciphertext = []
    for i in range(len(bin)):
        ciphertext.append((bin[i]+key[i])%2)
    return ciphertext


