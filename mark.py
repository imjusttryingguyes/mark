commands = ['plain', 'bold', 'italic', 'inline-code', 'link',
            'header', 'new-line', 'ordered-list', 'unordered-list']
text = ''
link1 = ''
link2 = ''
text_output = ''
input_text = 0
count = ''
level = 0
header_count = 0


while input_text != '!done':
    input_text = input('Choose a formatter: ')
    if input_text == 'plain':
        text = input('Text: ')
        text_output = text_output + text
        print(text_output)
    elif input_text == 'bold':
        text = input('Text: ')
        text = f'**{text}**'
        text_output = text_output + text
        print(text_output)
    elif input_text == 'italic':
        text = input('Text: ')
        text = f'*{text}*'
        text_output = text_output + text
        print(text_output)
    elif input_text == 'inline-code':
        text = input('Text: ')
        text = f'`{text}`'
        text_output = text_output + text
        print(text_output)
    elif input_text == 'link':
        link1 = input('Label: ')
        link1 = f'[{link1}]'
        link2 = input('URL: ')
        link2 = f'({link2})'
        text_output = text_output + link1 + link2
        print(text_output)
    elif input_text == 'header':
        while header_count != 1:
            level = int(input('Level: '))
            if 1 > level or level > 6:
                print('The level should be within the range of 1 to 6')
            else:
                text = input('Text: ')
                count = '#' * level
                if text_output != '':
                    text_output = text_output + '\n'
                text = f'{count} {text}\n'
                text_output = text_output + text
                print(text_output)
                header_count = 1
    elif input_text == 'new-line':
        text = '\n'
        text_output = text_output + text
        print(text_output)
    elif input_text == 'ordered-list':
        number_rows = 0
        while number_rows <= 1:
            number_rows = int(input('Number of rows: '))
            number_rows_start = number_rows
            if number_rows <= 1:
                print('The number of rows should be greater than zero')
            else:
                break
        while number_rows >= 1:
            text = input(f'Row #{number_rows_start - number_rows + 1}: ')
            text = f'{number_rows_start - number_rows + 1}. ' + text + '\n'
            text_output = text_output + text
            number_rows -= 1
        print(text_output)
    elif input_text == 'unordered-list':
        number_rows = 0
        while number_rows <= 1:
            number_rows = int(input('Number of rows: '))
            number_rows_start = number_rows
            if number_rows <= 1:
                print('The number of rows should be greater than zero')
            else:
                break
        while number_rows >= 1:
            text = input(f'Row #{number_rows_start - number_rows + 1}: ')
            text = f'* ' + text + '\n'
            text_output = text_output + text
            number_rows -= 1
        print(text_output)
    elif input_text == '!help':
        print('''Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line
        Special commands: !help !done''')
    elif input_text == '!done':
        file = open("output.md", 'w')
        file.write(text_output)
    else:
        print('Unknown formatting type or command')
