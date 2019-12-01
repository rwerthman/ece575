from src.WriteBack import WriteBack
from src.ControlUnit import ControlUnit
from src.InstructionDecode import InstructionDecode
from src.InstructionFetch import InstructionFetch
from src.MemoryAccess import MemoryAccess
from src.Execution import Execution

import unittest

class WriteBackTestCase( unittest.TestCase ):

    def testExecute( self ):
        controlUnit = ControlUnit()
        controlUnit = ControlUnit()
        IF = InstructionFetch( [] )
        ID = InstructionDecode( controlUnit, IF )
        EX = Execution( controlUnit, ID )
        MEM = MemoryAccess( controlUnit, ID, EX )
        WB = WriteBack( controlUnit, ID, EX, MEM )

        controlUnit.MemToReg = 0
        ID.writeRegister = "r3"
        MEM.readData = 0
        EX.ALUResult = 5

        WB.execute()

        self.assertEqual( ID.readFromRegister( "r3" ), 5 )


if __name__ == '__main__':  
    unittest.main()