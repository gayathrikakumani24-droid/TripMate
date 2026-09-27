from tools.tavily_tool import tavily_search
from tools.flight_tool import search_flights
from backend import run_travel_agent
# res=tavily_search("Best hotels in India")
# print(res)
# print(search_flights("Plan a 7 days Japan trip from Bangladesh"))
user_input=input("Enter travel request: ")
response=run_travel_agent(user_input)
print(response["answer"])
