class MemoryAccess( object ):

    def __init__( self ):
        self.mMemWrite = False
        self.mMemRead = False
        self.mDataMemory = [0, 0, 0, 0]
        self.mALUResult = None
        self.mReadData = None
    
    def execute( self, aALUResult):
        self.mALUResult = aALUResult
    
    def ReadMemory( self, address ):
        # if self.MemRead:
        pass
    
    def WriteMemory( self, address, data ):
        # if self.MemWrite:
        pass