import gtmagent
import json

def agent():
    command = 'mupip replicate -source -checkhealth'.split()
    for line in gtmagent.run(command):
        if "PID" in line:
            fields = line.split()
            source_pid = fields[1]
            source_mode = fields[7]

    command = ('ps --pid=' + source_pid + ' -o cmd=').split()
    for line in gtmagent.run(command):
        source_command_line = line
        fields = source_command_line.split()
        for field in fields:
            if "secondary" in field:
                secondary_info = field.split('=')[1]
                secondary_server = secondary_info.split(':')[0]
                secondary_port = secondary_info.split(':')[1]
            if "buffsize" in field:
                buffer_size = field.split('=')[1]
            if "log" in field:
                log_path = field.split('=')[1]
                                
    command = 'mupip replicate -source -showbacklog'.split()
    for line in gtmagent.run(command):
        if "backlog number" in line:
            fields = line.split()
            backlog_count = fields[0]
        if "written to journal pool" in line:
            fields = line.split()
            last_journal_pool_seq = fields[0]
        if "sent by source server" in line:
            fields = line.split()
            last_sent_seq = fields[0]

    data = { 'pid': source_pid, 
             'mode': source_mode,
             'backlog': backlog_count,
             'lastWritten': last_journal_pool_seq,
             'lastSent': last_sent_seq,
             'commandLine': source_command_line,
             'secondaryServer': secondary_server,
             'secondaryPort': secondary_port,
             'bufferSize': buffer_size,
             'logPath': log_path
             }
        
    return data

