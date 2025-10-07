import logging
import os

class LogGen:
    @staticmethod
    def loggen():
        """Generate a logger that writes to Logs/automation.log."""
        logs_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Logs'))
        os.makedirs(logs_dir, exist_ok=True)
        log_file = os.path.join(logs_dir, 'automation.log')

        logger = logging.getLogger("automation")
        logger.setLevel(logging.INFO)

        # Avoid adding multiple handlers if logger is called multiple times
        if not logger.handlers:
            file_handler = logging.FileHandler(log_file, mode='a')
            formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s', '%m/%d/%Y %I:%M:%S %p')
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

        return logger
