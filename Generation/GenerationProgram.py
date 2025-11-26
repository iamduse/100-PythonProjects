#TODO: Write welcome and ask the year they are born
red = "\033[91mThis is red text\033[0m"
green = "\033[92mThis is green text\033[0m"
blue = "\033[94mThis is blue text\033[0m"

print("\033[94mWELCOME TO GENERATION TELLER \033[0m")
year = int(input("Enter the year you born or the year you want to know: "))
#Create a dictionary to store the generation information
generations = {
    "Greatest Generation": {
        "start": 1901,
        "end": 1927,
        "description": "Named for enduring the Great Depression and fighting in WWII; "
                       "often seen as heroic and disciplined."
    },
    "Silent Generation": {
        "start": 1928,
        "end": 1945,
        "description": "Called 'silent' because they grew up during wartime and hardship,"
                       " known for conformity and traditional values."
    },
    "Baby Boomers": {
        "start": 1946,
        "end": 1964,
        "description": "Named for the large post-WWII 'baby boom' in birth rates."
    },
    "Generation X": {
        "start": 1965,
        "end": 1980,
        "description": "Named to represent a generation seen as independent and undefined ('X')."
                       " Popularized by Douglas Coupland’s novel."
    },
    "Millennials": {
        "start": 1981,
        "end": 1996,
        "description": "Named because they came of age around the new millennium;"
                       "also known for rapid tech adoption."
    },
    "Generation Z": {
        "start": 1997,
        "end": 2012,
        "description": "Named simply as the next letter after Gen X/Y; "
                       "known as the first fully digital-native generation."
    },
    "Generation Alpha": {
        "start": 2013,
        "end": 2025,
        "description": "Named for starting a new 'alphabet' of generations;"
                       " born into highly advanced digital and AI environments."
    },
    # "Generation Beta": {
    #     "start": 2025,
    #     "end": 2039,
    #     "description": "Projected name continuing the Greek alphabet; "
    #                    "expected to grow up in an even more automated and AI-driven world."
    # }
}

#Fetch the year , name and description in to the dictionary after receiving the year and doing some if statements
def get_generation(year):
    for gen, info in generations.items():
        if info["start"] <= year <= info["end"]:
            return gen, info["description"]
    return "Unknown Generation", "No description available."

# print the result after the function do the job
gen, desc = get_generation(year)
print("\n")
print("\033[92mGeneration:", gen, "\033[0m")
print("\033[94mDescription:", desc, "\033[0m")




