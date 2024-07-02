from jinja2 import Environment, FileSystemLoader
import os

# Установите путь к папке с шаблонами
template_dir = os.path.join(os.path.dirname(__file__), 'templates')

# Создайте окружение Jinja
env = Environment(loader=FileSystemLoader(template_dir))

# Список шаблонов для рендеринга
templates = ['home.html', 'about.html']

# Рендеринг каждого шаблона
for template_name in templates:
    # Загрузите шаблон
    template = env.get_template(template_name)

    # Данные для шаблона (если они необходимы)
    data = {}

    # Рендеринг шаблона с данными
    rendered_content = template.render(data)

    # Запись сгенерированного HTML в файл
    output_path = os.path.join(os.path.dirname(__file__), f'output_{template_name}')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(rendered_content)

    print(f'HTML файл создан: {output_path}')