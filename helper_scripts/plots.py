import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt  

def plot_bar(
    data: pd.DataFrame, 
    x_col: str, 
    y_col: str, 
    title: str, 
    xlabel: str = "", 
    ylabel: str = "", 
    palette: str = "dark:b_r", 
    figsize: tuple = (10,6)
) -> None:
    """
    Plot a bar chart using Seaborn.

    Args:
    - data: The dataframe to plot.
    - x_col: The column to plot on the x-axis.
    - y_col: The column to plot on the y-axis.
    - title: The title of the plot.
    - xlabel: The label for the x-axis.
    - ylabel: The label for the y-axis.
    - palette: The color palette to use.
    - figsize: The size of the figure.
    """
    plt.figure(figsize=figsize)
    sns.set_theme(style="ticks")
    ax = sns.barplot(data=data, x=x_col, y=y_col, hue=x_col, palette=palette, legend=False)
    sns.despine()
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

def plot_pie_charts(df: pd.DataFrame, column_mappings: dict) -> None:
    """
    Plot a pie chart for each column in the dataframe using Seaborn.

    Args:
    - df: The dataframe to plot.
    - column_mappings: A dictionary mapping column names to titles.

    Returns:
    - None
    """
    # Create the figure and axis
    fig, ax = plt.subplots(1, len(column_mappings), figsize=(10, 6))

    # Get the color palette
    colors = sns.color_palette()

    # Loop over the columns and plot a pie chart for each
    for i, (column, title) in enumerate(column_mappings.items()):
        # Plot the pie chart
        ax[i].pie(
            # Get the value counts of the column
            df[column].value_counts(),
            # Set the labels to "False" and "True"
            labels=["False", "True"],
            # Set the colors
            colors=colors,
            # Set the auto percentage
            autopct="%1.1f%%",
            # Set the start angle
            startangle=90,
        )
        # Set the title
        ax[i].set_title(title)

    # Show the plot
    plt.show()
