# Redirect App

**Redirect App** is a Flask application designed to redirect incoming requests based on environment variables prefixed with `TARGET_`.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/modulairy/redirect-app.git
   cd redirect-app
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate
   ```

3. Install the required packages:
   ```
   pip install flask
   ```

## Configuration

Configure the redirection targets using environment variables prefixed with `TARGET_`. Multiple targets can be specified by separating them with a semicolon (`;`). For example:

```
export TARGET_SITE1.COM="example.com;www.example.com"
export TARGET_SITE2.COM="sub.example.com;subdomain.example.com"
```

## Usage

1. Run the Flask application:
   ```
   python app.py
   ```

2. Incoming requests will be redirected based on the configured targets.

## Example

If an incoming request has a host of `example.com`, it will be redirected to `site1.com`.

## Contributing

If you want to contribute to this project, please follow these steps:

1. Fork the repository on GitHub.
2. Create a new branch with your changes.
3. Make your changes and commit them with descriptive messages.
4. Push your changes to your fork.
5. Submit a pull request to this repository.

## Issues

If you encounter any issues or have questions, please [open an issue](https://github.com/modulairy/redirect-app/issues) on GitHub.

## License

This project is licensed under the [Apache 2.0 License](../LICENSE).