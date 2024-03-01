import requests
import json

with open('nr.txt', 'r') as file:
    numbers = file.read().splitlines()
    
links = []
with open("xkcd_links.txt", "w") as links_file:
    for number in numbers:
        response = requests.get(f'https://xkcd.com/{number}/info.0.json')
        data = response.json()
        image_link = data['img']

        links_file.write(image_link + '\n')
        links.append(image_link)
links_file.close()
    
html_content = """
<!DOCTYPE html>
<html lang="pl-PL">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>XKCD Comic strips</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
<body>
    <div class="container">
        <h1 class="my-5">XKCD Comics</h1>
"""

for i, link in enumerate(links):
    html_content += f"""
    <div class="row">
        <div class="col mb-5">
            <img src="{link}" class="img-fluid" alt="XKCD Comic {numbers[i]}">
        </div>
    </div>
    """
    
html_content += """
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous">
</body>
</html>
"""

with open('xkcd_comics.html', 'w') as html_file:
    html_file.write(html_content)