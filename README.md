# Virtual-Python-Cube
CS102 project, a rubiks cube based puzzle game

CS102 PCPS-O8 project notes

Virtual rubik's cube (single window program w/ cube interface on left and buttons on right)

	1 Mandatory sub-sections

		1 Start with a solved cube
		2 Have 18 arrows to control cube movements
		3 Shuffle (button) will shuffle the cube using random function
		4 Exit (button) button quits the program

	2 Optional (but recommended) sub-sections (in order of priority) (recommend batch file for setup)

		1 Solve (button) will solve the cube with successive motions
		2 Save (button) makes the program record the current state of the cube, generates a list and creates a QR code containing that list, which must be saved by the player
		3 Resume (button) should accept the list from the QR code and produce the same cube (Inherently linked with save feature)
		4 OpenCV detects (Button) an actual cube and converts it to virtual form

Links 
	
	General code sharing - https://codeshare.io/
	1.1, 1.2 & 1.4 (core source code) - https://code-projects.org/rubiks-cube-in-python-with-source-code/
	2.1 (library for cube solving) - https://pypi.org/project/rubik-solver/
	2.1 (reference - cubing shorthand) - https://ruwix.com/the-rubiks-cube/notation/ 
	2.1 (delay command) - https://realpython.com/python-sleep/
	2.2 & 2.3 (QR code library) - https://pypi.org/project/qrcode/
	2.2 & 2.3 (image processing library (Pillow)) - https://pypi.org/project/Pillow/
	2.2 & 2.3 (show image command from pillow) - https://www.geeksforgeeks.org/python-pil-image-show-method/
	2.4 (OpenCV installation) - https://pypi.org/project/opencv-python/
	
