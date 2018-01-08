# Write the html_list function. The function takes one argument, a list of strings, and returns a single string which
#  is an HTML list. For example, if the function should produce the following string when provided the list ['first
# string', 'second string'].

# <ul>
# <li>first string</li>
# <li>second string</li>
# </ul>

# That is, the string's first line should be the opening tag <ul>. Following that is one line per element in the source
# list, surrounded by <li> and </li> tags. The final line of the string should be the closing tag </ul>.

def html_list(input_list):
    for i in range(len(input_list)):
        input_list[i] = '<li>' + input_list[i] + '</li>\n'
    input_list.insert(0, '<ul>\n')
    input_list.insert(len(input_list), '</ul>')

    return ''.join(input_list)



print(html_list(['first string', 'second string']))