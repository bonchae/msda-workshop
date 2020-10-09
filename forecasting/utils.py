import numpy as np
import time
import matplotlib.pyplot as plt


class Clock:
    def __init__(self):
        self.start_time = 0

    def start(self):
        self.start_time = time.time()

    def stop(self):
        return round(time.time() - self.start_time, 5)


def disp(df, lines=5, type='head'):
    print(df.shape)
    if type == 'head':
        print(df.head(lines))
    elif type == 'tail':
        print(df.tail(lines))
    else:
        print("Error: Please enter either 'head' or 'tail'.")


def display_results(pred_df, pred_col):
    # Plot results
    plt.plot(pred_df['y'])
    plt.plot(pred_df[pred_col], 'r--', alpha=0.8)
    plt.legend(['Actual', 'Predicted'])
    plt.title('Ride Austin Forecast')
    plt.show()

    # Accuracy
    metrics_dict = {}
    metrics_dict['mape'] = mean_absolute_percentage_error(pred_df['y'], pred_df[pred_col])
    metrics_dict['rmse'] = root_mean_squared_error(pred_df['y'], pred_df[pred_col])
    metrics_dict['mae'] = mean_absolute_error(pred_df['y'], pred_df[pred_col])
    metrics_dict['mfe'] = mean_forecast_error(pred_df['y'], pred_df[pred_col])

    print(pred_col)
    print(metrics_dict)


def root_mean_squared_error(y_true, y_pred):
    result = np.sqrt(np.mean((y_true - y_pred) ** 2))
    return np.round(result, 3)


def mean_forecast_error(y_true, y_pred):
    result = np.mean(y_true - y_pred)
    return np.round(result, 20)


def mean_absolute_error(y_true, y_pred):
    result = np.mean(np.abs(y_true - y_pred))
    return np.round(result, 3)


def mean_absolute_percentage_error(y_true, y_pred, zero_method='adjust', adj=0.1):
    if zero_method == 'adjust':
        y_true_adj = y_true.copy()
        y_true_adj[y_true_adj == 0] = adj
        result = np.mean(np.abs((y_true_adj - y_pred) / y_true_adj)) * 100

    elif zero_method == 'error':
        if len(y_true[y_true == 0]) > 0:
            raise ValueError('Input y_true array contains a zero.')
        else:
            result = np.mean(np.abs((y_true - y_pred) / y_true)) * 100

    elif zero_method == 'ignore':
        y_true_ign = y_true.copy()
        y_true_ign = y_true_ign[y_true_ign != 0]
        result = np.mean(np.abs((y_true_ign - y_pred) / y_true_ign)) * 100

    else:
        raise ValueError("Invalid zero_method value - must be 'adjust', 'error', or 'ignore'.")

    return np.round(result, 3)
