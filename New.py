Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 03:03:55) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.
print 'hello'
SyntaxError: Missing parentheses in call to 'print'. Did you mean print('hello')?
>>> 
>>> print("Hello")
Hello
>>> 
>>> var str = "Hello, Playground"
SyntaxError: invalid syntax
>>> 
>>> clear
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    clear
NameError: name 'clear' is not defined
>>> help
Type help() for interactive help, or help(object) for help about object.
>>> help()

Welcome to Python 3.6's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at https://docs.python.org/3.6/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> clear
No Python documentation found for 'clear'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

help> how to clear
No Python documentation found for 'how to clear'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

help> jello
No Python documentation found for 'jello'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

help> 

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
>>> 
=============================== RESTART: Shell ===============================
>>> print ("Hello world")
Hello world
>>> var: potato
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    var: potato
NameError: name 'potato' is not defined
>>> 
=============================== RESTART: Shell ===============================
>>> print ("Beef")
Beef
>>> def main ():
	print repeat ('yay',false)
	
SyntaxError: invalid syntax
>>> def main():
	print repeat('yay', False)
	
SyntaxError: invalid syntax
>>> 
