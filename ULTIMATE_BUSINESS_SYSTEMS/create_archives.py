import shutil

def create_archives():
    """Create archives of the recovered repositories."""
    print("Creating archives...")
    try:
        shutil.make_archive("/home/ubuntu/fresh_start/ultimate-lyra-ecosystem", "zip", "/home/ubuntu/fresh_start/ultimate-lyra-ecosystem")
        print("ultimate-lyra-ecosystem.zip created.")
    except Exception as e:
        print(f"Error creating ultimate-lyra-ecosystem.zip: {e}")

    try:
        shutil.make_archive("/home/ubuntu/fresh_start/files-for-build", "zip", "/home/ubuntu/fresh_start/files-for-build")
        print("files-for-build.zip created.")
    except Exception as e:
        print(f"Error creating files-for-build.zip: {e}")

if __name__ == "__main__":
    create_archives()

