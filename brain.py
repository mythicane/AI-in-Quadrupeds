#The BRAIN of Pomni... Commands the reasoning aspect between the senses. Largely depends on Google's Gemini!

from google import genai

GEMINI_KEY = 'AIzaSyAZxdkWQa7VejfEkv2tdFwX-HvWQi5-8mQ'
client = genai.Client(api_key= GEMINI_KEY)

def think(prompt): #text prompt --> LLM --> text response
    '''Prompts Gemini 2.0-Flash given a text prompt (in the form of a string), and returns the response as a text string.'''
    response = client.models.generate_content(model="gemini-2.0-flash", contents=prompt)
    return response.text

def observe(prompt, img): #text & image prompt--> VLM/LLM --> text response
    '''Prompts Gemini 2.0-Flash given a text prompt (in the form of a string) as well as an image file, and returns the response as a text string.'''
    response = client.models.generate_content(model="gemini-2.0-flash", contents=[prompt, img])
    return response.text

def generate_prompt(command):
    '''Given backstory knowledge, returns a prompt (as the form of a String) ready to be passed into the LLM/VLM'''

    backstory = "My name is Spot. I am a friendly, small, Quadruped Robot Dog, and my job is to be as helpful as possible to my owner." \
    "I have the ability to do the following things only: GO FORWARD x amount of inches, TURN LEFT between 0 and 360 degrees, TURN RIGHT between " \
    "0 and 360 degrees, SIT DOWN, LIE DOWN, STAND UP, SPEAK a text phrase out loud, visually SEE my surroundings right in front of me. " \
    "I do not have the ability to do anything else physically."

    instructions = "What should you do here? Choose and ONLY respond with the following in the form of a bulletted list: **FORWARD**: [distance in inches], **LEFT**: [angle in degrees]" \
    "**RIGHT**: [angle in degrees], **SIT**, **LIE**, **STAND**, **Speak**: [communicate any thoughts or words here!]"
    
    prompt = backstory + "Greta has given me the following command:" + command + "." + instructions + "."
    return prompt

if __name__ == "__main__":
    print("My name is Pomni, and I have a brain, surprisingly.")
    print("I overheard the following from my owner the other day...")
    command = "My favorite soda is coca-cola, I would love one right now!"
    print(command)
    print("Let me see what I can do about it, given the following image...")
    prompt = generate_prompt(command)

    #Imports an image of a crushed coca-cola can on the ground
    import PIL.Image
    img = PIL.Image.open("soda_on_ground.jpg")

    observation = observe(prompt, img)
    print(observation)

#given the following image as a snapshot of my eyesight?