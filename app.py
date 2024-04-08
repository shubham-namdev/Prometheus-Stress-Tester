import os
import socket
import json
import time
from utils import *
import nodeTests as nt


class StressTester:
    def __init__(self) -> None:

        self.load_variables()
        """Start Section"""
        self.run()

    def load_variables(self) -> None:
        self.json_file = r'config.json'
        with open(self.json_file, 'r') as f:
            self.config = json.load(f)

        self.IPnodeEx = self.config["ip"]["node_exporter"]
        self.IPmysql = self.config["ip"]["mysql"]
        self.github = self.config["link"]["github"]
        self.rulesYML = self.config["paths"]["rulesYML"]
        self.sqlrulesYML = self.config["paths"]["sqlrulesYML"]
        self.alertmanagerYML = self.config["paths"]["alertmanagerYML"]
        self.prometheusYML = self.config["paths"]["prometheusYML"]
        self.skel = os.path.join(os.getcwd(), "skel")
        self.rulesYML = self.config["paths"]["rulesYML"]

    def print_header(self, page="main"):
        if page=="main":
            print_message('WELCOME TO STRESS TESTER', color='blue', centered=True)
        elif page=="setup":
            print_message('WELCOME TO STRESS TESTER - SETUP', color='magenta', centered=True)
        elif page=="node_test":
            print_message('WELCOME TO STRESS TESTER - NODE EXPORTER', color='orange', centered=True)


        print_br()
        print_message('By - Shubham Namdev', color = 'blue')
        print('For more info, visit -> ', end = '')
        print_message(f'{self.github}', 'green')
        print_br()

    def print_ipInfo(self):
        print('Prometheus is running on : ', end = '')
        print_message('localhost:9090', 'magenta')

        if not self.IPnodeEx and not self.IPmysql :
            print("Node Exporter IP : ", end='')
            print_message('Not Defined', color = 'red')
            print("MySQL IP : ", end='')
            print_message('Not Defined', color = 'red')
        else:
            print("Node Exporter IP : ", end='')
            if self.IPnodeEx:
                print_message(self.IPnodeEx, color = 'green')
            else:
                print_message('Not Defined', color = 'red')

            print("MySQL IP : ", end='')
            if self.IPmysql :
                print_message(self.IPmysql , color = 'green')
            else:
                print_message('Coming Soon...', color = 'red')
        print_br()

    def restart_services(self) -> None:

        try:
            os.system('systemctl restart prometheus')
            print("\033[92mRestarted :\033[0m Prometheus Service")
        except Exception as e:
            print(e)

        try:
            os.system('systemctl restart alertmanager')
            print("\033[92mRestarted :\033[0m Alertmanager Service")
        except Exception as e:
            print(e)

    def reset(self, mode :str='main') -> None:
        prom_skel = f'{self.skel}/prombkp.yml'
        rules_skel = f'{self.skel}/rulesbkp.yml'
        sqlrules_skel = f'{self.skel}/sqlrulesbkp.yml'
        alertmanager_skel = f'{self.skel}/alertmanagerbkp.yml'

        print("Resetting")

        try:
            os.system(f'cp {prom_skel} {self.prometheusYML}')
            print("\033[92mRestored :\033[0m prometheus.yml")
        except Exception as e:
            print(e)

        try:
            os.system(f'cp {rules_skel} {self.rulesYML}')
            print("\033[92mRestored :\033[0m rules.yml")
        except Exception as e:
            print(e)

        try:
            os.system(f'cp {sqlrules_skel} {self.sqlrulesYML}')
            print("\033[92mRestored :\033[0m sqlrules.yml")
        except Exception as e:
            print(e)

        try:
            os.system(f'cp {alertmanager_skel} {self.alertmanagerYML}')
            print("\033[92mRestored :\033[0m alertmanager.yml")
        except Exception as e:
            print(e)

        if mode == 'all':
            try:
                with open(self.json_file, 'r') as f:
                    config = json.load(f)

                config["ip"]["node_exporter"] = ""
                config["ip"]["mysql"] = ""

                with open(self.json_file, 'w') as f:
                    json.dump(config, f, indent=4)
                print("\033[92mRestored :\033[0m config.json")
            except Exception as e:
                print(e)
        self.restart_services()
        print_message("Reset Complete!", color='green')
        print_message("...", color='red')
        time.sleep(1)
        self.load_variables()

    def check(self) -> bool:
        clear()
        self.print_header("main")
        self.load_variables()
        if not (self.IPmysql or self.IPnodeEx):
            print_message("No IPs are defined !", color='red')
            print_message("Do you want to configure IPs now? (y : continue,  any : Exit)", color='magenta')
            ch = input(">> ")
            match ch:
                case "y":
                    print_message("Opening Setup Page...", color="yellow")
                    time.sleep(1)
                    self.setup()
                case _ :
                    print_message("Thank You!", color="yellow")
                    print_message("Exiting...", color="red")
                    time.sleep(1)
                    exit()
            if not (self.IPmysql or self.IPnodeEx):
                return False
            else :
                return True
        else:
            return True

    def ipCheck(self, ip :str) -> bool:
        try:
            socket.inet_pton(socket.AF_INET, ip)
            return True
        except socket.error:
            try:
                socket.inet_pton(socket.AF_INET6, ip)
                return True
            except socket.error:
                return False

    def updateIP(self, ip:str, mode:str) :

        self.load_variables()
        self.reset()

        if mode == "NE":
            self.config['ip']['node_exporter'] = ip

            with open(self.json_file, 'w') as f:
                json.dump(self.config, f, indent=4)

        elif mode == "SQL":
            self.config['ip']['mysql'] = ip

            with open(self.json_file, 'w') as f:
                json.dump(self.config, f, indent=4)

        else:
            print_message("No mode selected!", color='red')
            print_message("Going Back...", color='red')
            time.sleep(1)
            clear()

        self.load_variables()

        if self.IPmysql:

            target = f"""
  - job_name: mysql
    static_configs:
      - targets: ["{self.IPmysql}:9104"]

    """
            with open(self.prometheusYML, 'a') as f:
                f.write(target)

            self.restart_services()
            print_message("Mysql IP Added Successfully!", color='green')

        if self.IPnodeEx:
            target = f"""
  - job_name: node_exporter
    static_configs:
      - targets: ["{ip}:9200"]
            """

            with open(self.prometheusYML, 'a') as f:
                f.write(target)

            self.restart_services()
            print_message("Node Exporter IP Added Successfully!", color='green')


    def add_target(self, mode:str) -> None:
        self.load_variables()
        if mode=="NE":
            ip = ""
            set_ip = self.IPnodeEx

            if set_ip:
                print("Current IP : ", end=' ')
                print_message(f'{set_ip}', color='magenta')

            print("Enter IP of Node ")
            print_message("enter 'q' to exit", color='magenta')
            while not ip:
                ip = input('> ')
                if ip:
                    if ip.lower() == 'q':
                        ip=""
                        self.setup()
                    elif not self.ipCheck(ip):
                        print_message(f"Invalid IP : {ip}", color='red')
                        print("Please Enter a Valid IP Address")
                        ip = ""
                else:
                    print("Please enter IP Address to continue.")


            if set_ip:
                ch = input('Do you want to overwrite? (y/n) : ')
                if ch == 'y':
                    self.reset()
                    self.updateIP(ip, 'NE')
                else:
                    self.setup()
            elif ip:
                self.updateIP(ip, 'NE')
            return

        elif mode=="SQL":
            ip = ""
            set_ip = self.config['ip']['mysql']

            if set_ip:
                print("Current IP : ", end=' ')
                print_message(f'{set_ip}', color='magenta')

            print("Enter IP of Node ")
            print_message("enter 'q' to exit", color='magenta')
            while not ip:
                ip = input("> ")
                if ip:
                    if ip.lower() == 'q':
                        ip=""
                        self.setup()
                    elif not self.ipCheck(ip):
                        print_message(f"Invalid IP : {ip}", color='red')
                        print("Please Enter a Valid IP Address")
                        ip = ""
                else:
                    print("Please enter IP Address to continue.")

            if set_ip:
                ch = input('Do you want to overwrite? (y/n) : ')
                if ch == 'y':
                    self.reset()
                    self.updateIP(ip, 'SQL')
                else:
                    self.setup()
            elif ip:
                self.updateIP(ip, 'SQL')

            return 0

    def mysql_testing(self, page=1):
        clear()
        print("Coming Soon...")
        time.sleep(1)

    def node_testing(self, page=1):
        clear()
        self.print_header("node_test")
        print_message("WARNING: The following actions may damage your computer.", color='red')
        print_message("Please make sure you understand the risks before proceeding.", color='red')
       
        
        print("""Please Select Test Type - 
1. High CPU Usage Alerting
2. High Memory Usage Alerting
3. Low Disk Space Alerting
4. Network Traffic Tester
5. Exit""")
        ch = input(">> ")

        match ch:
            case '1':
                nt.cpuTest()
            case '2':
                nt.memTest() 
            case '3':
                nt.diskTest() 
            case '4':
                nt.networkAttack()
            case '5':
                print_message("Going Back to Main Page...", color='green')
                time.sleep(1)
                return False
            case _:
                print_message("Invalid Respose...", color='red')
                time.sleep(1)
        return True
       
              

    def setup(self) -> None:
        clear()
        self.print_header('setup')
        print_message("Please Select the Node Type :")

        ch = input("""
\033[33m1)\033[0m Add Node Exporter Node
\033[33m2)\033[0m Add MySQL Node
\033[33m3)\033[0m Reset Setings
\033[33m4)\033[0m Exit
>> """)

        match ch:
            case '1':
                self.add_target("NE")

            case '2':
                clear()
                print_message("Coming Soon...", color="cyan")
                #self.add_target("SQL")
                time.sleep(2)
                clear()
            case '3':
                self.reset('all')
            case '4':
                print_message('Going back to Main Page', color='green')
                time.sleep(1)
                clear()
                return False
            case _:
                print_message("Invalid Choice!", color='red')
                time.sleep(1)


        return True

    def main(self) -> None:
        clear()
        self.load_variables()
        self.print_header()
        self.print_ipInfo()
        chk = False
        while not chk:
            chk = self.check()

        if not self.IPmysql and self.IPnodeEx:
            print_message("MySQL Node not Defined!", color='red')
            print('Node Exporter Set for Stress Testing.')
            # print_message("Do you want to Stress Test - Node Exporter Node?", color='orange')
            print_message("Do you want to Begin Stress Test?", color='orange')
            print("\033[33my\033[0m : yes")
            # print("\033[33mn (any)\033[0m : open setup page")
            print("\033[33mq\033[0m : exit")

            ch = input(">> ")
            if ch == 'y':
                ret = True
                while ret:
                    ret = self.node_testing(0)
            else :
                return False
            # else:
            #     print_message("Opening Setup page...", color='magenta')
            #     time.sleep(1)
            #     ret = True
            #     while ret:
            #         ret = self.setup()
            #     return True

        elif not self.IPnodeEx and self.IPmysql:
            print_message("Node Exporter not Defined!", color='red')
            print('MySQL Set for Stress Testing.')
            print_message("Do you want to Stress Test - MySQL Node?", color='orange')
            print("\033[33my\033[0m : continue")
            print("\033[33mn (any)\033[0m : open setup page")
            print("\033[33mq\033[0m : exit")

            ch = input(">> ")
            if ch == 'y':
                self.mysql_testing(0)
            elif ch == 'q':
                return False
            else:
                print_message("Opening Setup page...", color='magenta')
                time.sleep(1)
                ret = True
                while ret:
                    ret = self.setup()
                return True

        elif self.IPnodeEx and self.IPmysql:
            print_message('Please Select the Node for Stress Testing : ', 'orange')
            ch = input(f"""\033[33m1)\033[0m Node Exporter : {self.IPnodeEx}
\033[33m2)\033[0m MySQL Node    : {self.IPmysql}
\033[33m3)\033[0m Open Setup Page
\033[33m4)\033[0m Exit
>> """)

            match ch:
                case '1':
                    ret = True
                    while ret:
                        ret = self.node_testing()

                case '2':
                    print_message("Coming Soon...", color='magenta')
                    time.sleep(1)
                    clear()
                    # self.mysql_testing()

                case '3':
                    print_message("Opening Setup page...", color='magenta')
                    time.sleep(1)
                    ret = True
                    while ret:
                        ret = self.setup()

                case '4':
                    clear()
                    print_message('Thank You For Your Time', color='green')
                    print_message('Exiting...', color='red')
                    time.sleep(1)
                    clear()
                    return False
                case _:
                    print_message('Invalid Choice!', color='red')
                    time.sleep(1)

        return True

    def run(self):
        clear()
        self.print_header()
        self.print_ipInfo()
        chk = False
        while not chk:
            chk = self.check()

        clear()
        self.print_header()
        self.print_ipInfo()

        print_message("Do you want to continue with above setting?", color='magenta')
        print("\033[95my\033[0m : continue\n\033[95mn\033[0m : Open Setup Page")
        ch = input("\033[33m>> \033[0m")
        match ch:
            case "y" :
                run = True
                while run:
                    run = self.main()
                clear()
                print_message('Thank You For Your Time', color='green')
                print_message('Exiting...', color='red')
                time.sleep(1)
                clear()
                exit()
            case _ :
                print_message("Opening Setup Page...", color="yellow")
                time.sleep(1)
                self.setup()
                self.run()


if __name__ == "__main__":
    app = StressTester()

