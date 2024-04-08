import os
import json
from utils import *

curdir = os.getcwd()

with open ('config.json', 'r') as f:
    config = json.load(f)

github = config['link']['github']

def setupPrometheus():
    print_message("Setting Prometheus Service --", color = 'magenta')
    try:
        os.system("sudo yum install epel-release -y")
        print_message("Installed epel-release", color='green')
    except Exception as e:
        print_message("Error intalling Epel-release:", e)
    try:
        os.system("sudo yum install hping3 -y")
        print_message("Installed hping3", color='green')
    except Exception as e:
        print_message("Error installing hping3:", e)
    try:
        os.system("sudo useradd --no-create-home --shell /bin/false prometheus")
        print_message("Added New User: Prometheus", color='green')
    except Exception as e:
        print_message("Error adding user:", e)
    
    try:
        os.system("sudo mkdir /etc/prometheus")
        print_message("Created New Folder : /etc/prometheus", color='green')
    except Exception as e:
        print_message(f"Error creating directory /etc/prometheus: {e}", color='red')
    
    try:
        os.system("sudo mkdir /var/lib/prometheus")
        print_message("Created New Folder : /var/lib/prometheus", color='green')
    except Exception as e:
        print_message(f"Error creating directory /var/lib/prometheus: {e}", color='red')
    
    try:
        os.system("sudo chown prometheus:prometheus /etc/prometheus")
        print_message("Changed Owner for /etc/prometheus : prometheus", color='green')
    except Exception as e:
        print_message(f"Error changing ownership of /etc/prometheus: {e}", color='red')
    
    try:
        os.system("sudo chown prometheus:prometheus /var/lib/prometheus")
        print_message("Changed Owner for /var/lib/prometheus", color='green')
    except Exception as e:
        print_message(f"Error changing ownership of /var/lib/prometheus: {e}", color='red')
    
    try:
        os.system(f"sudo cp {curdir}/prometheus/prometheus /usr/local/bin/")
        print_message("Successfully Copied Prometheus to /usr/local/bin", color='green')
    except Exception as e:
        print_message(f"Error copying prometheus binary: {e}", color='red')
    
    try:
        os.system(f"sudo chmod 777 /usr/local/bin/prometheus ")
        print_message("Successfully Added Execution Permission for /usr/local/bin/prometheus", color='green')
    except Exception as e:
        print_message(f"Error Adding Execution Permission for /usr/local/bin/prometheus: {e}", color='red')
    try:
        os.system(f"sudo cp {curdir}/prometheus/promtool /usr/local/bin/")
        print_message("Successfully Copied Promtool to /usr/local/bin", color='green')
    except Exception as e:
        print_message(f"Error copying promtool binary: {e}", color='red')
    
    try:
        os.system(f"sudo cp -r {curdir}/prometheus/consoles /etc/prometheus")
        print_message("Successfully Copied Consoles to /etc/prometheus", color='green')
    except Exception as e:
        print_message(f"Error copying consoles directory: {e}", color='red')
    
    try:
        os.system(f"sudo cp -r {curdir}/prometheus/console_libraries /etc/prometheus")
        print_message("Successfully Copied Console_libraries to /etc/prometheus", color='green')
    except Exception as e:
        print_message(f"Error copying console_libraries directory: {e}", color='red')
    
    try:
        os.system(f"sudo cp {curdir}/services/prometheus.service /etc/systemd/system/prometheus.service")
        print_message("Successfully Added prometheus.service to /etc/systemd/system", color='green')
    except Exception as e:
        print_message(f"Error copying prometheus.service file: {e}", color='red')
    
    try:
        os.system(f"sudo cp {curdir}/prometheus/prometheus.yml /etc/prometheus/prometheus.yml")
        print_message("Successfully Copied prometheus.yml to /etc/prometheus", color='green')
    except Exception as e:
        print_message(f"Error copying prometheus.yml file: {e}", color='red')
    
    try:
        os.system(f"sudo cp {curdir}/prometheus/rules.yml /etc/prometheus/rules.yml")
        print_message("Successfully Copied rules.yml to /etc/prometheus", color='green')
    except Exception as e:
        print_message(f"Error copying rules.yml file: {e}", color='red')
    
    try:
        os.system(f"sudo cp {curdir}/prometheus/sqlrules.yml /etc/prometheus/sqlrules.yml")
        print_message("Successfully Copied sqlrules.yml to /etc/prometheus", color='green')
    except Exception as e:
        print_message(f"Error copying sqlrules.yml file: {e}", color='red')
    
    try:
        os.system("sudo systemctl daemon-reload")
        print_message("Successfully Reloaded System Daemon", color='green')
    except Exception as e:
        print_message(f"Error reloading systemd daemon: {e}", color='red')
    
    try:
        os.system("sudo systemctl start prometheus")
        print_message("Successfully Started prometheus.service", color='green')
    except Exception as e:
        print_message(f"Error starting prometheus service: {e}", color='red')

