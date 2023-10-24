import sys
from typing import Generator

import openai
from rich.console import Console
from rich.pretty import install
from rich.traceback import install as ins

install()
ins()
console = Console(record=True, force_terminal=True)

def chat_endpoint(prompt:str,context:str):
	response = openai.ChatCompletion.create(
		model="gpt-3.5-turbo",
		messages=[
			{
				"role":"user",
				"content":prompt
			},
			{
				"role":"system",
				"content":context
			}
		],
		stream=True
	)
	for choice in response:
		chunk = choice.choices[0]["delta"].get("content",None)
		if chunk is None:
			continue
		yield chunk


			
def stream_logs(log_generator:Generator[str,None,None]):
	for log in log_generator:
		console.print(log,markup=True,highlight=True,soft_wrap=True,end="")
		sys.stdout.flush()

def main():
	messages = []
	while True:
		prompt = input("You: ")
		if prompt == "exit":
			break
		messages.append(prompt)
		history = "\n".join(messages[:9])
		context = f"History: {history}\n"
		log_generator = chat_endpoint(prompt,context)
		stream_logs(log_generator)
		print()
	

