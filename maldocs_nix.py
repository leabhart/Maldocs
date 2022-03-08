import sys
import os
import fleep

filename = sys.argv[1]

print ("Beginning analysis of \"" + filename + "\"...\n")

with open(filename, "rb") as file:
    info = fleep.get(file.read(128))

print("File Name: ")
print(filename)
print("\nListing possible file types:")
print(info.type)
print("\nListing possible file extensions:")
print(info.extension)
print("\nListing possible file MIME types:")
print(info.mime)
print("\n")

print("Looking for plain text URLs and listing them (if found)...\n[")
os.system("Strings \""+filename+"\" | grep -Eo '(http|https)://[a-zA-Z0-9./?=_%:-]*'")
print("]\nFinished looking for plain text URLs.\n")

if "document" in info.type:
        if "pdf" in info.extension:
                print("\nAttempting to identify risky keywords and dictionary entries....")
                os.system("pdfid.py -e \""+filename+"\"")

#               print("\nAttempting to identify risky tags and malformed objects...") << currently not working - wr$
#               os.system("peepdf.py –fl \""+filename+"\"") << currently not working - written for python 2 only

                print("\nAttempting to parse the Header, Objects, Cross Reference, and Trailer elements...")
                os.system("pdf-parser.py \""+filename+"\"")

        elif "rtf" in info.extension:
                print("\nAttempting to list groups and structure of RTF-formatted file...")
                os.system("rtfdump.py \""+filename+"\"")

                print("\nAttempting to locate groups in file that enclose an object...")
                os.system("rtfdump.py \""+filename+"\" -f O")

        else:
                print("\nAttempting to locate and extract any macros file...")
                os.system("olevba \""+filename+"\"")

                print("\nAttempting to locate and list any OLE2 streams present in file and looking for obfuscated $
                os.system("oledump.py \""+filename+"\" -p plugin_http_heuristics")
