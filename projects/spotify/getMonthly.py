import requests
import csv

url = "https://chartmasters.org/wp-admin/admin-ajax.php?action=get_wdtable&table_id=74"

headers = {
    "User-Agent": "Mozilla/5.0",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Requested-With": "XMLHttpRequest",
    "Origin": "https://chartmasters.org",
    "Referer": "https://chartmasters.org/most-monthly-listeners-on-spotify/"
}

all_rows = []
start = 0
length = 1000

# Use your current nonce here
wdtNonce = "674fa59e7b"

while True:
    payload = {
        "draw": str(start // length + 1),
        "start": str(start),
        "length": str(length),
        "order[0][column]": "4",  # order by listeners
        "order[0][dir]": "desc",

        "columns[0][data]": "0",
        "columns[0][name]": "rank",
        "columns[0][searchable]": "false",
        "columns[0][orderable]": "true",
        "columns[0][search][value]": "",
        "columns[0][search][regex]": "false",

        "columns[1][data]": "1",
        "columns[1][name]": "g#",
        "columns[1][searchable]": "false",
        "columns[1][orderable]": "true",
        "columns[1][search][value]": "",
        "columns[1][search][regex]": "false",

        "columns[2][data]": "2",
        "columns[2][name]": "pic",
        "columns[2][searchable]": "false",
        "columns[2][orderable]": "false",
        "columns[2][search][value]": "",
        "columns[2][search][regex]": "false",

        "columns[3][data]": "3",
        "columns[3][name]": "artist",
        "columns[3][searchable]": "true",
        "columns[3][orderable]": "true",
        "columns[3][search][value]": "",
        "columns[3][search][regex]": "false",

        "columns[4][data]": "4",
        "columns[4][name]": "listeners",
        "columns[4][searchable]": "true",
        "columns[4][orderable]": "true",
        "columns[4][search][value]": "",
        "columns[4][search][regex]": "false",

        "columns[5][data]": "5",
        "columns[5][name]": "daily",
        "columns[5][searchable]": "true",
        "columns[5][orderable]": "true",
        "columns[5][search][value]": "",
        "columns[5][search][regex]": "false",

        "columns[6][data]": "6",
        "columns[6][name]": "monthly",
        "columns[6][searchable]": "true",
        "columns[6][orderable]": "true",
        "columns[6][search][value]": "",
        "columns[6][search][regex]": "false",

        "columns[7][data]": "7",
        "columns[7][name]": "artist_spotify_id",
        "columns[7][searchable]": "false",
        "columns[7][orderable]": "false",
        "columns[7][search][value]": "",
        "columns[7][search][regex]": "false",

        "columns[8][data]": "8",
        "columns[8][name]": "country",
        "columns[8][searchable]": "true",
        "columns[8][orderable]": "false",
        "columns[8][search][value]": "",
        "columns[8][search][regex]": "false",

        "columns[9][data]": "9",
        "columns[9][name]": "genre",
        "columns[9][searchable]": "true",
        "columns[9][orderable]": "false",
        "columns[9][search][value]": "",
        "columns[9][search][regex]": "false",

        "columns[10][data]": "10",
        "columns[10][name]": "language",
        "columns[10][searchable]": "true",
        "columns[10][orderable]": "false",
        "columns[10][search][value]": "",
        "columns[10][search][regex]": "false",

        "columns[11][data]": "11",
        "columns[11][name]": "gender",
        "columns[11][searchable]": "true",
        "columns[11][orderable]": "false",
        "columns[11][search][value]": "",
        "columns[11][search][regex]": "false",

        "search[value]": "",
        "search[regex]": "false",

        "wdtNonce": wdtNonce,
    }

    response = requests.post(url, data=payload, headers=headers)
    data_json = response.json()

    rows = data_json.get("data", [])
    print(f"Fetched {len(rows)} rows starting at {start}")

    if not rows:
        print("No more data, stopping.")
        break

    all_rows.extend(rows)
    start += length

# Write to CSV
csv_headers = [
    "rank", "g#", "pic", "artist", "listeners", "daily", "monthly",
    "artist_spotify_id", "country", "genre", "language", "gender"
]

with open("chartmasters_table74.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(csv_headers)
    for row in all_rows:
        writer.writerow(row)

print(f"Saved {len(all_rows)} rows to chartmasters_table74.csv")
