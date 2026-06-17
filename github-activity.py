#!/usr/bin/env python3
import sys
import json
import urllib.request
import urllib.error

def fetch_user_data(username):
    url = f"https://api.github.com/users/{username}/events"
    
    # Github wants to see a User-Agent header otherwise the request will be declined
    req = urllib.request.Request(url, headers={'User-Agent': 'GitHubActivityCLI'})
    
    try:
        with urllib.request.urlopen(req) as response:
            # Usually the data is in bytes which is unreadable so I need to decoded it with
            # common decoding type utf-8 to convert it into a text string
            user_data = response.read().decode('utf-8')
            
            # Parse the JSON text string into a python object
            list_user_data = json.loads(user_data)
            
            return list_user_data
              
    except urllib.error.HTTPError as e:
        # GitHub responded, but with an error code
        if e.code == 404:
            print(f"Error: The username '{username}' typed doesn't exist on GitHub.")
        elif e.code == 403:
            print("Error: Rate limit exceeded or access forbidden. Try again later.")
        else:
            print(f"GitHub server returned an error code: {e.code}")
            
    except urllib.error.URLError as e:
        # If something is wrong with the internet
        print(f"Error: {e.reason}")
    
    except json.JSONDecodeError as e:
        # The data fetched might be incompatible for json.loads()
        print("Error: Reaceived broken data form GitHub. Please try again.")
        
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        
    return None



def display_github_activity(username):
    events_list = fetch_user_data(username)
    # This list is used to store already proccesed PushEvent repos
    push_totals = {}
    
    if events_list:
        # Loop through all dictionary elements in list
        for event in events_list:
            event_type = event.get("type")
            repo_name = event.get("repo", {}).get("name")
    
            # --- 1. COLLECT PUSH EVENTS SILENTLY ---
            if event_type == "PushEvent":
                payload = event.get("payload", {})
        
                # Calculate individual commits safely right now
                commits = payload.get("size")
                if commits is None:
                    commits = len(payload.get("commits", []))
                if commits == 0:
                    commits = 1
            
                # Add to the dictionary total for this specific repo
                push_totals[repo_name] = push_totals.get(repo_name, 0) + commits

            # --- 2. DISPLAY OTHER EVENTS IMMEDIATELY ---
            elif event_type == "WatchEvent":
                print(f"- Starred {repo_name}")
        
            elif event_type == "IssuesEvent":
                action = event.get("payload", {}).get("action", "interacted with")
                print(f"- {action.capitalize()} an issue in {repo_name}")
                
            elif event_type == "CreateEvent":
                payload = event.get("payload", {})
                ref_type = payload.get("ref_type", {}) # 'repository', 'branch', or 'tag'
                ref_name = payload.get("ref") # Name of the branch/tag (None if it's a repo)
                
                if ref_type == "repository":
                    print(f"- Created a brand new repository: {repo_name}")
                else:
                    print(f"- Created a new {ref_type} ({ref_name}) in {repo_name}")
                    
            elif event_type == "PullRequestEvent":
                payload = event.get("payload")
                action = payload.get("action") # 'opened', 'closed', 'reopened'
                
                # Capitalize makes 'opened' look like 'Opened' to put it in the beginning of the
                # sentence
                print(f"- {action.capitalize()} a pull request in {repo_name}")
                
            else:
                # Formats 'ForkEvent' into 'Fork Event' smoothly
                clean_event_name = event_type.replace("Event", " Event")
                print(f"- Performed a {clean_event_name} on {repo_name}")
                
                

        # --- 3. PRINT ALL SUMMED PUSHES AT THE VERY END ---
        for repo, total_commits in push_totals.items():
            print(f"- Pushed {total_commits} commit(s) to {repo}")
                            
            
        
if __name__ == "__main__":
    
    # If user didn't type github user's name then warn about it
    if len(sys.argv) < 2:
        print("User's name hasn't been typed, the right usage: github-activity <github_username>")
        sys.exit(1) # Stop to prevent code from running anyway
        
    # Put user's name (sys.argv[1]) into the function to see results
    username = sys.argv[1]
    print(f"Fetching recent data for {username}... \n")
    display_github_activity(username)