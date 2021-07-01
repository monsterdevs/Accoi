"""
This module is to fetch logs from a ghost machine. It supports both Access
and DDC logging.
"""

import re
import time

import paramiko


class FetchGhostLogs:
    """
    Class that has several methods which are leveraged to fetch
    logs from a ghost machine
    """
    def __init__(self, inputs):
        """
        Receives input in json format and assign their values to class
        variables to be used in function of this module
        """
        self.ip = inputs["ip"]

        if "startTime" in inputs:
            self.startTime = inputs["startTime"]
        if "endTime" in inputs:
            self.endTime = inputs["endTime"]

        self.ghost_dest = "/tmp/ghostlog.txt"
        self.rotate_ghost_logs()
        ghostfile = self.check_ghost_mode()

        if "reqID" in inputs:
            self.reqID = inputs["reqID"]
            self.log_contents = self.fetchGhostLogsWithRequestID(
                self.ip, ghostfile, self.reqID
            )
        else:
            lines = self.get_Ghost_arf(
                self.ip, self.startTime, self.endTime, ghostfile
            )
            self.log_contents = self.fetchGhostLogs(
                self.ip, self.startTime, self.endTime, lines
            )
        # print(self.log_contents)
        # return self.log_contents

    def get_result(self):
        """Function to return the logs"""
        return self.log_contents

    def get_Ghost_arf(self, ip, startTime, endTime, ghostfile):
        """Function to get ghost's arf"""
        time.sleep(10)
        # logger.info("Sleeping for some time ")
        cmdConstant = (
            "/a/sbin/arf --from "
            + str(startTime)
            + " --to "
            + str(endTime)
            + " /a/logs/"
            + ghostfile
        )
        # logger.info(cmdConstant)
        lines = self.executeCommand(ip, cmdConstant)
        # lines = lines.split("\n")
        lines = lines.strip()
        lines = lines.split("\n")

        # logger.info(lines)
        return lines

    def check_ghost_mode(self):
        """Function to check logging mode"""
        cmdConstant = "/a/bin/tbl-fetch 0 ghostmon ghostvars | grep billing"
        result = self.executeCommand(self.ip, cmdConstant)
        mode_num = re.findall(r"([0-9]+)$", result.decode())
        mode_num = "".join(mode_num)
        if mode_num == "4":
            ghostfile = "ghost.access.log"
        elif mode_num == "10":
            ghostfile = "ghost.ddc.log"
        # logger.info(ghostfile)
        return ghostfile

    def fetchGhostLogs(self, ip, startTime, endTime, lines):
        """Function to fetch ghost logs"""
        for line in lines:
            # logger.info(line)
            if line == "/a/logs/ghost.ddc.log":
                cmdConstant = "zcat " + line + ".gz"

            elif line == "/a/logs/ghost.access.log":
                cmdConstant = "zcat " + line + ".gz"

            elif line[-2:] == "gz":
                cmdConstant = (
                    "zcat "
                    + line
                    + ' | awk -F"|" \' $2 > '
                    + str(startTime)
                    + " && $2 < "
                    + str(endTime)
                    + " '"
                )
            else:
                cmdConstant = (
                    "cat "
                    + line
                    + ' | awk -F"|" \' $2 > '
                    + str(startTime)
                    + " && $2 < "
                    + str(endTime)
                    + " '"
                )

        # logger.info(cmdConstant)
        log_contents = self.executeCommand(ip, cmdConstant)
        log_contents = log_contents.split("\n")
        return log_contents

    def fetchGhostLogsWithRequestID(self, ip, line, reqID=""):
        """Function to fetch ghost logs with request id"""
        if line == "/a/logs/ghost.ddc.log":
            cmdConstant = "zcat " + line + ".gz" + " |grep " + reqID

        elif line == "/a/logs/ghost.access.log":
            cmdConstant = "zcat " + line + ".gz" + " |grep " + reqID

        elif line[-2:] == "gz":
            cmdConstant = "zcat " + "/a/logs/" + line + " |grep " + reqID
        else:
            cmdConstant = (
                "zcat " + "/a/logs/" + line + ".gz" + "|grep " + reqID
            )
            # logger.info(line)

        # logger.info(cmdConstant)
        log_contents = self.executeCommand(ip, cmdConstant)
        log_contents = log_contents.decode()
        log_contents = log_contents.split("\n")

        return log_contents

    def rotate_ghost_logs(self):
        """Function rotate ghost logs"""
        cmdConstant = "/a/bin/ghost -k rotate"
        self.executeCommand(self.ip, cmdConstant)

    def executeCommand(self, ip, cmdConstant):
        """Function to remotely execute commands using paramiko"""
        # logger.info("executing the command %s" % (cmdConstant))
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.load_system_host_keys()
        client.connect(ip, username="root", timeout=300)
        cmd = cmdConstant
        _, stdout, _ = client.exec_command(cmd)

        return stdout.read().strip().decode("utf-8")
        # return stdout.read().strip()
