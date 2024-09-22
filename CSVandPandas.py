# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Task 1: Reading the CSV File
# Load the CSV file into a pandas DataFrame
df = pd.read_csv("acc_players-2324F.csv", header=1)

# Display the first 5 rows of the DataFrame to understand the structure of the data
print("First 5 rows of the DataFrame:")
print(df.head())

# Task 2: Basic Analysis
# Calculate the total points scored by all players combined
total_points = df['PTS'].sum()
print("\nTotal points scored by all players:", total_points)

# Find the player who has played the most minutes (MP)
most_minutes_player = df.loc[df['MP'].idxmax(), 'Player']
print("Player with the most minutes:", most_minutes_player)

# Identify the top 5 players in terms of total rebounds (TRB)
top_rebounders = df[['Player', 'TRB']].sort_values(by='TRB', ascending=False).head(5)
print("Top 5 players in total rebounds:\n", top_rebounders)

# Task 3: Player Filtering
# Create a new DataFrame containing only players who played more than 500 minutes
filtered_df = df[df['MP'] > 500]

# From this filtered DataFrame, determine the player with the highest total assists (AST)
highest_assist_player = filtered_df.loc[filtered_df['AST'].idxmax(), 'Player']
print("\nPlayer with the highest assists (more than 500 minutes):", highest_assist_player)

# Who are the top 3 Assist Leads in the League?
top_assist_leaders = filtered_df[['Player', 'AST']].sort_values(by='AST', ascending=False).head(3)
print("Top 3 Assist Leaders:\n", top_assist_leaders)

# Who are the top 3 Shot Blockers?
top_blockers = filtered_df[['Player', 'BLK']].sort_values(by='BLK', ascending=False).head(3)
print("Top 3 Shot Blockers:\n", top_blockers)

# Task 4: School-Based Analysis
# Group the players by School and calculate the total points scored by each school
school_points = df.groupby('School')['PTS'].sum().reset_index()
print("\nTotal points scored by each school:\n", school_points)

# Group the players by School and calculate the total assists (AST) for each team
school_assists = df.groupby('School')['AST'].sum().reset_index()
print("Total assists by each school:\n", school_assists)

# Sort the schools by total points scored and display the top 3 schools
top_schools = school_points.sort_values(by='PTS', ascending=False).head(3)
print("Top 3 schools by total points scored:\n", top_schools)

# Task 5: Extra Credit (Bonus)
# Create a bar chart showing the top 5 players by total points scored (PTS)
top_5_scorers = df[['Player', 'PTS']].sort_values(by='PTS', ascending=False).head(5)
plt.bar(top_5_scorers['Player'], top_5_scorers['PTS'], color='skyblue')
plt.xlabel('Player')
plt.ylabel('Total Points')
plt.title('Top 5 Players by Total Points')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Correlation: Investigate whether there is any correlation between a player's field goal percentage (FG%) and their win shares (WS)
correlation = df['FG%'].corr(df['WS'])
print("\nCorrelation between FG% and WS:", correlation)

# Provide a scatter plot for the correlation
plt.scatter(df['FG%'], df['WS'], color='purple')
plt.xlabel('Field Goal Percentage (FG%)')
plt.ylabel('Win Shares (WS)')
plt.title('Correlation between FG% and WS')
plt.show()


#I used stack overflow and OpenAI to help with this assignment