# AI in Quadrupeds

"AI In Quadrupeds" is a project that focuses on combining helpful, friendly AI with quadruped-based gait and manipulation policies. Quadrupeds, like any other robot, should be intelligent, empathetic, and determined to help out their humans whenver the can. The AI (spearheaded by heart.py) enables a popular open source Quadruped (Spot Micro) to make intelligent decisions (and of course, take action) based upon complex commands given to it by a user.

This project is largely inspired by UT Austin's B.U.M.B.L.E (Unifying Reasoning and Acting with Vision-Language Models for Building-wide Mobile Manipulation
, 2024) project, which focuses on combining AI-powered intelligent decision making with Mobile Arm Manipulator (more specifically, a Tiago Robot) movement policies. While a Tiago Robot is the cutting edge for mobile arm manipulators, the likelihood of the average college student or american household affording one is pretty low, making . I decided to create a "BUMBLE-knockoff" version specifically for Quadruped Gait and Manipulation... in the form of an easily accessible, cheap to make, (and personally very adorable) Spot Micro. Now, everyone can have a helpful robot dog that they can 3D print right at their homes (or in my case, the NYU Tandon School of Engineering's Makerspace) with parts they can order off of Amazon for less than $100. 


# Acknowledgements

This project was created for the Gait and Manipulation (Spring 2025) class, as part of the Masters of Science in Mechatronics & Robotics at New York University. The project was met with various levels of success, and with the encouragement of the Professor, we have decided to upload the project to Open Source so that others can enjoy.

![alt text](<Code Flow Diagram.png>)

# How to get Started

Please take a look at requirements.txt for environmental requirements.

Once all libraries are installed, feel free to launch every "sense" for a demonstration of the code...

**voice.py** - The Voice of Spot Micro. Launching will give you a demonstration of their voice. Feel free to set the gender within the file, by running set_voice(g) under main, where g = 'f' for a feminine voice, or g = 'm' for a masculine voice. 

**eyes.py** - The Eyes of Spot Micro. Please connect a USB web-cam (or any camera for the matter), then run read_cameras() under main. This will give you a list of camera IDs. Choose the ID of the camera you want to take vision from, and write it under the global variable CAMERA_PORT. Launching the file will make the camera you specified take your selfie!

**ears.py** - The Ears of Spot Micro, powered by IBM's TTS and OpenAI's Whisper. This module can work offline, so no need to worry about wifi connectivity for now. When you run the file, speak into your microphone for 10 seconds. Your words should print back to you.

**brain.py** - The Intelligence of Spot Micro... powered by Google's Gemini-flash-2.0. You would need an API key- write it under the global variable GEMINI_KEY. You only need the free version for the program to work. Launching the file will load in "soda_on_ground.jpg" (aka, a crumpled coca-cola can on the ground POV of the robot) into the VLM, and demo their response given a scenario (Their owner really wants coca-cola right about now!). The scenario can be changed, if you'd like: just rewrite "command" under main.

**heart.py** - The Heart of Spot Micro, aka, the driving force of the project. This is your "Main.py" file. Running this will launch the program...

# What to expect when launching Heart.py

Launching heart will turn on Spot's ears: It will be listening, but dormant until you say the keywords "Hey Spot!". Spot will wake up, ready to take in any commands. Feel free to talk to it- Do you want Spot to fetch you a soda? Did you lose something and need help finding it? Spot will take in the world around it, and throw up flags that showcase what it's going to do: Go Forward [x] amount of inches, Turn Right/Left [x] amount of degrees, Sit Down, Lie Down, Stand Up, and Speak it's thoughts out loud back to you. View the command prompt to see these flags go up, and make sure to turn on your volume to hear what Spot has to say.

Tricks that I've found helpful when interacting with spot...
1) Be in a silent or quiet room. I learned Spot cannot hear me well when Im in a busy makerspace, hallway, or coffee shop.
2) If you want spot to be more vocal, tell it to "talk me through your process!" It will then verbally communicate the flags it threw up (not just print them on the terminal).
3) If it cannot see or detect something, check your camera or the lighting around your room. You can see the last thing Spot has seen under "short_term_memory.png." 

# References

BUMBLE Credits...
@article{shah2024bumble,
   title={BUMBLE: Unifying Reasoning and Acting with Vision-Language Models for Building-wide Mobile Manipulation},
   author={Shah, Rutav and Yu, Albert and Zhu, Yifeng and Zhu, Yuke and Mart{\'\i}n-Mart{\'\i}n, Roberto},
   booktitle={2025 IEEE International Conference on Robotics and Automation (ICRA)},
   year={2025},
   organization={IEEE}
}

SPOTMicro Credits...
https://spotmicroai.readthedocs.io/en/latest/

# A work in Progress

1) The Triangulation is alright, but not perfect - future works include incorporation Ultrasonic Sensors (or even a LIDAR I hope!!) to make more accurate perceptive assumptions.
2) Of course, the flags are useful, but we need to work on the controls/movement aspect of Spot Micro. Despite Spot not moving right now, it’s only a matter of connecting the flags to hard-coded movement policies for the project to be complete. AKA, the final step of the project (and the most crucial), get it to walk, sit, turn, stand up, etc. on command… then let the AI take the reigns!
3) Make ears.py more sensitive in louder, more "audibly messy" environments. It should still take in commands in public places. Maybe work on non-verbal ways to command spot?

Any bugs, or suggestions, on improving this project will be welcomed.



 
