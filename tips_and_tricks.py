# Lambda explanation
# This is how to process a dictionary's items

# Understanding Lambda Functions
## What is a Lambda?
#A lambda is an anonymous function in Python, written as `lambda arguments: expression`.

## Example:
lambda x: x * 2
#is really just a simple version of:
def double(x):
    return x * 2

#CH8 Decorators -> L3 Decorators

def markdown_to_text_decorator(func):
    
    def wrapper(*args, **kwargs):
        
        new_list = list(map(convert_md_to_txt, args))
        new_dict = dict(map(lambda item: (item[0], convert_md_to_txt(item[1])), kwargs.items()))
        
        return func(*new_list, **new_dict)
        pass

    return wrapper

# don't touch below this line

def convert_md_to_txt(doc):
    lines = doc.split("\n")
    for i in range(len(lines)):
        line = lines[i]
        lines[i] = line.lstrip("# ")
    return "\n".join(lines)
