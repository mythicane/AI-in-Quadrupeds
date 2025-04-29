#The HEART of Pomni... aka, the Main File that drives everything intelligent!
'''
1 file: listens in, and truncates an instruction
2 file: LLM interface that takes the innquiry, compiles it with other shit, gets a response, returns response
3 file: robot controller server that accepts trajetory instructions and sends it directly to the arduino '''

import brain #Cognitive Processing / LLM/VLMs
import ears #audio processing
import voice #vocal communications
import eyes #visual communications / Computer Vision

import PIL.Image #for image processing 

def process_prompt(prompt):
    '''Processes Prompt generation to execute accordingly!'''
    lines = prompt.splitlines()

    for line in lines:
        line = line.strip()
        if line.startswith("*") and "**" in line:
            try:
                first_star = line.index("**") + 2
                second_star = line.index("**", first_star)
                command = line[first_star:second_star].strip().lower()

                #A WORK IN PROGRESS!!
                colon_index = line.index(":", second_star)
                argument = line[colon_index + 1:].strip()

                if command == "speak":
                    voice.speak(argument)
                    
                elif command == "forward":
                    print(f"Moving forward {argument} inches.")

                elif command == "left":
                    print(f"Moving left {argument} degrees.")

                elif command == "right":
                    print(f"Moving right {argument} degrees.")

                elif command == "sit":
                    print("Spot has decided to Sit Down.")

                elif command == "lie":
                    print("Spot has decided to lie down.")

                elif command == "stand":
                    print("Spot has decided to stand up.")
                
                else:
                    print(f"Unknown command '{command}' with argument: {argument}")

            except ValueError:
                #if the line doesn't have proper format, just ignore it
                continue

#takes in an instruction
if __name__ == "__main__":
    while(True):
        text = ears.listen(False, 3)
        print(text)
        if "hey spot" in text.lower():
            voice.speak("Hey, how can I help you?") #Recognizes that my owner is calling me...
        
            #Listens for the Command
            text = ears.listen(False, 10)

            print("You said the following:", text)

            #Processes Command, looks infront of them, and Thinks about it...
            prompt = brain.generate_prompt(text)
            eyes.memorize(eyes.blink())
            img = PIL.Image.open("short_term_memory.png")
            response = brain.observe(prompt, img)

            #Prints deliberations, then parses it for commands...
            print(response)
            process_prompt(response)            

        if "that will be all spot" in text.lower():
            voice.speak("No worries. Say hey spot if you need me again!")
            break
        else:
            continue