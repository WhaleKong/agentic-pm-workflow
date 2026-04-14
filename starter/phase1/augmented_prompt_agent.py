import os
from dotenv import load_dotenv
import workflow_agents.base_agents as base_agents

# Load environment variables from .env file
load_dotenv()

# Retrieve OpenAI API key from environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")

prompt = "What is the capital of France?"
persona = "You are a college professor; your answers always start with: 'Dear students,'"

augmented_agent = base_agents.AugmentedPromptAgent(openai_api_key, persona)

augmented_agent_response = augmented_agent.respond(prompt)

# Print the agent's response
print(augmented_agent_response)

# The agent likely used its pretrained general world knowledge to answer that Paris is
# the capital of France, and the system prompt shaped the style of the reply so it
# sounds like a college professor and begins with "Dear students,".
