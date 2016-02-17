import gtmagent

def agent():

    current_region = ''

    data = {}

    command = 'lke show -all'.split()
    for line in gtmagent.run(command):
        if "%GTM-I-NOLOCKMATCH" in line:
            fields = line.split()
            current_region = fields[7]
            data[current_region] = {}
        if "%GTM-I-LOCKSPACEUSE" in line:
            fields = line.split()
            data[current_region]['percentFree'] = fields[5]
            data[current_region]['totalPages'] = fields[7]

    return data
            
