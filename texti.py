#Git texta python verkefni
text_file=open("texti.txt", "w")
text_file.write("Halló hvað segir þú gott?")
text_file.close()

text_file=open("texti.txt", "a")
text_file.write("\n" + "bla bla bla bla")
text_file.write("\n" + "bla bla bla bla")
text_file.write("\n" + "bla bla bla bla")

text_file=open("text.txt", "r")
print(text_file.read())
text_file.close()

