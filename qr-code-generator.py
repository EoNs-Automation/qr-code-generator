import qrcode
import os
import re

def clean_filename(text):
    # Remove characters that are not allowed in filenames
    text = re.sub(r'[\\/*?:"<>|]', "", text)
    text = text.replace("https://", "").replace("http://", "").replace("www.", "")
    text = text.replace("/", "-").replace(".", "-")
    return text[:50]  # limit length


def generate_qr():
    print("=== QR Code Generator ===")
    print("Type 'quit' to exit.\n")

    # Get the folder where this script is located
    script_folder = os.path.dirname(os.path.abspath(__file__))

    # Create a "qrcodes" folder if it doesn't exist
    output_folder = os.path.join(script_folder, "qrcodes")
    os.makedirs(output_folder, exist_ok=True)

    while True:
        data = input("Enter text or URL to encode: ").strip()

        if data.lower() == "quit":
            print("Goodbye!")
            break

        if not data:
            print("Please enter something.\n")
            continue

        # Create QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        # Create a clean filename based on the input
        name = clean_filename(data)
        filename = f"{name}-qrcode.png"
        filepath = os.path.join(output_folder, filename)

        img.save(filepath)

        print(f"\nQR Code saved as '{filename}'")
        print(f"Location: {filepath}\n")


if __name__ == "__main__":
    generate_qr()