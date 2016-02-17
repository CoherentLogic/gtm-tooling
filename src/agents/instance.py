import gtmagent
import os
import lockspace

def agent():
    
    instance_user = os.environ['USER']
    instance_home = os.environ['HOME']
    gtm_routines = os.environ['gtmroutines']
    gtm_global_directory = os.environ['gtmgbldir']

    repl_side = os.environ['REPL_SIDE']
    
    files = {}

    command = 'dse all -dump'.split()
    for line in gtmagent.run(command):
        if "Region" in line and "Seqno" not in line: 
            fields = line.split()
            files[current_file]['region'] = fields[1]


        if len(line) > 0:
            fields = line.split()

            if len(fields) > 0:
                if fields[0] == 'File':
                    current_file = fields[1]
                    files[current_file] = {}

            if line[0] == ' ':
                
                if "Access method" in line:
                    files[current_file]['accessMethod'] = fields[2]
                    files[current_file]['globalBuffers'] = fields[5]

                if "Reserved Bytes" in line:
                    files[current_file]['reservedBytes'] = fields[2]
                    files[current_file]['blockSize'] = fields[7]

                if "Maximum record size" in line:
                    files[current_file]['maximumRecordSize'] = fields[3]
                    files[current_file]['startingVBN'] = fields[6]

                if "Maximum key size" in line:
                    files[current_file]['maximumKeySize'] = fields[3]
                    files[current_file]['totalBlocks'] = fields[6]

                if "Null subscripts" in line:
                    files[current_file]['nullSubscripts'] = fields[2]
                    files[current_file]['freeBlocks'] = fields[5]

                if "Standard Null Collation" in line:
                    files[current_file]['standardNullCollation'] = fields[3]
                    files[current_file]['freeSpace'] = fields[6]
                
                if "Last Record Backup" in line:
                    files[current_file]['lastRecordBackup'] = fields[3]
                    files[current_file]['extensionCount'] = fields[6]

                if "Last Database Backup" in line:
                    files[current_file]['lastDatabaseBackup'] = fields[3]
                    files[current_file]['localMaps'] = fields[8]

                if "Last Bytestream Backup" in line:
                    files[current_file]['lastBytestreamBackup'] = fields[3]
                    files[current_file]['lockSpace'] = fields[6]
                
                if "In critical section" in line:
                    files[current_file]['inCriticalSection'] = fields[3]
                    files[current_file]['timersPending'] = fields[6]

                if "Cache freeze id" in line:
                    files[current_file]['cacheFreezeID'] = fields[3]
                    files[current_file]['flushTimer'] = fields[6]

                if "Current transaction" in line:
                    files[current_file]['currentTransaction'] = fields[2]
                    files[current_file]['numWritesPerFlush'] = fields[6]
                
                if "Certified for Upgrade to" in line:
                    files[current_file]['maximumTN'] = fields[2]
                    files[current_file]['certifiedForUpgradeTo'] = fields[7]

                if "Maximum TN Warn" in line:
                    files[current_file]['maximumTNWarn'] = fields[3]
                    files[current_file]['desiredDBFormat'] = fields[7]
                
                if "Master Bitmap Size" in line:
                    files[current_file]['masterBitmapSize'] = fields[3]
                    files[current_file]['blocksToUpgrade'] = fields[7]

                if "Create in progress" in line:
                    files[current_file]['createInProgress'] = fields[3]
                    files[current_file]['modifiedCacheBlocks'] = fields[7]
                
                if "Reference count" in line:
                    files[current_file]['referenceCount'] = fields[2]
                    files[current_file]['waitDisk'] = fields[5]
                
                if "Journal State" in line:
                    files[current_file]['journalState'] = fields[2]
                    if len(fields) > 3:
                        files[current_file]['journalBeforeImaging'] = fields[6]

                if "Journal Allocation" in line:
                    files[current_file]['journalAllocation'] = fields[2]
                    files[current_file]['journalExtension'] = fields[5]

                if "Journal Buffer Size" in line:
                    files[current_file]['journalBufferSize'] = fields[3]
                    files[current_file]['journalAlignSize'] = fields[6]

                if "Journal AutoSwitchLimit" in line:
                    files[current_file]['journalAutoSwitchLimit'] = fields[2]
                    files[current_file]['journalEpochInterval'] = fields[6]

                if "Journal Yield Limit" in line:
                    files[current_file]['journalYieldLimit'] = fields[3]
                    files[current_file]['journalSyncIO'] = fields[7]

                if "Journal File:" in line:
                    files[current_file]['journalFile'] = fields[2]

                if "Mutex Hard Spin Count" in line:
                    files[current_file]['mutexHardSpinCount'] = fields[4]
                    files[current_file]['mutexSleepSpinCount'] = fields[9]

                if "Mutex Queue Slots" in line:
                    files[current_file]['mutexQueueSlots'] = fields[3]
                    files[current_file]['killsInProgress'] = fields[7]

                if "Replication State" in line:
                    files[current_file]['replicationState'] = fields[2]
                    files[current_file]['regionSequenceNumber'] = fields[5]

                if "Zqgblmod Seqno" in line:
                    files[current_file]['zqgblmodSequenceNumber'] = fields[2]
                    files[current_file]['zqgblmodTrans'] = fields[5]

                if "Endian Format" in line:
                    files[current_file]['endianFormat'] = fields[2]
                    files[current_file]['commitWaitSpinCount'] = fields[7]

                if "Database file encrypted" in line:
                    files[current_file]['databaseFileEncrypted'] = fields[3]
                    files[current_file]['instFreezeOnError'] = fields[8]
                
                if "Spanning Node Absent" in line:
                    files[current_file]['spanningNodeAbsent'] = fields[3]
                    files[current_file]['maximumKeySizeAssured'] = fields[8]

                if "Defer allocation" in line:
                    files[current_file]['deferAllocation'] = fields[2]


    if repl_side == 'PRIMARY':
        import replication_source
        source_server_data = replication_source.agent()

    lock_data = lockspace.agent()

    data = {'instanceUser': instance_user,
            'instanceHome': instance_home,
            'routinePath': gtm_routines,
            'globalDirectory': gtm_global_directory,
            'gtmLocation': os.environ['gtm_dist'],            
            'files': files,
            'zquitAnyway': os.environ['gtm_zquit_anyway'],
            'log': os.environ['gtm_log'],
            'prompt': os.environ['gtm_prompt'],
            'noCEnable': os.environ['gtm_nocenable'],
            'bufferSize': os.environ['gtm_buffer_size'],
            'zinterruptAction': os.environ['gtm_zinterrupt'],
            'gtmBoolean': os.environ['gtm_boolean'],
            'gtmETrap': os.environ['gtm_etrap'],
            'lockData': lock_data,
            'replication': { 'role': repl_side,
                             'controlFile': os.environ['gtm_repl_instance'],
                             'instanceName': os.environ['gtm_repl_instname'],
                             'secondaryInstance': os.environ['gtm_repl_instsecondary'],
                             'source_server': source_server_data}
            }

    return data
