from google.adk.agents.llm_agent import Agent

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='A helpful assistant for answering stock related questions.',
    instruction='Answer user questions about stocks accurately using real time data from Nairobi Stocks Exchange(NSE)',
)
