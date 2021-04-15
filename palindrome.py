def palindrome(string):
    assert len(string) > 0, 'No se puede una cadena vacía'
    return string == string[::-1]

print(palindrome('  '))