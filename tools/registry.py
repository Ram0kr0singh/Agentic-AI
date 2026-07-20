from .calculator import execute as calculator
from .time_tool import execute as time_tool
from .weather import execute as weather

TOOLS = {
    "calculator": calculator,
    "time": time,
    "weather": weather,
}

def execute_tool(tool_name: str, arguments: dict):
    tool = TOOLS.get(tool_name)
    
    if tool is None:
        return f"Unknown tool: {tool_name}"
    return tool(arguments)
def list_table():
    return list(TOOLS.keys())

if __name__ == "__main__":
    print("Registered tools\n")
    print(
        execute_tool(
            "calculator",
            {
                "expression": "25*10"
            }
        )
    )
    print("\n")
    
    print(
        execute_tool(
            "time",
            {}
        )
    )
    print(
        execute_tool(
            "weather",
            {
                "city":"delhi"
            }
        )
    )