# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

# Least Squares Moving Average


def calculate_lsma(df, period=21):
    lsma_values = []

    for i in range(period, len(df)):
        # Extract the most recent N df points
        subset = df.iloc[i - period:i]

        # Perform linear regression to fit a line
        x = np.arange(len(subset))
        y = subset['close'].values
        slope, intercept = np.polyfit(x, y, 1)

        # Calculate the LSMA value using the linear equation
        lsma = intercept + slope * (period - 1)
        lsma_values.append(lsma)

    lsma_series = pd.Series(lsma_values, index=df.index[period:])

    return lsma_series


# Determine the direction of the trend
def trend_detection(df, column):
    """
    Add a 'trend' column to a DataFrame based on the line trend.

    Parameters:
    df (pd.DataFrame): The DataFrame containing the 'date' and the existing column to check.
    column (str): The name of the existing column containing the values to check.

    Returns:
    pd.DataFrame: The input DataFrame with an additional 'trend' column.
    """
    if df.empty or column not in df.columns:
        return df  # Return the original DataFrame if it's empty or the SMA column does not exist

    # Initialize the 'trend' column with 'Steady'
    df['trend'] = 'Indecisive'

    # Find where SMA is rising or falling and update the 'trend' column accordingly
    rising_mask = df[column] > df[column].shift(1)
    falling_mask = df[column] < df[column].shift(1)

    df.loc[rising_mask, 'trend'] = 'Rising'
    df.loc[falling_mask, 'trend'] = 'Falling'

    return df

# Example usage:
# Assuming you have a DataFrame 'df' with an existing 'sma' column:
# df_with_trend = trend_detection(df, 'sma')
# print(df_with_trend)
