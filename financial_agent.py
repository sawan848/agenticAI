import os
import openai
from dotenv import load_dotenv
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
load_dotenv()

openai.api_key=os.getenv("OPENAI_API_KEY")



# web search agent
web_search_agent=Agent(
    name="Web serach Agent",
    role="Search the web for the information",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[DuckDuckGo()],
    instructions=["Alway include sources"],
    show_tool_calls=True,
    markdown=True
)

# Financial Agent
finance_agent=Agent(
    name="Finance AI Agent",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[YFinanceTools(stock_price=True,analyst_recommendations=True,stock_fundamentals=True,company_info=True,company_news=True)],

    instructions=["Use tables to display the data"],
    show_tool_calls=True,
    markdown=True
)

multi_ai_agent=Agent(
    model=Groq(id="llama-3.1-70b-versatile"),
    team=[web_search_agent,finance_agent],
    instructions=["Always include sources","Use tables to display the data"],
    show_tool_calls=True,
    markdown=True
)
multi_ai_agent.print_response("Summarize analyst recomendation and share the latest news for NVDA",stream=True)

print("Hellow ")