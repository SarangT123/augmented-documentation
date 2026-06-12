import os


def build():
    docs_dir = 'website/static/docs'
    submodules_dir = 'website/static/docs/submodules'
    output_path = 'website/static/index.html'

    filenames = sorted(next(os.walk(docs_dir), (None, None, []))[2])
    filenames2 = sorted(next(os.walk(submodules_dir), (None, None, []))[2])

    main_cards = ''
    for fname in filenames:
        name = fname.split('.html')[0]
        main_cards += f'''
    <div class="card" style="width: 18rem; margin-right: 1rem; margin-left: 1rem;">
        <div class="card-body">
            <h5 class="card-title">{name}</h5>
            <p class="card-text">The documentation for <b>{name}</b> in "augmented"</p>
            <a href="docs/{fname}" class="card-link">View {name}</a>
        </div>
    </div>'''

    sub_cards = ''
    for fname in filenames2:
        name = fname.split('.html')[0]
        sub_cards += f'''
    <div class="card" style="width: 18rem; margin-right: 1rem; margin-left: 1rem;">
        <div class="card-body">
            <h5 class="card-title">{name}</h5>
            <p class="card-text">The documentation for <b>{name}</b> in "augmented"</p>
            <a href="docs/submodules/{fname}" class="card-link">View {name}</a>
        </div>
    </div>'''

    html = f'''<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-F3w7mX95PdgyTmZZMECAngseQB83DfGTowi0iMjiWaeVhAn4FJkqJByhZMI3AhiU" crossorigin="anonymous">
    <title>Augmented Documentation</title>
</head>

<body>
    <h1 class="text-center">Augmented Documentation</h1>
    <h2 class="text-center">Main modules</h2>
    <div class="d-flex justify-content-center">
    <br>
    {main_cards}
    </div>
    <h2 class="text-center">Sub modules</h2>
    <div class="d-flex justify-content-center">
    <br>
    {sub_cards}
    </div>
</body>

</html>'''

    with open(output_path, 'w') as f:
        f.write(html)

    print(f'Generated {output_path} ({len(filenames)} main, {len(filenames2)} sub modules)')


if __name__ == '__main__':
    build()
