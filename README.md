<p align="center">
  <img src="https://github.com/jeraldconstantino/nitrate-sufficiency-monitoring-system/blob/main/icon/logo.svg" alt="banner" width="150" height="150">
</p>
<h1 align="center">Nitrate Sufficiency Monitoring System</h1>

The system is primarily designed for monitoring and classifying an aquaponic system's nitrate sufficiency based on the lettuce's morphological features. The software has been developed using the [PyQt5 library](https://pypi.org/project/PyQt5/). It is integrated with a deep learning model, utilizing [Ultralytic's YOLO algorithm](https://docs.ultralytics.com/modes/) to perform live video feed classification and segmentation tasks. The software was also deployed on a Raspberry Pi 4 Model B connected with a Raspberry Pi Camera v2 for real-world inferencing. 

## Features
- Incorporates a deep learning model for live feed classification and segmentation tasks.
- Users can capture images of the lettuce, whether the detection is enabled or not.
- Automates the operation frequency of the fish feeding device based on the model inference result.
- Displays inference results, such as classification labels and prediction scores, aiding users in nutrient management decision-making.
- Users can configure the fish-feeding schedule settings based on their desired time.

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

By following these steps, you should be able to run the software successfully. If you encounter any issues, double-check that all the prerequisites are installed and followed each step correctly. You may also adjust a specific dependencies version once the provided version in `requirements.txt` is deprecated.

## Deployment in Hardware System
The software is specifically designed for deployment on a Raspberry Pi 4 Model B with a seven-inch LCD monitor. The authors recommend that the computing device has a minimum of 8GB of RAM and a TPU accelerator connected. It is because performing live video classification and segmentation is highly intensive, requiring significant computational resources.

### Circuit Configuration of Fish Feeder and Raspberry Pi 4
The fish feeder has four wires with different colors: violet, blue, green, and yellow. The violet wire connects to the relay inside the feeder’s case, controlling the DC motor’s on/off function. The blue wire connects to the limit switch. The green wire supplies power (5V) to the relay and switch. The yellow wire is the ground connection.
> **NOTE:** The authors have modified a fish-feeding device purchased online to make it programmable with the Raspberry Pi 4 and other microcontrollers. 
1. Connect the violet color wire to the GPIO 20 (BCM pin numbering) of the digital pins on the Raspberry Pi 4.
2. Connect the blue color wire to the GPIO 21 (BCM pin numbering) of the digital pins on the Raspberry Pi 4.
3. Connect the green color wire to the 5V pin of the Raspberry Pi 4.
4. Connect the yellow color wire to the ground pin of the Raspberry Pi 4.
5. Insert the two AA batteries (R6S UM-3 1.5V) into the power supply of the fish feeder.

### Configure the Software for Automatic Start-up
1. Follow the instruction on how to run the software above.
2. Go to the ".config" folder and add a folder named "autostart".
3. Create a file in a ".desktop" extension name inside that folder.
4. Open the file. Copy and paste the following commands inside the ".desktop" file.
  ```
  [Desktop Entry]
  Encoding=UTF-8
  Type=Application
  Name=<Nitrate Sufficiency>
  Comment=
  Exec=sh -c "python3 path/main.py"
  StartupNotify=false
  Terminal=true
  Hidden=false
  ```
5. Configure the paths of all necessary files inside the main.py file. Kindly search for the following syntax and modify the paths according to your file system. Ensure that you have provided absolute paths for accurate file referencing
```
# Path declaration
mainWindowUI = "absolute path for main.ui"
feedingScheduleDialogUI = "absolute path for feedingScheduleDialog.ui"
directory = 'absolute path for the image folder'
model = YOLO("absolute path for model/best.pt")
windowLogoPath = "absolute path for for icon/logo.svg"
successIconPath = "absolute path for icon/success.svg"
loadingIndicatorPath = "absolute path for gif/loading_indicator.gif"
```
6. Reboot the Raspberry Pi 4 and wait for the software to launch automatically at start-up.
----------------------------
## NOTE:
<p align="justify">
This software is one of the components of the Undergraduate Thesis entitled "Monitoring and Classification of Nitrate Sufficiency of an Aquaponic System Based on Lettuce Morphological Status using a Machine Vision Approach." We want to express our heartfelt appreciation to the person behind the successful implementation of the project and to those who supported the entire development.
</p>