def setupAlertmanager():
    print_message("Setting Alertmanager Service --", color='magenta')
    try:
        os.system("sudo groupadd -f alertmanager")
        print_message("Added New Group: alertmanager", color='green')
    except Exception as e:
        print_message("Error adding group:", e, color='red')

    try:
        os.system("sudo useradd -g alertmanager --no-create-home --shell /bin/false alertmanager")
        print_message("Added New User: alertmanager", color='green')
    except Exception as e:
        print_message("Error adding user:", e, color='red')
    
    try:
        os.system("sudo mkdir -p /etc/alertmanager/templates")
        print_message("Created New Folder: /etc/alertmanager/templates", color='green')
    except Exception as e:
        print_message(f"Error creating directory /etc/alertmanager/templates: {e}", color='red')
    
    try:
        os.system("sudo mkdir /var/lib/alertmanager")
        print_message("Created New Folder: /var/lib/alertmanager", color='green')
    except Exception as e:
        print_message(f"Error creating directory /var/lib/alertmanager: {e}", color='red')
    
    try:
        os.system("sudo chown alertmanager:alertmanager /etc/alertmanager")
        print_message("Changed Owner for /etc/alertmanager: alertmanager", color='green')
    except Exception as e:
        print_message(f"Error changing ownership of /etc/alertmanager: {e}", color='red')
    
    try:
        os.system("sudo chown alertmanager:alertmanager /var/lib/alertmanager")
        print_message("Changed Owner for /var/lib/alertmanager: alertmanager", color='green')
    except Exception as e:
        print_message(f"Error changing ownership of /var/lib/alertmanager: {e}", color='red')
    
    try:
        os.system(f"sudo cp {curdir}/alertmanager/alertmanager /usr/bin/")
        print_message("Copied alertmanager binary to /usr/bin/", color='green')
    except Exception as e:
        print_message("Error copying alertmanager binary:", e, color='red')
    
    try:
        os.system(f"sudo cp {curdir}/alertmanager/amtool /usr/bin/")
        print_message("Copied amtool binary to /usr/bin/", color='green')
    except Exception as e:
        print_message("Error copying amtool binary:", e, color='red')
    
    try:
        os.system("sudo chown alertmanager:alertmanager /usr/bin/alertmanager")
        print_message("Changed Owner for /usr/bin/alertmanager: alertmanager", color='green')
    except Exception as e:
        print_message("Error changing ownership of /usr/bin/alertmanager:", e, color='red')
    
    try:
        os.system("sudo chown alertmanager:alertmanager /usr/bin/amtool")
        print_message("Changed Owner for /usr/bin/amtool: alertmanager", color='green')
    except Exception as e:
        print_message("Error changing ownership of /usr/bin/amtool:", e, color='red')
    
    try:
        os.system(f"sudo cp {curdir}/alertmanager/alertmanager.yml /etc/alertmanager/alertmanager.yml")
        print_message("Copied alertmanager.yml to /usr/bin/alertmanager/", color='green')
    except Exception as e:
        print_message("Error copying alertmanager.yml file:", e, color='red')
    
    try:
        os.system("sudo chown alertmanager:alertmanager /etc/alertmanager/alertmanager.yml")
        print_message("Changed Owner for /etc/alertmanager/alertmanager.yml: alertmanager", color='green')
    except Exception as e:
        print_message("Error changing ownership of /etc/alertmanager/alertmanager.yml:", e, color='red')
    
    try:
        os.system(f"sudo cp {curdir}/services/alertmanager.service /etc/systemd/system/alertmanager.service")
        print_message("Copied alertmanager.service file to /etc/systemd/system/", color='green')
    except Exception as e:
        print_message("Error copying alertmanager.service file:", e, color='red')
    
    try:
        os.system("sudo systemctl daemon-reload")
        print_message("Reloaded systemd daemon", color='green')
    except Exception as e:
        print_message("Error reloading systemd daemon:", e, color='red')
    
    try:
        os.system("sudo systemctl start alertmanager")
        print_message("Started Alertmanager service", color='green')
    except Exception as e:
        print_message("Error starting Alertmanager service:", e, color='red')

