# Maldocs
Scripting together some of my favorite Python tools for doing initial triage of a suspected malicious document (e.g. PDF, DOC, DOCX, XSLM, etc.)

## Requirements and Dependencies

### Python Version
Although I love Python 2.7 and think that Python 3 is an impure abomination... I've used Python 3 for this.

### Operating System
I wrote this for Windows because that's what I'm normally using when someone wants me to look at document for them. If you plan to run this on Linux you'll likely need to make some small updates but in theory it should still work. 

One Linux change I can think of off the top of my head is you'll need to update line 23. Change:
```
os.system("Strings \""+filename+"\" | findstr /i http")
```
To:
```
os.system("Strings \""+filename+"\" | grep http")
```

### Libraries and Programs Used
fleep: File format determination library for Python
Author: [Mykyta Paliienko](https://github.com/floyernick)
[https://github.com/floyernick/fleep-py](https://github.com/floyernick/fleep-py)
```bash
pip install fleep
```

oletools: Python tools to analyze OLE and MS Office files
Author: [Philippe Lagadec](https://github.com/decalage2)
[https://github.com/decalage2/oletools/wiki/Install](https://github.com/decalage2/oletools/wiki/Install)
```bash
pip install -U oletools
```
Note: Specifically this is using olevba.py.

oledump.py: Program to analyze OLE files
Author: [Didier Stevens](https://blog.didierstevens.com/)
[https://blog.didierstevens.com/my-software/](https://blog.didierstevens.com/my-software/)

rtfdump.py: Tool to analyze RTF documents
Author: [Didier Stevens](https://blog.didierstevens.com/)
[https://blog.didierstevens.com/my-software/](https://blog.didierstevens.com/my-software/)

pdfid.py: Tool to scan a PDF looking for keywords and risky tags
Author: [Didier Stevens](https://blog.didierstevens.com/)
[https://blog.didierstevens.com/my-software/](https://blog.didierstevens.com/my-software/)

pdf-parser.py: Tool to parse a PDF looking at the main PDF elements
Author: [Didier Stevens](https://blog.didierstevens.com/)
[https://blog.didierstevens.com/my-software/](https://blog.didierstevens.com/my-software/)

Strings: Looks for strings in files.
Author: Mark Russinovich
[https://docs.microsoft.com/en-us/sysinternals/downloads/strings](https://docs.microsoft.com/en-us/sysinternals/downloads/strings)

Note: After you download oledump.py, rtfdump.py, pdfid.py, pdf-parser.py, and Strings you'll want to add them to your Path environment variable.
Additional Note: For convenience you'll want to add the maldocs.py script to your Path as well.

## Usage
Assuming maldocs.py is in your Path, simply call the script with the file name you want to triage:
```bash
maldocs.py "some really suspicious email attachment.docm"
```

## Additional Reading
Lenny Zeltser has some really great resources on his website, including an "Analyzing Malicious Documents Cheat Sheet" ([https://zeltser.com/analyzing-malicious-documents/](https://zeltser.com/analyzing-malicious-documents/)). I highly encourage you to check it out, along with the rest of his website.

Otherwise Didier Stevens' website ([https://blog.didierstevens.com/](https://blog.didierstevens.com/))is another really great resource.

## Planned Changes and Improvements
Another really great tool that I like to run for PDFs is peepdf ([http://eternal-todo.com/tools/peepdf-pdf-analysis-tool](http://eternal-todo.com/tools/peepdf-pdf-analysis-tool)). I started to include it here, but found when updating my script to Python 3 that peepdf is still Python 2.7.

There is a version here that looks like it might be updated by someone else but I haven't had time to look at it closely or try to get it working. See [https://pypi.org/project/peepdf/](https://pypi.org/project/peepdf/) if you want to look at it yourself.