import sys

def convert_to_html(markdown_text: str):

    counter = 0
    new_text: str = ""

    while(counter < len(markdown_text)):

        if (counter + 2 == len(markdown_text)):
            return new_text
    

        if(markdown_text[counter] == "*" and markdown_text[counter + 1] == "*"):
            new_text += "<b>"
            counter += 2;
            first_index = counter;
            if(counter >= len(markdown_text)):
                print("Incorect formating out of range", file=sys.stderr)
                #print(new_text);
                #print(counter)
                sys.exit(1)
            if(markdown_text[counter] != ' '):
                if(markdown_text[counter] == "*" and markdown_text[counter + 1] == "*"):
                    new_text += "</b>"
                    counter += 2
                else:
                    #print("hello")
                    while(markdown_text[counter] != "*" or markdown_text[counter + 1] != "*"):

                        new_text += markdown_text[counter]
                        #print(new_text)
                        counter += 1

                        
                        if(len(markdown_text) - 1 == counter):
                            print("Invalid formating there is no \'**\' at the end", file=sys.stderr)
                            sys.exit(1)

                        if(markdown_text[counter - 1] == "*" and markdown_text[counter] != "*"):
                            print("Invalid formating there is no \'**\' at the end", file=sys.stderr)
                            sys.exit(1)
                    
                    if(markdown_text[counter - 1] == " "):
                        print("Invalid formating: no space symbol is allowed right before \'**\'", file=sys.stderr)
                        sys.exit(1)

                    last_index = counter - 1;

                    Contain_Nested_Formating = IsContainNestedFormating(markdown_text,['_','`','```'], first_index, last_index)

                    if(Contain_Nested_Formating):
                        print("Invalid formating: contain nested formating is not allowed", file=sys.stderr)
                        sys.exit(1)
                        
                    new_text += "</b>"
                    counter += 2

                    if(counter == len(markdown_text)):
                        return new_text
            else:
                print("Invalid formating: no space symbol is allowed right after \'**\'", file=sys.stderr)
                sys.exit(1)

        
        elif(markdown_text[counter] == "_"):
            new_text += "<i>"
            counter += 1;
            if(counter >= len(markdown_text)):
                print("Incorrect formating: out of range", file=sys.stderr)
               # print(new_text);
               # print(counter)
                sys.exit(1)
            if(markdown_text[counter] != ' '):
                if(markdown_text[counter] == "_"):
                    new_text += "</i>"
                    counter += 1
                else:
                    #print("hello")
                    IsSnakeCase = False
                    IsEndOfString = False
                    while(markdown_text[counter] != "_" or IsSnakeCase):

                        new_text += markdown_text[counter]
                        #print(new_text)
                        counter += 1
                        
                        if(len(markdown_text) <= counter):
                            IsEndOfString = True
                            break

                        #print(counter)
                        if(len(markdown_text) -  1 == counter):
                            continue;
                        
                        if(markdown_text[counter] == "_" and markdown_text[counter - 1].isalpha() and markdown_text[counter + 1].isalpha()):
                            IsSnakeCase = True
                            #print("IsSnakeCase")
                        else:
                            IsSnakeCase = False
                            #print("IsNOTSnakeCase")

                    if(IsEndOfString):
                        print("Invalid formating: there is no \'_\' at the end", file=sys.stderr)
                        sys.exit(1)
                    
                    if(markdown_text[counter - 1] == " "):
                        print("Invalid formating: no space symbol is allowed right before \'_\'", file=sys.stderr)
                        sys.exit(1)
                    new_text += "</i>"
                    counter += 1
                   # print(new_text)

                    if(counter == len(markdown_text)):
                        return new_text
            else:
                print("Invalid formating: no space is allowed right after \'_\'", file=sys.stderr)
                sys.exit(1)

        elif(markdown_text[counter] == "`" and markdown_text[counter + 1] == "`" and  markdown_text[counter + 2] == "`"):
            print("i`m in ``` backtics text ")
            new_text += "<pre>"
            counter += 3;
           
            if(counter >= len(markdown_text)):
                print("Incorect formating out of range", file=sys.stderr)
                #print(new_text);
                #print(counter)
                sys.exit(1)
            if(markdown_text[counter] != ' '):
                if(markdown_text[counter] == "`" and markdown_text[counter + 1] == "`" and  markdown_text[counter + 2] == "`"):
                    new_text += "</pre>"
                    counter += 3
                else:
                    #print("hello")
                    
                    while(markdown_text[counter] != "`" or markdown_text[counter + 1] != "`" or  markdown_text[counter + 2] != "`"):

                        new_text += markdown_text[counter]
                        counter += 1

                        
                        if(len(markdown_text)  <= counter + 2):
                            print("Invalid formating there is no \'```\' at the end", file=sys.stderr)
                            sys.exit(1)

                    print(new_text)
                    if(markdown_text[counter - 1] == " "):
                        print("Invalid formating: no space symbol is allowed right before \'```\'asdasdasdas", file=sys.stderr)
                        sys.exit(1)
                    new_text += "</pre>"
                    counter += 3
                   # print(new_text)

                    if(counter == len(markdown_text)):
                        return new_text
            else:
                print("Invalid formating: no space symbol is allowed right after \'```\'", file=sys.stderr)
                sys.exit(1)

        elif(markdown_text[counter] == "`"):
            new_text += "<tt>"
            counter += 1;
            if(counter >= len(markdown_text)):
                print("Incorrect formating: out of range", file=sys.stderr)
               # print(new_text);
               # print(counter)
                sys.exit(1)
            if(markdown_text[counter] != ' '):
                if(markdown_text[counter] == "`"):
                    new_text += "</tt>"
                    counter += 1
                else:
                    IsEndOfString = False;
                    #print(IsEndOfString)
                    while(markdown_text[counter] != "`"):

                        new_text += markdown_text[counter]
                       # print(new_text)
                        counter += 1
                        #print(counter)

                        
                        if(len(markdown_text) == counter):
                            IsEndOfString = True
                            break;
                    
                    if(IsEndOfString):
                        print("Invalid formating: there is no \'`\' at the end", file=sys.stderr)
                        sys.exit(1)
                    if(markdown_text[counter - 1] == " "):
                        print("Invalid formating: no space symbol is allowed right before \'`\'", file=sys.stderr)
                        sys.exit(1)
                    new_text += "</tt>"
                    counter += 1
                    #print("out_of_while")

                    if(counter == len(markdown_text)):
                        return new_text
            else:
                print("Invalid formating: no space is allowed right after \'`\'", file=sys.stderr)
                sys.exit(1)

           # print("out of monospace")
            #print(new_text)
                

        if(counter == len(markdown_text)):
            return new_text
        
        while(markdown_text[counter] == " " or markdown_text[counter] == "\n" or markdown_text[counter] == "\t"):
            new_text += markdown_text[counter]
            counter += 1
            
            if(counter == len(markdown_text)):
                return new_text

    return new_text

