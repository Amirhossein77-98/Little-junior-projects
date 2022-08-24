
exit = False
palindrome = False
New_String = ""
while not exit:
  String = input("Enter a string to check for palindrome or 'exit' to close: ").lower()
  if String == "exit":
    exit = True
    break
  else:
    for x in String:
      if x.isalnum:
        New_String += x

    Reversed = New_String[::-1]
    
    if New_String == Reversed:
      palindrome = True
      print(palindrome)
    else:
      palindrome = False
      print(palindrome)
      