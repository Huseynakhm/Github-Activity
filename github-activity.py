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
    
    except json.JSONDEcodeError as e:
        # The data fetched might be incompatible for json.loads()
        print("Error: Reaceived broken data form GitHub. Please try again.")
        
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        
    return None



def display_github_activity(username):
    events_list = fetch_user_data(username)
    
    if events_list:
        # Loop through all dictionary elements in list
        for event in events_list:
            # Get the type of event type
            event_type = event.get("type")
            
            # Get the name of the repository in this type
            repo_name = event.get("repo", {}).get("name")
            
            # If the event is PushEvent then print the count of comits to the screen
            if event_type == "PushEvent":
                payload = event.get("payload", {})
                
                # Look up to "size" key to get the count of commits
                count_of_commits = payload.get("size")
                
                # We check whether there was size key or not if there wasn't then we manually
                # count all commits from commits key 
                if count_of_commits is None:
                    count_of_commits = len(payload.get("commits", []))
                    
                # If still there was nothing then commits count is 1 because there was initially a PushEvent type, 
                # meaning the user published the code some time ago 
                if count_of_commits == 0:
                    count_of_commits = 1
                    
                print(f"- Pushed {count_of_commits} commit(s) to {repo_name}")
                
                
            # If the event type is WatchEvent then show the starred project
            if event_type == "WatchEvent":
                payload = event.get("payload", {})
                action = payload.get("action")
                
                if action == "started":
                    print(f"- Starred {repo_name}")
                    
              
            # If user opened a bug report or feature request        
            if event_type == "IssuesEvent":
                payload = event.get("paylaod", {})
                action = payload.get("action")
                
                if action == "opened":
                    print(f"- Opened a pull request in {repo_name}")
                elif action == "closed":
                    print(f"- Cloased a pull request in {repo_name}")
                elif action == "reopened":
                    print(f"- Reopened a pull request in {repo_name}")
                    
            
            # If user submitted code changes to be reviewed                    
            if event_type == "PullRequestEvent":
                payload = event.get("payload", {})
                action = payload.get("action")
                
                if action == "opened":
                    print(f"- Opened a pull request in {repo_name}")
                elif action == "closed":
                    print(f"- Merged {repo_name}")
                    
            
            
            # If user made a new branch or release tag
            if event_type == "CreateEvent":
                payload = event.get("payload", {})
                ref_type = payload.get("ref_type")
                
                if ref_type == "branch":
                    print(f"- Created a new branch in {repo_name}")
                elif ref_type == "tag":
                    print(f"- Tagged a branch in {repo_name}")
                            
            
        
if __name__ == "__main__":
    
    # If user didn't type github user's name then warn about it
    if len(sys.argv) < 2:
        print("User's name hasn't been typed, the right usage: github-activity <github_username>")
        
    # Put user's name (sys.argv[1]) into the function to see results
    username = sys.argv[1]
    print(f"Fetching recent data for {username}... \n")
    display_github_activity(username)