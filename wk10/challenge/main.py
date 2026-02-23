from csv_log_source import CsvLogSource, MainWindow
def main():
    csv_source = CsvLogSource("data.csv")
    app = MainWindow(csv_source)
    app.display_logs()

if __name__ == "__main__":
    main()