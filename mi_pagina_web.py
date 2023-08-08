from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    title = "Fotos de aviones Airbus y Boeing de las mejores aerolíneas comerciales"
    subtitle = "En esta página te mostraré fotos de los mejores aviones y aerolíneas del mundo :)"
    
    images = [
        {
            'src': 'https://cdn.jetphotos.com/full/6/697515_1678389991.jpg',
            'description': 'Aircraft: Boeing 747-47UF(SCD) - Airline: Atlas Air'
        },
        {
            'src': 'https://cdn.jetphotos.com/full/5/519256_1676916847.jpg',
            'description': 'Aircraft: Boeing 737-8 MAX - Airline: Southwest Airlines '
        },
        {
            'src': 'https://cdn.jetphotos.com/full/5/38468_1641268379.jpg',
            'description': 'Aircraft: Airbus A320-271N - Airline: JetSmart'
        },
        {
            'src': 'https://cdn.jetphotos.com/full/5/1011920_1686098677.jpg',
            'description': 'Aircraft: Boeing 747-8B5 - Airline: Korean Air'
        }
    ]
    
    image_tags = ""
    for image in images:
        image_tags += f"<img src='{image['src']}' alt='{image['description']}' class='small-img'>"

    page_content = f"<h1>{title}</h1><h2>{subtitle}</h2>{image_tags}"
    
    return f"""
    <html>
    <head>
        <title>Mi Página Web</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: lightgreen;
                margin: 0;
                padding: 20px;
            }}
            
            .container {{
                max-width: 800px;
                margin: 0 auto;
            }}
            
            .small-img {{
                max-width: 300px;
                height: auto;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            {page_content}
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run()
