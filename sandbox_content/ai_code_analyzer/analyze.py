'''
AI-powered code analyzer for the Ultimate Lyra Trading System.

This script uses curl to make direct requests to the Google Gemini API to analyze the codebase, categorize files,
and generate documentation.
'''

import os
import subprocess
import json

def analyze_file(file_path):
    '''Analyzes a single file using the Gemini API via curl.

    Args:
        file_path: The path to the file to analyze.

    Returns:
        A dictionary containing the analysis results, or None on error.
    '''
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()

        if not content.strip():
            return json.dumps({
                "file_path": file_path,
                "category": "Empty File",
                "summary": "This file is empty.",
                "rating": 0,
            })

        api_key = os.environ.get("GEMINI_API_KEY")
        if not api_key:
            print("Error: GEMINI_API_KEY environment variable not set.")
            return None

        prompt = f"""
        Analyze the following code file and provide a detailed analysis in JSON format.

        File Path: {file_path}
        File Content:
        ```
        {content}
        ```

        Provide the following information in your JSON response:
        - "file_path": The full path of the file.
        - "category": The category of the file (e.g., "Core Logic", "Utility", "Data", "Documentation", "Configuration", "Testing", "Deployment", "Other").
        - "summary": A concise summary of the file's purpose and functionality.
        - "rating": A rating from 1 to 10 for code quality, readability, and maintainability.
        - "suggestions": A list of suggestions for improvement (e.g., refactoring, documentation, performance).
        """

        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"

        headers = {
            "Content-Type": "application/json",
        }

        data = {
            "contents": [
                {
                    "parts": [
                        {
                            "text": prompt
                        }
                    ]
                }
            ]
        }

        response = subprocess.run(
            ['curl', '-s', '-X', 'POST', '-H', 'Content-Type: application/json', '-d', json.dumps(data), url],
            capture_output=True,
            text=True
        )

        if response.returncode == 0:
            return response.stdout
        else:
            print(f"Error calling Gemini API for {file_path}: {response.stderr}")
            return None

    except Exception as e:
        print(f"Error analyzing file {file_path}: {e}")
        return None

def main():
    '''Main function to analyze the entire codebase.'''
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    analysis_results = []

    for root, _, files in os.walk(CODEBASE_PATH):
        for file in files:
            file_path = os.path.join(root, file)
            print(f"Analyzing: {file_path}")
            result = analyze_file(file_path)
            if result:
                analysis_results.append(result)

    # Save the analysis results to a file
    with open(os.path.join(OUTPUT_DIR, "analysis_summary.json"), "w") as f:
        f.write("\n".join(analysis_results))

    print(f"\nAnalysis complete. Results saved to {OUTPUT_DIR}/analysis_summary.json")


if __name__ == "__main__":
    CODEBASE_PATH = "/home/ubuntu/github_push_staging"
    OUTPUT_DIR = "/home/ubuntu/ai_analysis_results"
    main()

