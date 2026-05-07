import qrcode
import os

def generate_qr_code(data, filename="my_qr_code.png"):
    """
    Generates a QR code from the given data and saves it to a file.
    """
    try:
        # Create a QR code instance
        qr = qrcode.QRCode(
            version=1, # Controls the size of the QR Code, from 1 to 40
            error_correction=qrcode.constants.ERROR_CORRECT_H, # High error correction
            box_size=10, # Size of each box in pixels
            border=4, # Thickness of the border (minimum is 4)
        )

        # Add data to the QR code
        qr.add_data(data)
        qr.make(fit=True)

        # Create an image from the QR code instance
        # You can customize colors here
        img = qr.make_image(fill_color="black", back_color="white")

        # Get the directory of the current script to save it in the same folder
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, filename)

        # Save the image
        img.save(file_path)
        print(f"✅ Successfully generated QR code!")
        print(f"📁 Saved to: {file_path}")

    except Exception as e:
        print(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    print("--- QR Code Generator ---")
    
    # Get the value from the user
    value_to_encode = input("Enter the text, URL, or value you want to convert to a QR code: ")
    
    if value_to_encode.strip():
        # Optional: Ask for a custom filename
        output_filename = input("Enter the output filename (e.g., website_qr.png) [Press Enter for default]: ")
        
        if not output_filename.strip():
            output_filename = "my_qr_code.png"
            
        # Ensure it has a .png extension
        if not output_filename.lower().endswith(('.png', '.jpg', '.jpeg')):
             output_filename += ".png"
             
        generate_qr_code(value_to_encode, output_filename)
    else:
        print("Error: Value cannot be empty.")
