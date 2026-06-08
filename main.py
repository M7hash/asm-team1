from fastapi import FastAPI
from recon.subfinder import run_subfinder
from recon.httpx_scan import run_httpx
from recon.nmap_scan import run_nmap
from database.asset_repository import save_asset
from database.db import get_connection

app = FastAPI()


@app.get("/")
def home():
    return {
        "service": "ASM Recon Service",
        "status": "running"
    }


@app.get("/discover")
def discover(domain: str):

    hosts = run_subfinder(domain)

    hosts = [
        host.strip()
        for host in hosts
        if host.strip()
    ]

    for host in hosts:
        save_asset(host, "subfinder")

    return {
        "status": "success",
        "domain": domain,
        "total_subdomains": len(hosts),
        "assets": [
            {
                "hostname": host,
                "source": "subfinder"
            }
            for host in hosts
        ]
    }


@app.get("/assets")
def get_assets():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT id, hostname, source, discovered_at
        FROM assets
        ORDER BY id DESC
    """)

    rows = cur.fetchall()

    cur.close()
    conn.close()

    return {
        "total_assets": len(rows),
        "assets": [
            {
                "id": row[0],
                "hostname": row[1],
                "source": row[2],
                "discovered_at": str(row[3])
            }
            for row in rows
        ]
    }

@app.get("/live")
def live(domain: str):
    hosts = run_subfinder(domain)
    live_hosts = run_httpx(hosts)

    return {
        "status": "success",
        "domain": domain,
        "total_live_hosts": len(live_hosts),
        "live_hosts": live_hosts
    }

@app.get("/scan")
def scan(host: str):

    ports = run_nmap(host)

    return {
        "status": "success",
        "host": host,
        "scan_result": result
    }

@app.get("/recon")
def recon(domain: str):

    # Step 1 - Find Subdomains
    hosts = run_subfinder(domain)

    # Step 2 - Find Live Hosts
    live_hosts = run_httpx(hosts)

    results = []

    # Step 3 - Scan Live Hosts
    for host in live_hosts[:10]:

        try:
            nmap_result = run_nmap(host)

            results.append({
                "host": host,
                "open_ports": ports
            })

        except Exception as e:

            results.append({
                "host": host,
                "error": str(e)
            })

    return {
        "status": "success",
        "domain": domain,
        "subdomains_found": len(hosts),
        "live_hosts_found": len(live_hosts),
        "results": results
    }
