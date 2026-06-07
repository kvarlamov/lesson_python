from pymonad.tools import curry
from pymonad.reader import Compose

# 2-1

@curry(2)
def tag(tag_name, value):
    return f'<{tag_name}>{value}</{tag_name}>'

bold   = tag('b')
italic = tag('i')

# пример
print(bold('Жирный текст'))
print(italic('Текст курсивом'))

# пример Compose
bold_italic = (Compose(italic)
                   .then(bold))

print(bold_italic('жирный курсив'))

# 2-2
@curry(3)
def tag(tag_name, attr, value):
    if attr:
        attrs_str = ' '.join(f'{k}="{v}"' for k, v in attr.items())
        return f'<{tag_name} {attrs_str}>{value}</{tag_name}>'
    return f'<{tag_name}>{value}</{tag_name}>'

bold   = tag('b', {})
italic = tag('i', {})

list_item   = tag('li', {'class': 'list-group'})

print(tag('li', {'class': 'list-group'}, 'item 23')) # <li class="list-group">item 23</li>

# примеры
print(bold('жирный'))
print(list_item('item 1'))

bold_list_item = (Compose(list_item)
                      .then(bold))

print(bold_list_item('item 42')) # <b><li class="list-group">item 42</li></b>