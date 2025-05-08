import requests
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://www.pro-football-reference.com/years/2022/games.htm'
response = requests.get(url)

if response.status_code == 200: #error if code = 200
    print("Request successful!")
else:
    print("Request failed with status code:", response.status_code)

soup = BeautifulSoup(response.text, 'html.parser') 

#find first table element
table = soup.find('table', {'id':  'games'})

#get headers
headers = []
for th in table.find_all('th'):
    text = th.getText()
    if text and not text.isdigit() and text not in headers:
        headers.append(text)
#slice out playoff weeks (they are rows, not headers)
headers = headers[:12]

#get rows
rows = []
tbody = table.find('tbody')

for tr in tbody.find_all('tr'):
    week_cell = tr.find('th')  # Find the header cell in the row
    week = week_cell.getText().strip() if week_cell else None  # Extract week number if it exists

    
    row_data = tr.find_all('td')
    
    if row_data:
        cleaned_data = [week]  
        # Clean and store the text from each data cell
        for cell in row_data:
            cell = cell.getText().strip()
            if cell and cell != "@" and cell != "boxscore":
                cleaned_data.append(cell)
        
        rows.append(cleaned_data)  # Append the cleaned data to the rows list

#print(f'Headers: {headers}')
#print(f'Rows: {rows[0]}')

#map headers and rows together
final_data = [] #list of dictionaries
for row in rows:
    if len(row) == len(headers):
        row_dict = dict(zip(headers, row))

        final_data.append(row_dict)


# converting strings to numerical values
for game in final_data:
    if not isinstance(game['Week'], str):
        game['Week'] = int(game['Week']) if game['Week'] else 0 # Week of game

    game['PtsW'] = int(game['PtsW']) if game['PtsW'] else 0  # Points for Winner
    game['PtsL'] = int(game['PtsL']) if game['PtsL'] else 0  # Points for Loser
    game['YdsW'] = int(game['YdsW']) if game['YdsW'] else 0  # Yards for Winner
    game['YdsL'] = int(game['YdsL']) if game['YdsL'] else 0  # Yards for Loser
    game['TOW'] = int(game['TOW']) if game['TOW'] else 0 # Time outs for winner
    game['TOL'] = int(game['TOL']) if game['TOL'] else 0 # Time outs for loser

df = pd.DataFrame(final_data)
df.to_csv('nfl_2022_data.csv', index=False)
