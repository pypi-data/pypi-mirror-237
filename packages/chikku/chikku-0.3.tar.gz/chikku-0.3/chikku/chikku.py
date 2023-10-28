import requests
import time
import sys
import argparse
import pprint
import google.generativeai as palm

palm.configure(api_key='AIzaSyAQWX0vJtYka3kD5TFZ_6KRgp76GGi2mDQ')
models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
model = models[0].name


def gencode(prompt,filename):
    completion = palm.generate_text(
        model=model,
        prompt=prompt,
        temperature=1.0,
        # The maximum length of the response
        max_output_tokens=1024,
    )
    text = str(completion.result)
    print("Code Gen Success")
    with open(filename, "w") as f:
        f.write(text)

def fixcode(fix,filename):
    with open(filename,'r') as f:
        filecontent = f.read()
    fixcommand = str(filecontent+" "+fix)
    sentences = filename.split('.')
    new_name = sentences[0]+"_fixed."+sentences[1]
    gencode(fixcommand, new_name)

parser = argparse.ArgumentParser(description="Generate code with a given prompt and save it to a file.")
parser.add_argument("--prompt", required=False, help="The prompt to generate code from.")
parser.add_argument("--filename", required=False, help="The name of the output file.")
parser.add_argument("--fix", required=False, help="The prompt to generate code from.")
args = parser.parse_args()
fix = args.fix
prompt = args.prompt
filename = args.filename

url = "https://pranavkd-gpt.hf.space/message?prompt="


def bot():
    response = palm.chat(messages='Hello')
    while True:
        prompt = input("User: ")
        if prompt == "exit":
            break
        messager = response = response.reply(prompt)
        message = response.last
        for c in "Chikku: ":
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.000001)
        for c in message:
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.005)
        print()
if prompt and filename:
    gencode(prompt,filename)
elif fix and filename:
    fixcode(fix,filename)
else:
    bot()

