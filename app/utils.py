import pandas as pd
import matplotlib.pyplot as plt

def load_data(countries):
    file_map = {
        "Benin": "benin_clean.csv",
        "Sierra Leone": "sierraleone_clean.csv",  
        "Togo": "togo_clean.csv",
    }

    dfs = []
    for country in countries:
        path = f"data/{file_map[country]}"
        df = pd.read_csv(path)
        df["Country"] = country
        dfs.append(df)
    return pd.concat(dfs, ignore_index=True)

def plot_boxplot(df, metric, countries):
    plt.figure(figsize=(8, 5))
    data = [df[df["Country"] == c][metric].dropna() for c in countries]
    plt.boxplot(data, labels=countries)
    plt.title(f"{metric} Comparison")
    plt.ylabel(metric)
    plt.grid(True)
    return plt
