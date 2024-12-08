import matplotlib.pyplot as plt
import seaborn as sns

def create_time_series_plot(data, column, title):
    """Generate a time-series plot for a specific column."""
    plt.figure(figsize=(10, 5))
    plt.plot(pd.to_datetime(data['Timestamp']), data[column], label=title)
    plt.xlabel("Timestamp")
    plt.ylabel(title)
    plt.legend()
    return plt.gcf()

def create_correlation_heatmap(data):
    """Generate a correlation heatmap."""
    plt.figure(figsize=(8, 6))
    sns.heatmap(data.corr(), annot=True, cmap="coolwarm", fmt=".2f")
    return plt.gcf()