def setupNodeExporter():
    print_message("Setting up NodeExporter Service --", color='magenta')
    try:
        os.system("sudo groupadd -f node_exporter")
        print_message("Added New Group: node_exporter", color='green')
    except Exception as e:
        print_message("Error adding group:", e, color='red')

    try:
        os.system("sudo useradd -g node_exporter --no-create-home --shell /bin/false node_exporter")
        print_message("Added New User: node_exporter", color='green')
    except Exception as e:
        print_message("Error adding user:", e, color='red')
    
    try:
        os.system("sudo mkdir /etc/node_exporter")
        print_message("Created New Folder: /etc/node_exporter", color='green')
    except Exception as e:
        print_message(f"Error creating directory /etc/node_exporter: {e}", color='red')
    
    try:
        os.system("sudo chown node_exporter:node_exporter /etc/node_exporter")
        print_message("Changed Owner for /etc/node_exporter: node_exporter", color='green')
    except Exception as e:
        print_message(f"Error changing ownership of /etc/node_exporter: {e}", color='red')
    
    try:
        os.system(f"sudo cp {curdir}/node_exporter/node_exporter /usr/bin/")
        print_message("Copied node_exporter binary to /usr/bin/", color='green')
    except Exception as e:
        print_message("Error copying node_exporter binary:", e, color='red')
    
    try:
        os.system("sudo chown node_exporter:node_exporter /usr/bin/node_exporter")
        print_message("Changed Owner for /usr/bin/node_exporter: node_exporter", color='green')
    except Exception as e:
        print_message("Error changing ownership of /usr/bin/node_exporter:", e, color='red')
    
    try:
        os.system(f"sudo cp {curdir}/services/node_exporter.service /etc/systemd/system/node_exporter.service")
        print_message("Copied node_exporter.service file to /etc/systemd/system/", color='green')
    except Exception as e:
        print_message("Error copying node_exporter.service file:", e, color='red')
    
    try:
        os.system("sudo chmod 777 /etc/systemd/system/node_exporter.service")
        print_message("Changed permissions for /etc/systemd/system/node_exporter.service", color='green')
    except Exception as e:
        print_message("Error changing permissions for /etc/systemd/system/node_exporter.service:", e, color='red')
    
    try:
        os.system("sudo systemctl daemon-reload")
        print_message("Reloaded systemd daemon", color='green')
    except Exception as e:
        print_message("Error reloading systemd daemon:", e, color='red')
    
    try:
        os.system("sudo systemctl start node_exporter")
        print_message("Started NodeExporter service", color='green')
    except Exception as e:
        print_message("Error starting NodeExporter service:", e, color='red')
    
    try:
        os.system("sudo firewall-cmd --permanent --zone=public --add-port=9200/tcp")
        print_message("Opened port 9200/tcp in firewall", color='green')
    except Exception as e:
        print_message("Error opening port 9200/tcp in firewall:", e, color='red')
    
    try:
        os.system("sudo firewall-cmd --reload")
        print_message("Reloaded firewall", color='green')
    except Exception as e:
        print_message("Error reloading firewall:", e, color='red')

def setupMySQLExporter():
    pass

def main() -> None:
    setupPrometheus()
    setupAlertmanager()
    setupNodeExporter()
    setupMySQLExporter()

def print_header(page="main"):
    if page=="main":
        print_message('WELCOME TO STRESS TESTER', color='blue', centered=True)
    elif page=="setup":
        print_message('WELCOME TO STRESS TESTER - SETUP', color='magenta', centered=True)

    print_br()
    print_message('By - Shubham Namdev', color = 'blue')
    print('For more info, visit -> ', end = '')
    print_message(f'{github}', 'green')
    print_br()

if __name__ == "__main__":
    clear()
    print_header()
    main()

