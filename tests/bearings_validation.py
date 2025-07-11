import sys
import logging
from pathlib import Path

logging.basicConfig()
logging.getLogger().setLevel(logging.WARNING)

try:
    # Import the library installed using pip
    from python_vor import get_bearing
    import importlib.metadata

    print(f"Calling test using installed library, version: {importlib.metadata.version("python_vor")}")
except ImportError:
    # Use this block if working with source code
    sys.path.append(str(Path(__file__).parent.parent))
    from src.python_vor import get_bearing

    print("Calling test using local library files")


def main():
    """
    Main function to test the get_bearing function with WAV files in the audio folder.
    """

    wavs_folder = "audio/"
    offset = 223  # Adjust this as needed for your test case
    errors = 0

    # For each WAV file in the folder, calculate the bearing
    for wav_file in Path(wavs_folder).glob("*.wav"):
        print(f"Processing {wav_file.name}...")
        try:
            # Calculate the bearing using the get_bearing function
            bearing = get_bearing(str(wav_file), offset=offset)
            print(f"Bearing for {wav_file.name}: {bearing:.2f}°")
            # Get the bearing from the file name
            expected_bearing = float(wav_file.stem.split("-")[-1].replace("Deg", ""))
            print(f"Expected bearing for {wav_file.name}: {expected_bearing:.2f}°")
            # Check if the calculated bearing matches the expected bearing
            if abs(bearing - expected_bearing) < 2:  # Allow a small tolerance
                print(f"Test passed for {wav_file.name}.")
            else:
                print(f"Test failed for {wav_file.name}. Expected {expected_bearing:.2f}°, got {bearing:.2f}°")
                errors += 1
        except Exception as e:
            print(f"Error processing {wav_file.name}: {e}")
            errors += 1

    if errors > 0:
        raise RuntimeError(f"Test completed with {errors} errors.")
    else:
        print("All tests passed successfully.")


if __name__ == "__main__":
    main()
