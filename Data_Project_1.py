import pandas as pd
import json
import sqlite3

# Function to load CSV data
def load_csv(file_path):
    try:
        df = pd.read_csv(file_path)
        print("Initial Data:", len(df), "records,", len(df.columns), "columns")
        print("Columns in CSV:", df.columns)  # Print column names for verification
        return df
    except Exception as e:
        print(f"Error loading CSV: {e}")
        return None

# Function to load JSON data
def load_json(file_path):
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        df = pd.DataFrame(data)
        print("Initial Data:", len(df), "records,", len(df.columns), "columns")
        print("Columns in JSON:", df.columns)  # Print column names for verification
        return df
    except Exception as e:
        print(f"Error loading JSON: {e}")
        return None

# Function to transform data (add columns and drop columns)
def transform_data(df, add_cols=None, drop_cols=None):
    # Add new columns if specified
    if add_cols:
        for col in add_cols:
            df[col] = None  # Initialize the new column with None or any other logic

    # Drop columns if specified
    if drop_cols:
        try:
            df = df.drop(columns=drop_cols)
        except KeyError as e:
            print(f"Error dropping columns: {e}")

    print("Transformed Data:", len(df), "records,", len(df.columns), "columns")
    return df

# Function to save the transformed data
def save_data(df, file_path, output_format):
    if output_format == 'csv':
        df.to_csv(file_path, index=False)
    elif output_format == 'json':
        df.to_json(file_path, orient='records')
    elif output_format == 'sql':
        save_to_sql(df, file_path)
    else:
        print(f"Unsupported output format: {output_format}")

# Function to save DataFrame to SQL
def save_to_sql(df, db_name):
    try:
        conn = sqlite3.connect(db_name)
        df.to_sql('drake_lyrics', conn, if_exists='replace', index=False)
        conn.close()
        print(f"Data saved to SQL database: {db_name}")
    except Exception as e:
        print(f"Error saving to SQL: {e}")

# ETL Pipeline function
def etl_pipeline(file_path, source_type, output_format, add_cols=None, drop_cols=None):
    # Load the data based on the source type
    if source_type == 'csv':
        df = load_csv(file_path)
    elif source_type == 'json':
        df = load_json(file_path)
    else:
        print(f"Unsupported source type: {source_type}")
        return

    # Transform the data
    df_transformed = transform_data(df, add_cols=add_cols, drop_cols=drop_cols)

    # Save the transformed data
    output_file = f"transformed_data.{output_format}" if output_format != 'sql' else 'drake_lyrics.db'
    save_data(df_transformed, output_file, output_format)

    print(f"Data saved to {output_file}")

# Example Usage
etl_pipeline('drake_data.json', source_type='json', output_format='sql', add_cols=['Lyric_Score'], drop_cols=['lyrics_url'])



#I used chatGPT and stackoverflow to help with this code