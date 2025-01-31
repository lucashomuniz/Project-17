
"""
=================
NETFLIX EXERCISE
=================
"""

import pandas

# ANÁLISE EXPLORATÓRIA
excel_file = pandas.ExcelFile('NFLX_DS_03_22_24_Data.xlsx')
dataset1 = pandas.read_excel(excel_file, 'NFLX Top 10')
dataset2 = pandas.read_excel(excel_file, 'IMDB Rating')
dataset3 = pandas.read_excel(excel_file, 'Runtime')

# PART 1 - QUESTION 1
# IN THE ‘FILMS (ENGLISH)’ CATEGORY, WHICH FILM HAS THE MOST APPEARANCES IN OUR DATA SET (NFLX TOP 10 TAB)? WHAT WERE ITS AVERAGE WEEKLY HOURS VIEWED?
print('PART 1 - QUESTION 1')
dataset1_outage = dataset1.loc[dataset1['weekly_hours_viewed'] != 0]
dataset1_outage_english_films = dataset1_outage[dataset1_outage['category'] == 'Films (English)']
film_counts = dataset1_outage_english_films['show_title'].value_counts()
most_common_film = film_counts.idxmax()
max_occurrences = film_counts.max()
print(f'Film Name: {most_common_film}')
print(f'Total Occurrences: {max_occurrences}')
avg_weekly_hours_1 = dataset1_outage[dataset1_outage['show_title'] == most_common_film]['weekly_hours_viewed'].mean()
print(f'Average Weekly Hours Viewed: {avg_weekly_hours_1}')
print("")

# PART 1 - QUESTION 2
# IN THE 'FILMS (ENGLISH)' CATEGORY, WHICH FILM HAS THE LOWEST IMDB RATING? WHAT WERE ITS AVERAGE WEEKLY HOURS VIEWED?
print('PART 1 - QUESTION 2')
dataset2.rename(columns={'title': 'show_title'}, inplace=True)
dataset2_unique = dataset2.drop_duplicates(subset=['show_title'])
merged_dataset = pandas.merge(dataset1_outage_english_films, dataset2[['show_title', 'rating']], on='show_title', how='left')
imdb_lowest_film = merged_dataset.loc[merged_dataset['rating'].idxmin(), 'show_title']
avg_weekly_hours_2 = merged_dataset.loc[merged_dataset['show_title'] == imdb_lowest_film, 'weekly_hours_viewed'].mean()
print(f'Film Name: {imdb_lowest_film}')
print(f'Average Weekly Hours Viewed: {avg_weekly_hours_2:.0f}')
print("")

# PART 1 - QUESTION 3
# IN THE 'FILMS (NON-ENGLISH)' CATEGORY, WHICH FILM HAS SPENT THE MOST WEEKS IN THE TOP 10?
# TO ESTIMATE THE NUMBER OF USERS WHO WATCHED THIS FILM, WHAT ASSUMPTIONS WOULD YOU MAKE AND WHAT RISKS ARE INVOLVED?
print('PART 1 - QUESTION 3')
dataset1_outage_noenglish_films = dataset1_outage[dataset1_outage['category'] == 'Films (Non-English)']
most_weeks_top10 = dataset1_outage_noenglish_films.nlargest(1, 'cumulative_weeks_in_top_10')
film_most_weeks_top10 = most_weeks_top10.iloc[0]['show_title']
qty_most_weeks_top10 = most_weeks_top10.iloc[0]['cumulative_weeks_in_top_10']
print(f'Film Name: {film_most_weeks_top10}')
print(f'Weeks in Top10: {qty_most_weeks_top10}')
total_weekly_hours = dataset1_outage_noenglish_films[dataset1_outage_noenglish_films['show_title'] == film_most_weeks_top10]['weekly_hours_viewed']
last_four_results = total_weekly_hours.tail(4).sum()
print(f'Average 4 Weeks Hours Viewed: {last_four_results}')
