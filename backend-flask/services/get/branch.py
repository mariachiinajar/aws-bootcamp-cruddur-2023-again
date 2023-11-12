import subprocess

def get_current_git_branch():
    try:
        # Run the Git command to get the current branch
        result = subprocess.run(['git', 'rev-parse', '--abbrev-ref', 'HEAD'], capture_output=True, text=True, check=True)

        # Extract and return the branch name
        branch_name = result.stdout.strip()
        return branch_name
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return None
        