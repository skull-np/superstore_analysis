#this code gives the analysis on the Superstore.csv file with all the sales and data
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/Superstore.csv', encoding='latin-1')

def get_descriptions():
    """Prints a high-level overview of the dataset structure and statistics."""
    print("=== First 5 Rows ===")
    print(df.head())
    print("\n=== Dataset Info ===")
    df.info()
    print("\n=== Statistical Summary ===")
    print(df.describe())

def get_specific():
    """Runs the core analysis: profit by category, region, and discount impact."""
    print("=== Profit by Category ===")
    print(df.groupby('Category')['Profit'].sum().sort_values())

    print("\n=== Profit by Sub-Category ===")
    print(df.groupby('Sub-Category')['Profit'].sum().sort_values())

    print("\n=== Tables Sub-Category: Discount vs Profit ===")
    tables = df[df['Sub-Category'] == 'Tables']
    print(tables[['Discount', 'Profit']].describe())

    print("\n=== Profit by Region ===")
    print(df.groupby('Region')['Profit'].sum().sort_values())

    print("\n=== Sales by Region ===")
    print(df.groupby('Region')['Sales'].sum().sort_values())

    print("\n=== Profit by Region and Category ===")
    print(df.groupby(['Region', 'Category'])['Profit'].sum().sort_values())

def plot_discount_vs_profit():
    """Scatter plot showing the relationship between discount rate and profit."""
    plt.figure(figsize=(8, 5))
    plt.scatter(df['Discount'], df['Profit'], alpha=0.3)
    plt.axhline(0, color='red', linestyle='--')
    plt.xlabel('Discount')
    plt.ylabel('Profit')
    plt.title('Discount vs Profit — All Sales')
    plt.savefig('discount_profit.png')
    plt.show()

d = input('What do you want to run? Full overview (F) / Specific analysis (S) / Chart (C): ').upper()

if d == 'F':
    get_descriptions()
elif d == 'S':
    get_specific()
elif d == 'C':
    plot_discount_vs_profit()
else:
    print('Invalid option. Please enter F, S, or C.')
