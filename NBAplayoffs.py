import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Correct file paths to your local systemregular_season_df = pd.read_csv('C:\\Users\\amani\\DataSystems\\csv_files\\2023-2024 NBA Player Stats - Regular.csv', sep=';', encoding='latin1')

regular_season_df = pd.read_csv(r'C:\Users\amani\DataSystems\2023-2024 NBA Player Stats - Regular.csv', sep=';', encoding='latin1')
playoffs_df = pd.read_csv(r'C:\Users\amani\DataSystems\2023-2024 NBA Player Stats - Playoffs.csv', sep=';', encoding='latin1')


# Display the first few rows of each dataset
print("Regular Season Stats:")
print(regular_season_df.head())

print("\nPlayoff Stats:")
print(playoffs_df.head())

# Get basic information about the datasets
print("\nRegular Season Data Info:")
regular_season_df.info()

print("\nPlayoff Data Info:")
playoffs_df.info()

# Check for missing values
print("\nMissing Values in Regular Season Data:")
print(regular_season_df.isnull().sum())

print("\nMissing Values in Playoff Data:")
print(playoffs_df.isnull().sum())

# Get statistical summaries of the data
print("\nStatistical Summary (Regular Season):")
print(regular_season_df.describe())

print("\nStatistical Summary (Playoffs):")
print(playoffs_df.describe())

# Cleaning Data - Dropping any rows with missing values (if necessary)
regular_season_df = regular_season_df.dropna()
playoffs_df = playoffs_df.dropna()

# Rename columns for easier access
regular_season_df.rename(columns={'Tm': 'Team','PTS': 'Points', 'TRB': 'Rebounds', 'AST': 'Assists'}, inplace=True)
playoffs_df.rename(columns={'Tm': 'Team','PTS': 'Points', 'TRB': 'Rebounds', 'AST': 'Assists'}, inplace=True)

print("\nUpdated Regular Season Columns:")
print(regular_season_df.columns)

print("\nUpdated Playoff Columns:")
print(playoffs_df.columns)

# Top 10 players with the most points in the regular season
top_scorers_regular = regular_season_df[['Player', 'Points']].sort_values(by='Points', ascending=False).head(10)
print("\nTop 10 Regular Season Scorers:")
print(top_scorers_regular)

# Top 10 players with the most points in the playoffs
top_scorers_playoffs = playoffs_df[['Player', 'Points']].sort_values(by='Points', ascending=False).head(10)
print("\nTop 10 Playoff Scorers:")
print(top_scorers_playoffs)

# Grouping the data by 'Team' and calculating the average stats for each team
team_avg_stats_regular = regular_season_df.groupby('Team')[['Points', 'Rebounds', 'Assists']].mean().reset_index()
print("\nAverage Team Stats (Regular Season):")
print(team_avg_stats_regular)

# Similarly for playoffs
team_avg_stats_playoffs = playoffs_df.groupby('Team')[['Points', 'Rebounds', 'Assists']].mean().reset_index()
print("\nAverage Team Stats (Playoffs):")
print(team_avg_stats_playoffs)

# Plotting
sns.set(style="whitegrid")

# Bar chart of the top 10 regular season scorers
plt.figure(figsize=(10,6))
sns.barplot(x='Points', y='Player', data=top_scorers_regular)
plt.title('Top 10 Regular Season Scorers')
plt.show()

# Bar chart of the top 10 playoff scorers
plt.figure(figsize=(10,6))
sns.barplot(x='Points', y='Player', data=top_scorers_playoffs)
plt.title('Top 10 Playoff Scorers')
plt.show()

# Plot a comparison of average team stats between regular season and playoffs
team_avg_stats = pd.merge(team_avg_stats_regular, team_avg_stats_playoffs, on='Team', suffixes=('_Regular', '_Playoffs'))

plt.figure(figsize=(12,8))
sns.barplot(x='Points_Regular', y='Team', data=team_avg_stats, color="b", label="Regular Season")
sns.barplot(x='Points_Playoffs', y='Team', data=team_avg_stats, color="r", label="Playoffs")
plt.title('Average Points per Team: Regular Season vs Playoffs')
plt.legend()
plt.show()

# Exercise 1: Top 10 Rebounders
top_rebounders_regular = regular_season_df[['Player', 'Rebounds']].sort_values(by='Rebounds', ascending=False).head(10)
print("\nTop 10 Regular Season Rebounders:")
print(top_rebounders_regular)

top_rebounders_playoffs = playoffs_df[['Player', 'Rebounds']].sort_values(by='Rebounds', ascending=False).head(10)
print("\nTop 10 Playoff Rebounders:")
print(top_rebounders_playoffs)

# Exercise 2: Assists Leader by Team
assists_leader_regular = regular_season_df.loc[regular_season_df.groupby('Team')['Assists'].idxmax(), ['Team', 'Player', 'Assists']]
print("\nAssists Leaders by Team (Regular Season):")
print(assists_leader_regular)

assists_leader_playoffs = playoffs_df.loc[playoffs_df.groupby('Team')['Assists'].idxmax(), ['Team', 'Player', 'Assists']]
print("\nAssists Leaders by Team (Playoffs):")
print(assists_leader_playoffs)

# Exercise 3: Visualize Rebounds per Team
team_avg_rebounds_regular = regular_season_df.groupby('Team')['Rebounds'].mean().reset_index()
team_avg_rebounds_playoffs = playoffs_df.groupby('Team')['Rebounds'].mean().reset_index()

team_avg_rebounds = pd.merge(team_avg_rebounds_regular, team_avg_rebounds_playoffs, on='Team', suffixes=('_Regular', '_Playoffs'))

# Plot average rebounds for regular season and playoffs
plt.figure(figsize=(12,8))
sns.barplot(x='Rebounds_Regular', y='Team', data=team_avg_rebounds, color="b", label="Regular Season")
sns.barplot(x='Rebounds_Playoffs', y='Team', data=team_avg_rebounds, color="r", label="Playoffs")
plt.title('Average Rebounds per Team: Regular Season vs Playoffs')
plt.legend()
plt.show()

# Finding the team with the biggest change in rebounds
team_avg_rebounds['Change'] = team_avg_rebounds['Rebounds_Playoffs'] - team_avg_rebounds['Rebounds_Regular']
biggest_change_team = team_avg_rebounds.loc[team_avg_rebounds['Change'].idxmax()]
print("\nTeam with the Biggest Increase in Rebounds:")
print(biggest_change_team)


#I wrote this code with the help of stack overflow