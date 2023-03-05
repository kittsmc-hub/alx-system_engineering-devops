POSTMORTEM
Issue Summary:
Duration: 12 hours, from 10:00 PM on March 1, 2023, to 10:00 AM on March 2, 2023 (UTC-8)
Impact: The web application was inaccessible for all users during the entire duration of the outage. All users attempting to access the application were met with a "404 error" message. The application serves around 10,000 users daily, and all of them were affected.
Root Cause: A misconfiguration in the load balancer resulted in an outage.
Timeline:
10:00 PM (UTC-8) on March 1, 2023: The outage was detected by a monitoring system.
10:05 PM: The engineering team was alerted about the issue and began investigating the cause.
10:10 PM: The team identified that the application was not responding to requests.
10:15 PM: The team noticed that the load balancer logs showed no traffic was reaching the application servers.
10:20 PM: The team began investigating the load balancer configuration and found that the SSL certificate had expired.
10:30 PM: The team updated the SSL certificate and restarted the load balancer, but the issue persisted.
11:00 PM: The team discovered that the load balancer's configuration had been accidentally changed, which was preventing traffic from reaching the application servers.
1:00 AM: After several attempts to fix the issue, the team escalated the incident to senior engineers.
3:00 AM: The senior engineers discovered that a misconfiguration in the load balancer resulted in the outage and worked to fix the issue.
10:00 AM on March 2, 2023: The incident was resolved, and the application was accessible again.
Root Cause and Resolution:
The root cause of the outage was a misconfiguration in the load balancer. Specifically, the load balancer was incorrectly configured to route traffic to a nonexistent server. This resulted in all traffic being dropped, preventing users from accessing the application. The resolution involved reconfiguring the load balancer to correctly route traffic to the application servers.
Corrective and Preventative Measures:
To prevent similar incidents in the future, the following corrective and preventative measures will be taken:
Update the load balancer configuration backup process to prevent accidental misconfigurations.
Implement regular load balancer configuration reviews to ensure that the configuration is up to date and properly configured.
Improve the monitoring system to detect load balancer misconfigurations quickly.
Conduct load balancer failover tests to ensure that the failover process is working as expected.
Train the engineering team on best practices for load balancer configuration and maintenance.
TODO:
Update the load balancer configuration backup process.
Schedule regular load balancer configuration reviews.
Improve the monitoring system to detect load balancer misconfigurations.
Conduct load balancer failover tests.
Train the engineering team on best practices for load balancer configuration and maintenance.
In conclusion, the outage was caused by a misconfiguration in the load balancer, resulting in an application outage for 12 hours. The engineering team worked to identify and resolve the issue, and corrective and preventative measures have been put in place to prevent similar incidents in the future.
 
