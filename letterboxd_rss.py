import requests
from bs4 import BeautifulSoup

# Replace this with your actual Letterboxd diary URL
diary_url = "https://letterboxd.com/adamkoplik/films/diary/"

response = requests.get(diary_url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all diary entries
entries = soup.find_all("li", class_="diary-entry-row")

movie_cards = ""

for entry in entries:
    title_tag = entry.find("td", class_="diary-entry-title")
    if title_tag:
        title = title_tag.get_text(strip=True)
    else:
        continue

    # Star rating
    rating_tag = entry.find("span", class_="rating")
    rating = rating_tag.get_text(strip=True) if rating_tag else "No rating"

    # Watch date
    date_tag = entry.find("td", class_="diary-day")
    date = date_tag.get_text(strip=True) if date_tag else "Unknown date"

    # Poster image
    poster_tag = entry.find("img")
    poster_url = poster_tag["src"] if poster_tag else ""

    # Film page link
    film_link_tag = title_tag.find("a")
    film_link = "https://letterboxd.com" + film_link_tag["href"] if film_link_tag else "#"

    # Build the HTML for each movie card
    movie_cards += f"""
    <div class="movie-card" style="background-image: url('{poster_url}');">
      <div class="movie-info">
        <h4>{title}</h4>
        <p>{rating}</p>
      </div>
      <div class="movie-hover">
        <p>Watched on {date}<br><a href="{film_link}" target="_blank">View on Letterboxd →</a></p>
      </div>
    </div>
    """

# Final page template
html_template = f"""
<!DOCTYPE html>
<html>
<head>
  <title>Adam's Letterboxd Diary</title>
  <style>
    body {{
      background: #111;
      color: #fff;
      font-family: sans-serif;
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      padding: 20px;
    }}
    .movie-card {{
      position: relative;
      background-size: cover;
      background-position: center;
      width: 180px;
      height: 270px;
      border-radius: 10px;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      justify-content: flex-end;
      margin: 10px;
      transition: transform 0.3s;
    }}
    .movie-card:hover {{
      transform: scale(1.03);
    }}
    .movie-info {{
      background: rgba(0,0,0,0.75);
      color: #fff;
      padding: 10px;
      text-align: center;
    }}
    .movie-hover {{
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: rgba(0,0,0,0.85);
      color: #fff;
      opacity: 0;
      padding: 10px;
      display: flex;
      align-items: center;
      justify-content: center;
      text-align: center;
      transition: opacity 0.3s;
    }}
    .movie-card:hover .movie-hover {{
      opacity: 1;
    }}
    a {{
      color: #1db954;
      text-decoration: none;
    }}
  </style>
</head>
<body>
{movie_cards}
</body>
</html>
"""

# Save to file
with open("letterboxd_diary.html", "w", encoding="utf-8") as f:
    f.write(html_template)

print("✅ Diary page generated as letterboxd_diary.html")
