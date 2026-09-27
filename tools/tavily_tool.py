from tavily import TavilyClient
import os
from dotenv import load_dotenv
load_dotenv()
client=TavilyClient(
    api_key=os.getenv('TAVILY_API_KEY'),
)
def tavily_search(query):
    response=client.search(
        query=query,
        max_results=5
        )
    results=[]
    for i,r in enumerate(response["results"]):
        title=r.get("title","Unknown")
        url=r.get("url","Unknown")
        snippet=r.get("content","Unknown")
        if len(snippet)>300:
            snippet=snippet[:300]+"..."
        results.append(f"Title: {title}\nURL: {url}\nSnippet: {snippet}")#"title":title,"url":url,"snippet":snippet)
    return "\n\n".join(results)