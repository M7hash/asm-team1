# ASM Platform - Team 1 Recon Service

## Overview

The Recon Service is the Team 1 component of the Attack Surface Management (ASM) Platform.

This service performs automated reconnaissance against a target domain by:

1. Discovering subdomains using Subfinder
2. Identifying live hosts using HTTPX
3. Performing port and service discovery using Nmap
4. Storing discovered assets in PostgreSQL
5. Exposing results through FastAPI REST APIs

---

## Architecture

```
Target Domain
      │
      ▼
  Subfinder
      │
      ▼
    HTTPX
      │
      ▼
  Live Hosts
      │
      ▼
     Nmap
      │
      ▼
 PostgreSQL
      │
      ▼
 FastAPI APIs
```

---

## Features

* Subdomain Discovery
* Live Host Detection
* Port Scanning
* PostgreSQL Asset Storage
* FastAPI REST APIs
* JSON Output for Team Integration

---

## Project Structure

```
asmplatform/
│
|── main.py
│
├── recon/
│   ├── subfinder.py
│   ├── httpx_scan.py
│   └── nmap_scan.py
│
├── database/
│   ├── db.py
│   └── asset_repository.py
│
│
└── README.md
```

---

## Requirements

### Python

* Python 3.10+

### Tools

* Subfinder
* HTTPX
* Nmap
* PostgreSQL

---

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/asmplatform.git
cd asmplatform
```

### Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Python Dependencies

```bash
pip install -r requirements.txt
```

---

## PostgreSQL Setup

Create database:

```sql
CREATE DATABASE asm;
```

Create assets table:

```sql
CREATE TABLE assets (
    id SERIAL PRIMARY KEY,
    hostname TEXT NOT NULL,
    source TEXT NOT NULL,
    discovered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## Running the Service

```bash
uvicorn app.main:app --reload
```

Server:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```





