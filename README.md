# 🌟 Prometheus Stress Tester 🌟

This repository contains a stress testing tool for Prometheus. It allows you to stress test your Prometheus setup by generating high loads and monitoring its performance.

## 🛠️ Technologies Used

- **[Prometheus](https://prometheus.io/):** An open-source systems monitoring and alerting toolkit.
- **[Alertmanager](https://prometheus.io/docs/alerting/alertmanager/):** Handles alerts sent by Prometheus server.
- **[Node Exporter](https://prometheus.io/docs/guides/node-exporter/):** Exports system and hardware metrics.
- **[Git](https://git-scm.com/):** Version control system for tracking changes in source code.
- **[Python 3](https://www.python.org/):** Programming language used for scripting.
- **JSON:** Data interchange format used for configuration files.
- **[hping3](https://tools.kali.org/information-gathering/hping3):** A command-line oriented TCP/IP packet assembler/analyzer.
- **[epel-release](https://fedoraproject.org/wiki/EPEL):** Extra Packages for Enterprise Linux (EPEL) repository release package.

## 🚀 Getting Started

Follow these instructions to get a copy of the project and run it on your local machine.

### Prerequisites

- Python 3.x
- Git

### Download Stress Tester

You can download the Stress Tester tar file from [this link](https://drive.google.com/file/d/1c90ButdQkiN1aPafKpOn-LQ5IClh8OFY/view?usp=drive_link).

**Note**: Cloning this repository directly will not work due to GitHub's file size constraint. The Prometheus folder, a major part of the project, is not included due to its size. Please download the Stress Tester tar file from the provided link.
### Extract the Tar File

Once downloaded, extract the tar file to your desired location.

Example command:
```bash
tar xzvf StressTester1.1.tar.gz
```

### Setup

Run `setup.py` to set up the Prometheus stress testing environment:

```bash
python3 setup.py
```

### Running the Application

After the setup is complete, you can run the application using the following command:

```bash
python3 app.py
```

**Note:** You can set the IP address of your Node Exporter in the `app.py` file. Currently, the option to specify the IP address of the machine running the script is available because stress testing must be performed on the same machine.

## ⚠️ Warning

This stress testing tool performs actions that may damage your computer or your Prometheus setup. Use it with caution.

## 🙌 Contributing

If you'd like to contribute to this project, please fork the repository and submit a pull request. You can also open an issue to report bugs or suggest improvements.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎉 Acknowledgments

- This project is inspired by the need for stress testing Prometheus setups in real-world scenarios. Take inspiration from this.
