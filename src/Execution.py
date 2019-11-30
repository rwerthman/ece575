class Execution( object ):

    def __init__( self ):
        self.mALUOp = 0
        self.mALUDate1 = None
        self.mALUDate2 = None
        self.mALUResult = None
    
    def execute( self, aOpCode, aALUData1, aALUData2 ):

        self.mALUOp = self.getALUOp( aOpCode )

        # Add
        if self.mALUOp == 0:
            self.mALUResult = aALUData1 + aALUData2
    
    def getALUOp( self, aOpCode ):
        if aOpCode == "add":
            return 0


