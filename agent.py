from google.adk.agents import LlmAgent
from google.adk.tools import agent_tool
from google.adk.tools.google_search_tool import GoogleSearchTool
from google.adk.tools import url_context

subagent_google_search_agent = LlmAgent(
  name='Subagent_google_search_agent',
  model='gemini-2.5-flash',
  description=(
      'Agent specialized in performing Google searches.'
  ),
  sub_agents=[],
  instruction='Use the GoogleSearchTool to find information on the web.',
  tools=[
    GoogleSearchTool()
  ],
)

subagent_url_context_agent = LlmAgent(
  name='Subagent_url_context_agent',
  model='gemini-2.5-flash',
  description=(
      'Agent specialized in fetching content from URLs.'
  ),
  sub_agents=[],
  instruction='Use the UrlContextTool to retrieve content from provided URLs.',
  tools=[
    url_context
  ],
)
subagent = LlmAgent(
  name='subagent',
  model='gemini-2.5-flash',
  description=(
      'Agent that handles a specific task'
  ),
  sub_agents=[],
  instruction='',
  tools=[
    agent_tool.AgentTool(agent=subagent_google_search_agent),
    agent_tool.AgentTool(agent=subagent_url_context_agent)
  ],
)
ghg_expert_google_search_agent = LlmAgent(
  name='GHG_Expert_google_search_agent',
  model='gemini-2.5-flash',
  description=(
      'Agent specialized in performing Google searches.'
  ),
  sub_agents=[],
  instruction='Use the GoogleSearchTool to find information on the web.',
  tools=[
    GoogleSearchTool()
  ],
)
ghg_expert_url_context_agent = LlmAgent(
  name='GHG_Expert_url_context_agent',
  model='gemini-2.5-flash',
  description=(
      'Agent specialized in fetching content from URLs.'
  ),
  sub_agents=[],
  instruction='Use the UrlContextTool to retrieve content from provided URLs.',
  tools=[
    url_context
  ],
)
root_agent = LlmAgent(
  name='GHG_Expert',
  model='gemini-2.5-flash',
  description=(
      'Agent to help with GHG or carbon accounting related  questions.'
  ),
  sub_agents=[subagent],
  instruction='# you are an AI agent to help user with questions related to following topics\n- GHG accounting\n- ESG Reporting\n- Sustainability Reporting\n- ESG\n- Net zero or carbon accounting.\n- Emissions Factors\n',
  tools=[
    agent_tool.AgentTool(agent=ghg_expert_google_search_agent),
    agent_tool.AgentTool(agent=ghg_expert_url_context_agent)
  ],
)