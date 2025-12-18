# 🐢 Project: Virtualized System Hardening & Security Architecture

**Focus:** Infrastructure, Security Engineering, Systems Resource Management

## Project Overview

Developed a controlled, virtualized Windows environment to implement and audit enterprise-level security protocols. This project focuses on the programmatic application of the Principle of Least Privilege (PoLP) and system-level resource optimization within a Linux-hosted virtualization layer.

## Key Technical Implementations

**Infrastructure & Virtualization:**
* Architected a high-performance Windows environment on a Ubuntu (Linux) host, optimizing hardware resource allocation (8 GB RAM / 6 CPU cores) for stable virtualization.

**Security & Identity Access Management (IAM):**
* Designed a hierarchical user/group structure to enforce strict access control.
* Engineered Group Policy Objects (GPOs) to harden the system's attack surface, including application whitelisting and mandatory password complexity requirements.
* Implemented Least Privilege by auditing and stripping unnecessary administrative rights from standard user accounts.

**Systems Observability & Troubleshooting:**
* Used Event Viewer to monitor for unauthorized access (Event ID 4625), treating system logs as a primary data source for security integrity.
* Managed system-level background processes and services to ensure high availability and uptime.

**Storage Engineering:**
* Performed manual partition manipulation and disk re-allocation to create dedicated data volumes, simulating a multi-tenant storage environment for isolated departmental use.






