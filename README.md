# biointernship
# A collection of the workflows and projects completed during my 2020 BioTrain Internship in Dr. Alex Harkess' Lab.
# Any scripts ending in .py can be run over a directory of images.
# A renaming script is available that will name all output images after their input image.
# 1. Initialize docker using terminal window (see initializedocker). 
# 2. Open Jupyter notebook and start one Terminal tab and one Python 3 tab.
# 3. In the Python 3 tab, run OpenCV code to extract the individual frames from timelapse video (see vidtoframes).
# 4. Run any PlantCV workflow over image set while simultaneously creating a unique output file for each image (see initializedocker).
# 5. Run bash script to rename all output images after their unique frame (see rename-script.sh).
# 6. Use desktop terminal window (instead of the Jupyter notebook terminal tab) to copy your specific output images to a new directory (see intializedocker).
# 7. Sort images sequentially in directory (see initializedocker).
# 8. Copy and paste this sequential list into a .txt file, save in the directory you're in. 
# 9. Using the dependency imagemagick in the desktop terminal window, run $ convert @step8.txt anyname.gif
