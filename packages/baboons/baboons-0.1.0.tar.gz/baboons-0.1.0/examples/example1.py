# MIT License
#
# Copyright (c) 2023 Clivern
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain


def main():

	information = """
	Elon Reeve Musk is a business magnate, investor and conspiracy theorist.[5] Musk is the founder, chairman, CEO and chief technology officer of SpaceX;
	angel investor, CEO, product architect and former chairman of Tesla, Inc.; owner, chairman and CTO of X Corp.; founder of the Boring Company;
	co-founder of Neuralink and OpenAI; and president of the Musk Foundation. He is the wealthiest person in the world, with an estimated net worth of US$207 billion as of October 2023,
	according to the Bloomberg Billionaires Index, and $231 billion according to Forbes, primarily from his ownership stakes in Tesla and SpaceX
	"""

	summary_template = """
	Given the information {information} about a person from i want you to create:
	1. A short summary
	2. Two interesting facts about him
	"""

	# Clear the white spaces
	information = information.strip()
	summary_template = summary_template.strip()

	summary_prompt_template = PromptTemplate(input_variables=['information'], template=summary_template)

	llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
	chains = LLMChain(llm=llm, prompt=summary_prompt_template)
	print(chains.run(information))

if __name__ == '__main__':
	main()
