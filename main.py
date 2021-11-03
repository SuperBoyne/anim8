'''
    _    _   _ ___ __  __  ___
   / \  | \ | |_ _|  \/  |( _ )
  / _ \ |  \| || || |\/| |/ _ \
 / ___ \| |\  || || |  | | (_) |
/_/   \_|_| \_|___|_|  |_|\___/
A simple library for cool text animations
By Boyne
Licensed under the MIT license
'''
import time, os

class Anim8:

  def __init__(self):
    pass
  
  def typeout(self, text, delay=0.1, newline=True):
    '''
    Periodically outputs text, making it look like you're typing it yourself!
    -- ARGS --
    -text  The text to print out
    -delay The time between each character printed out
    '''
    for char in text:
      print(char, flush=True, end="")
      time.sleep(delay)
    if newline:
     print()
  
  def clear(self):
    '''
    Clears all text on the screen! May not work for all terminals, particularly ones embedded in your IDE.
    '''
    if os.name == "nt":
      os.system("cls")
    else:
      os.system("clear")

#Module test
if __name__ == "__main__":
  anim8 = Anim8()
  anim8.typeout("The typeout() function will type out text as if you're typing it! Clearing in 3... 2... 1...")
  anim8.clear()