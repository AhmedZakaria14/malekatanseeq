import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. إصلاح الكود المعطوب في الـ nav-menu (الذي يحتوي على تكرار أو أخطاء في الـ SVG)
# سنقوم بتنظيف الـ data-settings التي يبدو أنها تسببت في المشكلة
broken_pattern = r'data-settings="\{.*?<\/path><\/svg>","library":"fa-solid"\},"full_width":"stretch","layout":"horizontal","toggle":"burger"\}"'
fixed_settings = 'data-settings=\'{"submenu_icon":{"value":"<i class=\\"fas fa-chevron-down\\"></i>","library":"fa-solid"},"full_width":"stretch","layout":"horizontal","toggle":"burger"}\''
content = re.sub(broken_pattern, fixed_settings, content)

# 2. استبدال روابط / بروابط نسبية /
# سنستهدف الروابط في القائمة والروابط العامة
content = content.replace('/', '/')
content = content.replace('/', '/')

# 3. تحديث العناوين والنصوص التي تشير إلى "زهرتي" لتناسب الموقع الجديد (ملك التنسيق)
content = content.replace('زهرتي', 'ملك التنسيق')
content = content.replace('تواصل معنا - ملك التنسيق', 'تواصل معنا - ملك التنسيق')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("تم تحديث الملف بنجاح.")
