import datetime

def write_log(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 'a' mode opens the file for appending, creating it if it doesn't exist
    with open("ai_pipeline.log", "a", encoding="utf-8") as log_file:
        log_file.write(f"[{timestamp}] {message}\n")
    print("Log entry added successfully.")

    def read_logs():
        print("\n Reading Log Entries ")
        try:
            with open("ai_pipeline.log", "r", encoding="utf-8") as log_file:
                print("\n--- Log Entries ---")
                for line in log_file:

                    # .strip() removes whitespace and newlines from the ends
                    print(line.strip())
        except FileNotFoundError:
            print("Log file not found. No entries to display.")

    if __name__ == "__main__":
        write_log("System initialized. Fetching model parameters...")
        write_log("Success: Connection established with data layer.")
        read_logs()

