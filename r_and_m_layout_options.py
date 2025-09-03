import requests

# Base URL
url = "https://rickandmortyapi.com/api/character"

# Request API data
response = requests.get(url)
data = response.json()

# Start HTML structure
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rick and Morty Characters</title>
</head>
<body>
    <h1>Rick and Morty Characters</h1>
"""

# ----------------------------------------
# Section 1: Using <strong>
# ----------------------------------------
html_content += "<h2>Version 1: Using &lt;strong&gt;</h2>"
for char in data["results"]:
    html_content += f"""
    <div>
        <img src="{char['image']}" width="100" alt="{char['name']}">
        <h3>{char['name']}</h3>
        <p><strong>Status:</strong> {char['status']}</p>
        <p><strong>Species:</strong> {char['species']}</p>
        <p><strong>Origin:</strong> {char['origin']['name']}</p>
    </div>
    """

# ----------------------------------------
# Section 2: Using <dl>
# ----------------------------------------
html_content += "<h2>Version 2: Using &lt;dl&gt;</h2>"
for char in data["results"]:
    html_content += f"""
    <div>
        <img src="{char['image']}" width="100" alt="{char['name']}">
        <h3>{char['name']}</h3>
        <dl>
            <dt>Status:</dt>
            <dd>{char['status']}</dd>
            <dt>Species:</dt>
            <dd>{char['species']}</dd>
            <dt>Origin:</dt>
            <dd>{char['origin']['name']}</dd>
        </dl>
    </div>
    """

# ----------------------------------------
# Section 3: Using <table> (characters in columns)
# ----------------------------------------
html_content += "<h2>Version 3: Using &lt;table&gt; (Side-by-Side)</h2>"
html_content += "<table border='1' cellpadding='5' cellspacing='0'>"

# Table header row (character names + images)
html_content += "<tr><th>Attribute</th>"
for char in data["results"]:
    html_content += f"""
        <th>
            <img src="{char['image']}" width="80" alt="{char['name']}"><br>
            {char['name']}
        </th>
    """
html_content += "</tr>"

# Row: Status
html_content += "<tr><th scope='row'>Status</th>"
for char in data["results"]:
    html_content += f"<td>{char['status']}</td>"
html_content += "</tr>"

# Row: Species
html_content += "<tr><th scope='row'>Species</th>"
for char in data["results"]:
    html_content += f"<td>{char['species']}</td>"
html_content += "</tr>"

# Row: Origin
html_content += "<tr><th scope='row'>Origin</th>"
for char in data["results"]:
    html_content += f"<td>{char['origin']['name']}</td>"
html_content += "</tr>"

html_content += "</table>"

# End HTML structure
html_content += """
</body>
</html>
"""

# Write to HTML file
with open("rick_and_morty_versions.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("HTML file created: rick_and_morty_versions.html")
