import subprocess

def run_httpx(hosts):

    result = subprocess.run(
        ["/home/kali/go/bin/httpx", "-silent"],
        input="\n".join(hosts),
        capture_output=True,
        text=True
    )

    return result.stdout.splitlines()
