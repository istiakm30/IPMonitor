# IP Change Monitor

This project is a Python application that monitors for changes to the public IP address. It checks the IP address at regular intervals and logs any changes or issues with the network connection.

## Features

- Monitors the public IP address
- Logs changes to the IP address
- Logs duration of IP usage
- Logs any issues with the network connection
- Visualizes IP usage durations

## Files

- `config.py`: Contains the configuration parameters for the script.
- `ip_checker.py`: Contains functions to get the current public IP address and check if it has- `logger.py`: Sets up logging for the application.
- `ip_usage_visualization.py`: Parses log data and visualizes IP usage durations in a bar chart.
- `main.py`: The main script that runs the monitoring loop.

## Usage

1. Clone the repository
2. Install the required Python packages: `requests` and `matplotlib` (for visualization).
3. Run `main.py` to initiate the IP address monitoring.
4. You can run `visualize.py` to see a visualization of IP usage durations.
--
## Configuration

You can configure the following parameters in `config.py`:

- `CHECK_INTERVAL`: Time interval in seconds between each check of the internet connection.
- `CHECK`: URL used to check if there is an active internet connection.
- `IP_CHECK_URL`: URL used to check the public IP address.
- `LOG`: Filename to log the connection and IP checks.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
