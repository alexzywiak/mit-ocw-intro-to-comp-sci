#!/usr/bin/env python -tt

from ps5_ghost import *

#
# Test code
#
def test_is_word_frag():
    
    if not is_word_frag(''):
        print 'Should return True for empty string'
        return

    if not is_word_frag('a'):
        print 'Should return True for "a"'
        return

    if not is_word_frag('lem'):
        print 'Should return True for "lem"'
        return

    if not is_word_frag('shoe'):
        print 'Should return True for "shoe"'
        return

    if is_word_frag('xzzz'):
        print 'Should return False for "xzzz"'
        return

    if is_word_frag('shoestronx'):
        print 'Should return False for "shoestronx"'
        return
    
    print "SUCCESS: test_is_word_frag()"

def test_is_word():

    if is_word(''):
        print 'Should return False for empty string'
        return

    if not is_word('aardvark'):
        print 'Should return True for "aardvark"'
        return

    if not is_word('lemon'):
        print 'Should return True for "lemon"'
        return

    if not is_word('shoe'):
        print 'Should return True for "shoe"'
        return

    if is_word('sharkx'):
        print 'Should return False for "sharkx"'
        return

    if is_word('xlkasjdfgisoj'):
        print 'Should return False for "xlkasjdfgisoj"'
        return
    
    print "SUCCESS: test_is_word()"

def test_is_valid_input():

    if is_valid_input(''):
        print 'Should return False for empty string'
        return

    if is_valid_input('abc'):
        print 'Should return False for "abc"'
        return

    if not is_valid_input('l'):
        print 'Should return True for "l"'
        return

    if not is_valid_input('L'):
        print 'Should return True for "L"'
        return

    
    print "SUCCESS: is_valid_input()"

print "----------------------------------------------------------------------"
print "Testing is_word_frag..."
test_is_word_frag()
print "Testing is_word..."
test_is_word()
print "Testing is_valid_input..."
test_is_valid_input()
print "All done!"
