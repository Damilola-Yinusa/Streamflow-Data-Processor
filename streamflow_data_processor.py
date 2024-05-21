import pandas as pd
import matplotlib.pyplot as plt
import os

# Define the file path
file_path = 'C:\\Users\\user\\Desktop\\Project T\\Streamflow data.xlsx'

# Load the data skipping the first five rows and setting the column names
data = pd.read_excel(file_path, skiprows=5, names=['Year', 'Month', 'Day', 'Q_kocairmak'])

# Convert Year, Month, Day to integers
data['Year'] = data['Year'].astype(int)
data['Month'] = data['Month'].astype(int)
data['Day'] = data['Day'].astype(int)

# Print the column names to verify
print(data.columns)

# Set the chunk size (number of data points per chunk)
chunk_size = 60  # Adjust this value as needed

# Create a directory to save the chunks and plots
output_dir = 'C:\\Users\\user\\Desktop\\Project T\\chunked_data'
os.makedirs(output_dir, exist_ok=True)

# Function to generate start and end dates for filenames
def get_date_range(chunk_data):
    start_date = f"{int(chunk_data.iloc[0]['Year'])}-{int(chunk_data.iloc[0]['Month']):02d}-{int(chunk_data.iloc[0]['Day']):02d}"
    end_date = f"{int(chunk_data.iloc[-1]['Year'])}-{int(chunk_data.iloc[-1]['Month']):02d}-{int(chunk_data.iloc[-1]['Day']):02d}"
    return start_date, end_date

# Save each chunk and plot
for i in range(0, len(data), chunk_size):
    chunk_data = data.iloc[i:i + chunk_size]
    if len(chunk_data) == 0:
        continue
    start_date, end_date = get_date_range(chunk_data)
    chunk_file = os.path.join(output_dir, f'chunk_{start_date}_to_{end_date}.xlsx')
    chunk_data.to_excel(chunk_file, index=False)
    
    # Plotting
    plt.figure()
    plt.plot(chunk_data.index, chunk_data['Q_kocairmak'])
    plt.title(f'Chunk {start_date} to {end_date}')
    plt.xlabel('Index')
    plt.ylabel('Streamflow')
    plt.grid(True)
    plot_file = os.path.join(output_dir, f'chunk_{start_date}_to_{end_date}.png')
    plt.savefig(plot_file)
    plt.close()

print(f'Saved chunks and their plots in {output_dir}')