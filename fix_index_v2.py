import re

with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    if 'elementor-nav-menu' in line and 'data-settings' in line:
        # استبدال الجزء المعطوب بالكامل داخل هذا السطر
        line = re.sub(r'data-settings="\{.*?\}"', 'data-settings=\'{"submenu_icon":{"value":"<i class=\\"fas fa-chevron-down\\"></i>","library":"fa-solid"},"full_width":"stretch","layout":"horizontal","toggle":"burger"}\'', line)
        # تنظيف أي سمات غريبة مثل 0="" أو 448=""
        line = re.sub(r'\s\d+=""', '', line)
    new_lines.append(line)

with open('index.html', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("تمت المحاولة الثانية للإصلاح.")
