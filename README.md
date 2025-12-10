# ThinkBrands GmbH - Engineering & Operations

Welcome to the central repository for ThinkBrands GmbH engineering tools, scripts, and infrastructure documentation. This repository serves as the single source of truth for our server management, automation scripts, and internal utilities.

## 📂 Repository Structure

The project is organized by technology and purpose. Please ensure you place new files in the appropriate directory to maintain cleanliness.

```text
.
├── scripts/                 # Automation and Utility Scripts
│   ├── python/              # Python automation (e.g., data processing, API connectors)
│   └── shell/               # Bash/Zsh scripts (e.g., server maintenance, backups)
│
├── web/                     # Internal Web Tools
│   ├── static/              # HTML/CSS/JS for landing pages or dashboards
│   └── assets/              # Shared images, JSON configurations, or styles
│
├── docs/                    # Technical Documentation (Knowledge Base)
│   ├── ubuntu-server/       # Server setup, SSH configs, firewall rules
│   ├── docker/              # Dockerfile templates, compose guides, container lists
│   └── n8n/                 # Workflow diagrams, node configurations, JSON exports
│
├── data/                    # Static data files
│   └── json/                # JSON schemas or config dumps
│
└── .gitignore               # Files to exclude from Git (logs, passwords, etc.)
```

## 🚀 Getting Started
### Prerequisites
To run the scripts in this repository, ensure your environment is set up with:
- OS: Ubuntu Server 20.04/22.04 LTS (recommended)
- Python: v3.8+ (Run pip install -r requirements.txt inside specific Python project folders)
- Shell: Zsh or Bash

### Installation & Setup
Clone the repository to your local machine or server:

```
git clone git@github.com:YourUsername/thinkbrands-infrastructure.git
cd thinkbrands-infrastructure
```

## 🛠 Usage Guide
### Running Scripts
Python: Always use a virtual environment when running complex Python scripts.
```
cd scripts/python/my-tool
python3 main.py
```

Shell Scripts: Ensure scripts are executable before running.
```
chmod +x scripts/shell/backup.sh
./scripts/shell/backup.sh
```
### Infrastructure Documentation
- Ubuntu Server: Refer to docs/ubuntu-server/ for guides on SSH hardening, user management, and cron jobs.
- Docker: Check docs/docker/ for our standard docker-compose.yml templates.
- n8n: Workflow JSON exports can be found in docs/n8n/. Import these directly into the n8n UI to restore workflows.

## 🤝 Contribution Guidelines
We follow a standard Git workflow for updates:
1. Pull the latest changes: git pull origin main
2. Make changes in the relevant directory.
3. Stage & Commit:
```
git add .
git commit -m "Add: New automation script for daily reporting"
```
4. Push: ```git push origin main```

##⚠️ Security Note: Never commit .env files, passwords, or API keys. Use environment variables instead.

### 📞 Support & Contact
Maintainer: Ulli Obermeier

Company: ThinkBrands GmbH

Internal Wiki: [Link to Confluence/Notion if applicable]

Last Updated: 2025-12-10
