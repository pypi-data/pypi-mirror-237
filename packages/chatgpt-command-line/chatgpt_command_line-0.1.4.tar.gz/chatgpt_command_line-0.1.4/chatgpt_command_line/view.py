import os
import sys
from datetime import datetime
from functools import wraps
from typing import Callable, Generator, TypeVar, cast

import click
import openai
from rich.console import Console
from rich.pretty import install
from rich.traceback import install as ins
from typing_extensions import ParamSpec

from .markdown import render_markdown
from .model import (Embedding, PineconeClient, QueryRequest, UpsertRequest,
                    create_vector)

T = TypeVar("T")
P = ParamSpec("P")

install()
ins()
console = Console(record=True, force_terminal=True)

	
def stream_logs(log_generator:Callable[P,Generator[str,None,None]])->Callable[P,Generator[str,None,None]]:
	@wraps(log_generator)
	def generator(*args: P.args, **kwargs: P.kwargs) -> Generator[str,None,None]:
		for log in log_generator(*args,**kwargs):
			console.print(log,markup=True,highlight=True,end="",emoji=True)
			sys.stdout.flush()
			yield log
	return generator

			
@stream_logs
def chat_endpoint(prompt:str,context:str)->Generator[str,None,None]:
	response = openai.ChatCompletion.create( # type: ignore
		model="gpt-3.5-turbo-16k",
		messages=[
			{
				"role":"user",
				"content":prompt
			},
			{
				"role":"system",
				"content":context
			},
			
		],
		stream=True,
		temperature=0.9,
		max_tokens=512
	)
	for choice in response: # type: ignore
		chunk = choice.choices[0]["delta"].get("content",None) # type: ignore
		if chunk is None:
			continue
		yield cast(str,chunk)


		
@click.group()
def cli():
	pass

@cli.command()
def chat():
	"""Chat with GPT-3.5 Large Language Model."""
	messages:list[str] = []
	while True:
		try:
			prompt = input(">>> ")
			if prompt == "exit":
				break
			messages.append(prompt)
			context = "\n".join(messages)
			string = ""
			for chunk in chat_endpoint(prompt,context):
				string += chunk
			messages.append(string)
			print("\n")
		except:
			os.makedirs("logs",exist_ok=True)
			_date = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
			with open(f"logs/{_date}.html","w") as f:
				f.write(render_markdown(f"# Conversation {_date}"+"\n".join(messages)))
			break
	