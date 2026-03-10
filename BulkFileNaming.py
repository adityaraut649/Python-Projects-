import os


def main():
    # Use the exact path where the images are
    folder = r'C:\Users\HP\Desktop\unusual'

    # List all files in that folder
    for count, filename in enumerate(os.listdir(folder)):
        # Only process actual .jpg files
        if filename.lower().endswith(".jpg"):
            # Construct the full old path
            source = os.path.join(folder, filename)

            # Construct the new name (e.g., image0.jpg, image1.jpg)
            new_name = f"image{count}.jpg"
            destination = os.path.join(folder, new_name)

            # Rename
            os.rename(source, destination)
            print(f"Renamed {filename} to {new_name}")


if __name__ == "__main__":
    main()