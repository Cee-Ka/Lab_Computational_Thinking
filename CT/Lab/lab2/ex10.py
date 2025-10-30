class Logger:
    def log(self, message):
        print(f"[log]: {message}")


class FileWriter:
    def __init__(self, filename):
        self.filename = filename

    def write(self, text):
        with open(self.filename, "a") as f:
            f.write(text + "\n")


class LogFileWriter(Logger, FileWriter):
    def __init__(self, filename):
        FileWriter.__init__(self, filename)

    def log(self, message):
        self.write(f"[log]: {message}")
        print(f"log written: {self.filename}")
        

log_writer = LogFileWriter("log.txt")

log_writer.log("Start")
log_writer.log("Processing...")
log_writer.log("Finish!")

