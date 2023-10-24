from stringsan.strings import occurences, first_occurence, last_occurence, is_zalgo

PATTERN = "hi"
STRING = "Hi, my name is hi man. He is hi hi man."
ZALGO = """
H̶̴̨̜̣͚̬͖̝̞̼͚̝̱̬̳̜̠͙̪͓͖̥̬͕̞̜̲͖̦̙̗̝̤̙̺̖̭̪̭̹̗̘̙̙͇̣͙̼͚̠͔̩̭͉͙̞̜̖̦̙̟̖͈͚͉̩̺̦͎̫̗̖̜̠̤̬̟̪͈̬͔̣̩̙̤̱͇̳̙̪̗̞͓͓͎̙̞̺͈͈̪͕̤̳̣̲̬̺̥͎̗̞̙̠̱̦̖͓̥̙̭̲̬̬̟̦̺̘̣̞̳͉̪̫̤̮͕̺̤̪̼̜̹͍̲̖͇̳̼̬̲͈̜̘͉̜̪̝̼͉̬͍̝̹̪̪͉̜̲̜̹̮̪͓̤̦̗͈̣̗̠̜̝̱̲̞̝̰̖̹̝̹̦̱͈̥͈͇̭̲͚̱̙̹̭̝͇͔̖̬̭̭͚͙͉̩̬̣̥̦͓̫̤̙̜̪̤͓̱̟͍̖͙̞̥͚̬̞͙̠͍̺̞͓̠̖͕̬͎̘̼̰̲̠͔͇̹̖͚̝͙͔̮̬̠̝͎̙̺̘͚͎̩̠̘̭͉͈͙͖͍̣̰̥͉̬͔͇̹̮̜̤͈͍̤̹̲͍͇͕̮͙̪̝͍̬̜̟̻̼͎̙͔͕̳̻͍̰̹̮͕͕͍͈͇̺̞͔̘̦̜̠̠̹̪͇͙͙͉̘̜̩͓͎̥̰̮͇͕̥̟̜̻̦͕̮̜͕̭͍̠̣̲͇̹̟̻̘͓̬͔̥̜̻̪̭̖͔̗͙͓̩̺̜̥͎̲̠͚̝͕̣̱̦͓͕̙͓̺̠̬̦͕͍̟̦̥̙̼̦̜̞̝͕̬̼̙̬̜͕̘̲͙̟͇̩͚̣̺̳̻͖̹͉͖͔̥͎̣̜̙̪̤͉̩̝̼̺͇̙̳̮̪̣͔̥̹̮̜̲̦̥̮̖͍̣̲͕̙͚̹̦͓̪͔̝͔̘̪̭̝̘͉̦̪̬̬̱̙̜̪̦̩͔̗͍̝̞̬̱͕͓̣̭̹̹͈̦͓͍̙͍̮͔̖̟̳͙̹͔̼̥͇̦̝̲͓̗̖̭̲̦̩̦̣͕̭̠̗͖̞̲̝̙̠͚̼͎͈̠͍̣̺͇̮̪̦̣͍̠̱̝̞͕̪͔͍̳͇͙̦̣̻̬͓̝͇̤̙̩̹͙̘̬̦̮̻͍̦͕̘͔̮̙͕̮͉̦͙͙̝͙̪̪̱͈̦̜̹̬͈͈͖̺̰̳͙̺̦̖͚͔͗̐͌͛̊ͨ̓̏ͥ̿͛̿͡
"""


def test_occurences():
    assert occurences(STRING, PATTERN) == 3
    
def test_first_occurence():
    assert first_occurence(STRING) == "Hi"

def test_last_occurence():
    assert last_occurence(STRING) == "man"

def test_is_zalgo():
    assert is_zalgo(STRING) == False 
    assert is_zalgo(ZALGO) == True
 