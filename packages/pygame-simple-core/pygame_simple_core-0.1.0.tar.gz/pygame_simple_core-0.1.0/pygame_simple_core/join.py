import os


content = ''

for path in (
    'tools/font_finder.py',
    'tools/font_loader.py',
    'tools/scheduled_event.py',
    'widgets/button.py',
    'widgets/container.py',
    'widgets/fps_counter.py',
    'widgets/text.py',
    'core.py'
):
    with open(path, 'r') as file:
        content = f'{content}{path}/n{file.read()}'

print(content)

