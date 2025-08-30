# URL Health Checker

![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Built with](https://img.shields.io/badge/Built%20with-Tkinter-orange)

A sleek, modern, and user-friendly desktop application built with Python and custom Tkinter to check the status of any URL. It provides real-time feedback on whether a website is online, offline, or returning an error, all within a beautiful, non-blocking interface.

## ✨ Features

*   **Modern UI:** A clean, dark-themed interface designed for a great user experience.
*   **Responsive & Non-Blocking:** The application uses threading to perform network checks, so the UI never freezes, even if a URL is slow to respond.
*   **Real-time Feedback:** Get instant status updates, including success codes (2xx) and error codes (4xx, 5xx).
*   **User-Friendly Input:** Includes placeholder text and automatically handles URLs with or without `http://` or `https://`.
*   **Robust Error Handling:** Gracefully manages connection timeouts, invalid URLs, and other network-related issues.
*   **Cross-Platform:** Built with Tkinter, Python's standard GUI package, making it compatible with Windows, macOS, and Linux.

## 🛠️ Technology Stack

*   **Language:** Python
*   **GUI Framework:** Tkinter (`ttk` for modern styling)
*   **HTTP Library:** `requests`
*   **Concurrency:** `threading` and `queue` for a non-blocking UI.

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

You need to have Python 3.7 or newer installed on your system.
*   [Python 3](https://www.python.org/downloads/)

### Installation

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/azario0/url-health-checker.git
    ```
    *(Note: You might want to rename `url-health-checker` to whatever you name your repository)*

2.  **Navigate to the project directory:**
    ```sh
    cd url-health-checker
    ```

3.  **Install the required packages:**
    It's recommended to use a virtual environment.
    ```sh
    # Create and activate a virtual environment (optional but recommended)
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

    # Install dependencies
    pip install -r requirements.txt
    ```

### Usage

Run the application with the following command:
```sh
python url_checker.py
```
The application window will open. Enter a URL in the input field and click the "Check Status" button or press `Enter` to see the result.

## 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

## 📄 License

Distributed under the MIT License. See `LICENSE.md` for more information.

## 📧 Contact

azario0 - [https://github.com/azario0](https://github.com/azario0)

Project Link: [https://github.com/azario0/url-health-checker](https://github.com/azario0/url-health-checker)
