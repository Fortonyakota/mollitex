import pandas as pd

# Example data (list of dictionaries)
data = [
    {'RepoID': 1, 'RepoLanguage': 'Python'},
    {'RepoID': 2, 'RepoLanguage': 'Java'},
    {'RepoID': 3, 'RepoLanguage': 'JavaScript'}
]

# Create a DataFrame using Pandas
df = pd.DataFrame(data, columns=columns)

# Display the DataFrame
print(df)
