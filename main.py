import asyncio
import os
from dotenv import load_dotenv
from researcher.core.researcher import Researcher

async def main():
    load_dotenv()
    researcher = Researcher()
    
    query = "What are the best practices for implementing AI agents?"
    
    try:
        results = await researcher.research(query)
        
        summary = await researcher.summarize(results)
        
        # Print results
        print("\nResearch Results:")
        print("-" * 50)
        for result in results:
            print(f"\nTitle: {result.title}")
            print(f"Source: {result.source}")
            print(f"Relevance: {result.relevance_score}")
            print(f"Content: {result.content[:200]}...")
        
        print("\nSummary:")
        print("-" * 50)
        print(summary)
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    if os.getenv("DEBUG") == "True":
        print("DEBUG MODE ENABLED")
    asyncio.run(main())
