import pandas as pandas_lib
import requests
import io

def handler(pd: "Ipipedream"):
    # 1. Fetch from GitHub
    url = "https://raw.githubusercontent.com/stephspaulding/clinical-data-interop-pipeline/refs/heads/main/triage.csv"
    r = requests.get(url)
    
    try:
        # 2. The most basic, explicit load possible
        # sep=',' and engine='c' prevents sniffing
        df = pandas_lib.read_csv(
            io.StringIO(r.text), 
            sep=',', 
            engine='c',
            header=0
        )
        
        # 3. Clean headers (Remove spaces and hidden characters)
        df.columns = df.columns.str.strip().str.lower()
        print(f"Columns Found: {list(df.columns)}")

        # 4. Convert Acuity to numbers (errors become NaN)
        df['acuity'] = pandas_lib.to_numeric(df['acuity'], errors='coerce')
        
        # 5. Filter for high priority
        high_priority = df[df['acuity'] <= 2].copy()
        
        return {
            "status": "Success",
            "metrics": {
                "total_rows": len(df),
                "high_priority_count": len(high_priority)
            },
            "alerts": high_priority.to_dict('records')
        }

    except Exception as e:
        # If it fails, we want to see EXACTLY why
        return {
            "status": "Critical Failure",
            "details": str(e),
            "preview": r.text[:100] # Show us what the data looks like
        }
