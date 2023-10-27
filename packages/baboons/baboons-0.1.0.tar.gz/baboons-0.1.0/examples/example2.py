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

	# Fetch data from someone linkein. You can even feed it as a JSON
	information = """
	Hi, I am Ahmed, a software developer interested specifically in development using PHP, Python, Go, Java, MySQL, Javascript, Rust & Elixir Newbie!
	I don’t believe on a specific language or a framework but on software principles that translate across language barriers. Frameworks and even programming languages change fast but principles are evergreen. I studied Petroleum Engineering (Yes I am a Petroleum Engineer :D). Weird Right! But It’s been an interesting journey to get here.
	I love challenges, Never settle for less, Always looking to improve and play nice with both humans and machines. Also I like gaming, photography. I been into Arduino and Electronics for a while now.
	Specialties: PHP, Python, Golang, Rust, Elixir, Java, Javascript, MySQL, NoSQL, MongoDB, Cassandra, HTML, CSS, Laravel, Symfony, Angular, CodeIgniter, Flask, Django, Vert.x, BackboneJs, jQuery, Ajax, Slim, WordPress Plugin and Themes Development, LAMP, OOP, VCS, GIT, Continuous Integration, Chef, Jenkins, ElasticSearch, RabbitMQ, Kafka, HAProxy, Vagrant, Consul, Grafana, Prometheus, Nomad, Terraform, Docker, Kubernetes, MVC, Composer, Bower, VueJs, Typescript, TDD, Linux, Cloud Computing, DevOps, Bash, Apache, Nginx, Scrum.
	Current Interests: Scaling Web Applications, Microservices Architecture, Cloud Native Architecture, High Availability and Automation.
	I would love to hear from you, and what you think about clivern. All feedback is welcome and if you have any idea you’d like to share or what you think I should write about next, let me know!
	You can reach me at hello at clivern.com
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
