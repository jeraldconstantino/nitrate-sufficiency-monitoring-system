<p align="center">
  <img src="https://github.com/jeraldconstantino/nitrate-sufficiency-monitoring-system/blob/main/icon/logo.svg" alt="banner" width="150" height="150">
</p>
<h1 align="center">Nitrate Sufficiency Monitoring System</h1>

The system is primarily designed for monitoring and classifying the nitrate sufficiency of an aquaponic system based on the morphological features of the lettuce. The software has been developed using the PyQt5 library and is integrated with a deep learning model that utilizes the [Ultralytic's YOLO algorithm](https://docs.ultralytics.com/modes/) to perform live video feed classification and segmentation tasks. It is deployed on a Raspberry Pi 4 Model B connected with a Raspberry Pi Camera v2 for real-world inferencing. 

## Features
- Incorporates a deep learning model for live feed classification and segmentation tasks.
- Users can capture images of the lettuce, whether the detection is enabled or not.
- Automates the operation frequency of the fish feeding device based on the model inference result.
- Displays inference results, such as classification labels and prediction scores, aiding users in nutrient management decision-making.
- Users can configure the fish feeding time schedule settings based on their desired schedule.

## How to run the software
Make sure that you have an updated version of the source code by following the instructions below.

> **NOTE:** Before running the software, make sure you have [Git](https://git-scm.com/) and [Python](https://www.python.org/downloads/) (including PIP) installed on your device.

1. Open your terminal or command prompt.

2. Navigate to the directory where you want to save the repository by using the `cd` command. For example:
   ```
   cd /path/to/your/desired/directory
   ```

3. Clone the repository by running the following command:
   ```
   git clone https://github.com/jeraldconstantino/nitrate-sufficiency-monitoring-system.git
   ```

4. Change to the cloned repository's directory:
   ```
   cd nitrate-sufficiency-monitoring-system
   ```

5. Create a virtual environment to isolate the software's dependencies:
   - **Windows**:
     ```
     python -m venv env
     ```
   - **macOS/Linux**:
     ```
     python3 -m venv env
     ```

6. Activate the virtual environment:
   - **Windows** (PowerShell):
     ```
     .\env\Scripts\Activate.ps1
     ```
   - **Windows** (Command Prompt):
     ```
     .\env\Scripts\activate.bat
     ```
   - **macOS/Linux**:
     ```
     source env/bin/activate
     ```

7. Install the required dependencies using PIP:
   ```
   pip install -r requirements.txt
   ```

8. Run the software:
   ```
   python main.py
   ```

By following these steps, you should be able to successfully run the software. If you encounter any issues, double-check that you have all the prerequisites installed and that you have followed each step correctly.

> **DISCLAIMER:** This project is part of our Undergraduate Thesis entitled, "Monitoring and Classification of Nitrate Sufficiency of an Aquaponic System Based on Lettuce Morphological Status using a Machine Vision Approach."
