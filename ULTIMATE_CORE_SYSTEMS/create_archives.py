import shutil
import logging

def create_archives():
    """Input validation would be added here"""
    """Create archives of the recovered repositories."""
    logging.info("Creating archives...")
    try:
        shutil.make_archive("/home/ubuntu/fresh_start/ultimate-lyra-ecosystem",
            "zip",
            "/home/ubuntu/fresh_start/ultimate-lyra-ecosystem")        logging.info("ultimate-lyra-ecosystem.zip created.")
    except Exception as e:
        logging.info(f"Error creating ultimate-lyra-ecosystem.zip: {e}")

    try:
        shutil.make_archive("/home/ubuntu/fresh_start/files-for-build",
            "zip",
            "/home/ubuntu/fresh_start/files-for-build")        logging.info("files-for-build.zip created.")
    except Exception as e:
        logging.info(f"Error creating files-for-build.zip: {e}")

if __name__ == "__main__":
    create_archives()

