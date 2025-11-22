Windows 10 Pro Local Administration Portfolio

Project Goal
To demonstrate core competency in Windows system administration and security by successfully deploying and configuring a single Windows 10 Pro Virtual Machine on a Linux host, utilizing local administrative tools to mimic enterprise policies and best practices. 

1. Virtual Machine Deployment & Configuration

Virtualization set-up, OS installation (manual, non-unattended), resource allocation, and initial setup troubleshooting. 

A. VM Deployment - Successfully installed a functional Windows 10 Pro VM on a Ubuntu host. 
B. Initial Configuration - Allocated 8 GB Ram and 6 CPU cores for optimal performance. 
C. Server Manager Installation - Installed Server Manager (RSAT) for future Active Directory and remote management projects. 

2. Identify and Access Management

Creation and modification of local user accounts and security groups (compmgmt.msc).

A. Local User Creation - Created local user accounts (PracticeUser and PracticeUser2) for testing security and access permissions. 
B. Local Group Creation - Created the group Local_CCA, a local group for Customer Care Associates.
C. Group Membership Management - Successfully added users to the Local_CCA group. 
D. Privilege Management - Removed a standard account from the local Administrators group to enforce principle of least privilege. 

3. Security Policy and Access Control

System hardening via Group Policy and application restriction.

A. Application Restriction (Group Policy) - Used Local Group Policy Editor (gpedit.msc) to Disable all apps from Windows Store, restricting access for all standard users, including the Local_CCA group. 
B. Immediate Policy Enforcement - Used the command gpupdate /force in Command Prompt to apply the policy changes immediately without rebooting. 
C. Password Policy Hardening - Used gpedit.msc to set the minimum password length to 8 characters instead of 0 to enhance account security. 

4. Troubleshooting and Monitoring

Auditing security events and managing essential system services. 

A. Auditing Failed Logins - Used Event Viewer to filter the Security Log for the Event ID 4625 (Failed Logins) to monitor security integrity. Verified the system had zero failed login attempts after initial setup. 
B. Service Management - Restarted the Print Spooler service to clear a hypothetical stuck print queue, demonstrating a core troubleshooting step. 

5. Resource and Storage Management 

A. Disk Management (Shrink) - Used Disk Management to shrink the main C: drive partition, creating a section of unallocated space. 
B. Volume Creation and Allocation - Created a new E: drive from the unallocated space. This drive is designed for use by the Local_CCA group to simulate centralized resource access. 
C. Verification - Verified the successful creation of the new volume through File Explorer. 






