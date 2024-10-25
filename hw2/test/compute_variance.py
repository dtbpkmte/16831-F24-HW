import pandas as pd

csv_files = ["l0.csv", "l095.csv", "l099.csv", "l1.csv"]


if __name__ == "__main__":
    for file in csv_files:
        df = pd.read_csv(file)
        variance = df["Value"].var()
        print(f"Variance of 'Value' in {file}: {variance}")
