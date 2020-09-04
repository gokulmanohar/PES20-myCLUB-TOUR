## PES myCLUB TOUR
Python code to formulate the myClub Tour event stats in PES mobile 2020.

![PES 2020 Poster](https://i.postimg.cc/508H46N4/pes-11253-1.jpg)

### Functionalities
* Provides you with the sum of total goals scored along a week.
* Can formulate multiple tour events in a single week.
* Finds the top goal scorer [golden boot winner] of every week.
* Can retain the details of all the previous week's tour stats and provide info in a comparable manner.
* Puts out a graph showing the total goals scored throughout the Fiscal year [Quarters].
* Pulls up the web-browser showing the details of the golden boot winner.

### Execution
1. Save the *.txt* file in the [format](https://github.com/gokulmanohar/PES-myCLUB-TOUR/tree/master/files) into `files` folder.
2. Execute `RUN.bat`.
3. Specify the name of the saved file.


### Usage
The `RUN.bat` is configured to locate the Python interpreter from *C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python38\python.exe*. If there is a change in the path, consider changing it. Also if any import error occurs please consider running,
```
pip install numpy
pip install matplotlib
```
Download the entire code base from this github directory and extract it to any desired location. **Do not remove or rename a file/folder**. Some files/folders may be empty but do not try to remove it.
You can download the directory without the `internal/Python` folder in it from [here](https://drive.google.com/file/d/1iIhW6aAUKF6N_R_hpbZBOYTl7qVmo702/view). [Only about 50KB in size] and change the python interpreter in the `RUN.bat` to one in your own PC. (But you may have to download the import modules)

### Screenshots
**UI**  
![PES 2020 Poster](https://i.postimg.cc/G3VyFw6n/pes-my-clubui.png)

**Graph**  
![Graph](https://i.postimg.cc/FsBtDGNS/2020-Q3.jpg)

### Changelog
**Major Update [02-09-2020]**  
Changes:
1. Different tour dict. files for different quarters of the year. 
2. All these files link to tour_complete dict. backup file.
3. Automatic save for the graph.
4. Introduction of script_helper.py.
5. Python now integrated into the directory itself.
6. Robust RUN.bat file.
7. Duplication of dict. now eliminated.
8. Comments added for better understanding.

### Future plans
1. Copy the golden boot winner name to clipboard.
2. Download the image directly from browser.
3. Image resizing with OPENCV.
4. Making a cataloge with every golden boot winners.
