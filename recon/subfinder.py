import subprocess

def run_subfinder(domain):

    result = subprocess.run(
        ["subfinder", "-d", domain, "-silent"],
        capture_output=True,
        text=True
    )

    return result.stdout.splitlines()


if __name__ == "__main__":

    hosts = run_subfinder("tesla.com")

    for host in hosts:
        print(host)
