# The Mad Mage's Fortress

Welcome to "The Mad Mage's Fortress" RPG game! Follow the instructions below to ensure a smooth setup on both macOS and Windows platforms.

## Installation Instructions

### Prerequisites
- Python 3.x
- pip (Python package installer)

### Step-by-Step Guide

1. **Ensure Python is installed:**
   - [Download Python](https://www.python.org/downloads/) and follow the installation instructions for your operating system.

2. **Check if Pillow is installed:**
   - Pillow is a Python Imaging Library (PIL) fork that adds image processing capabilities to your application.

3. **Install Pillow:**
   - Open your terminal (macOS) or command prompt (Windows) and run the following command:
     ```bash
     pip install pillow
     ```
   - If Pillow is not already installed, the game will prompt you to install it. Follow the on-screen instructions.

### Running the Game

1. **Download the game files:**
   - Ensure all the game files are saved in the correct directory. For example:
     - `The_Mad_Mage.py`
     - `warrior.jpg`
     - `mage.jpg`
     - `ranger.jpg`
     - `fortress.jpg`

2. **Update Image Paths:**
   - Ensure the image paths in the script are correctly pointing to the locations of your images. Example paths:
     ```python
     characters = {
         "Warrior": r"path/to/warrior.jpg",
         "Mage": r"path/to/mage.jpg",
         "Ranger": r"path/to/ranger.jpg"
     }
     image_path = r"path/to/fortress.jpg"
     ```

3. **Run the Game:**
   - Open your terminal (macOS) or command prompt (Windows), navigate to the directory containing the game files, and run the following command:
     ```bash
     python The_Mad_Mage.py
     ```

### Troubleshooting

1. **Pillow Not Installed:**
   - If you see an error message saying Pillow is not installed, run the following command to install it:
     ```bash
     pip install pillow
     ```

2. **Permission Errors:**
   - If you encounter a permission error while accessing image files, ensure the file paths are correct and you have the necessary permissions to access them.

3. **Common Errors:**
   - **ModuleNotFoundError**: Ensure you have installed all required libraries using pip.
   - **FileNotFoundError**: Verify that the paths to your image files are correct.

### Additional Information

For more detailed instructions or additional support, please refer to the official documentation of Python and Pillow.

Happy adventuring, brave hero!