def IsContainNestedFormating(text: str, list_of_contained_symbols: list, first_index: int, last_index: int):

    list_of_contained_symbols.sort();

    print(list_of_contained_symbols)

    first, second, third = list_of_contained_symbols;
    first = list_of_contained_symbols[0];
    print(first)
    len_of_largest_format_symbol = len(third);

    first_symbol = text[first_index]
    last_symbol = text[last_index]


    print(f"\n {first_symbol} , {last_symbol}")
    if(first_symbol != last_symbol):
        return False

    two_symbols_format = ""
    three_symbols_format = ""
    if(len_of_largest_format_symbol == 3):
        two_symbols_format = text[first_index:first_index + len_of_largest_format_symbol - 1];
    elif(len_of_largest_format_symbol == 2):
        three_symbols_format = text[first_index:first_index + len_of_largest_format_symbol - 1];
    
    print(list_of_contained_symbols[0])
    

    if(first_symbol == first):
        print("first")
        return True
    elif(first_symbol == second and last_symbol == second):
        print("second")
        return True 
    elif (first_symbol == third and last_symbol == third):
        print("thirds")
        result = True;

    return False;

def read_file(input_path):
    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

def save_to_file(html_text, output_path):
    try:
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(html_text)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)



if __name__ == "__main__":

    argv_len = len(sys.argv)

    if (argv_len < 2  or argv_len > 3):
        print("Invalid amount of parametrs", file=sys.stderr)
        sys.exit(1)

    input_file = sys.argv[1]
    markdown_text = read_file(input_file)
    html_text = convert_to_html(markdown_text)

    if (argv_len == 3):
        output_file = sys.argv[2]
        save_to_file(html_text, output_file)
        print(f"File was successfuly converted to HTML and saved to {output_file}")
    else:
        print(html_text)
