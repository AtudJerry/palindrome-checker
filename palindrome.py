from dataclasses import replace
jerr = input(" enter your txt")
if jerr[:] == jerr[::-1]: #checks if the text is exactly equal to the text in reverse order reverse
    print("the text is a palindrome")
else:
    print("the text is not a palindrome")