import matplotlib.pyplot as plt

def plot_data(df):
    fig, ax = plt.subplots()
    ax.plot(df['time'], df['temperature'], label='Temperature')
    ax.plot(df['time'], df['pressure'], label='Pressure')
    ax.set_xlabel('Time')
    ax.set_ylabel('Value')
    ax.set_title('Machine Data Plot')
    ax.legend()
    return fig